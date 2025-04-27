# SPDX-FileCopyrightText: 2025 Alva Theaters
#
# SPDX-License-Identifier: GPL-3.0-or-later

import bpy
import time

from ..utils.event_utils import EventUtils
from ..utils.orb_utils import find_executor


class TimelineSync:
    '''
    This is where we create qmeos. Remember, a qmeo is like a video, but each frame is a lighting cue,
    not a picture. This is how we get Blender animation data stored locally on a lighting console.
    
    This script is just one very small part of a larger system called Orb. It's sort of the middle man
    between the upper level operator and the DSL. The DSL is for step-by-step logic-less operations, 
    and this is where we do the Pythonic logic specific to each Orb operator. And then there's yet another
    middle man between here and the actual DSL—-the installed lighting console. Because all this logic 
    here can work on multiple lighting console brands, as long as the Console class is installed properly.
    '''
    def __init__(self, context, active_item):
        self.scene = context.scene
        self.frame_rate = EventUtils.get_frame_rate(context.scene)
        self.start_frame = context.scene.frame_start
        self.end_frame = context.scene.frame_end

        self.event_list = find_executor(context.scene, context.scene, 'event_list')
        self.start_macro = find_executor(context.scene, context.scene, 'start_macro')
        self.end_macro = find_executor(context.scene, context.scene, 'end_macro')
        self.cue_list = find_executor(context.scene, context.scene, 'cue_list')


    def execute(self, Console):
        yield from Console.record_timecode_macro(self.start_macro, self.event_list, state='enable')
        yield from Console.record_timecode_macro(self.end_macro, self.event_list, state='disable')

        frames = list(range(int(self.start_frame), int(self.end_frame)))
        cue_duration = round(1 / self.frame_rate, 2)

        yield from Console.delete_recreate_event_list(self.event_list, self.end_frame, self.frame_rate)
        yield Console.delete_cue_list(self.cue_list), "Recreating cue list"

        wm = bpy.context.window_manager
        wm.progress_begin(0, 100)
 
        for i, frame in enumerate(frames):
            yield from self.qmeo_frame(Console, frame, cue_duration, wm, frames, i)

        wm.progress_end()
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

        final_frame = frames[-1]
        timecode = EventUtils.frame_to_timecode(final_frame) # Ensure this event has a time component even if something above got skipped
        
        yield Console.final_event_stop_clock(self.event_list, final_frame, timecode, self.end_macro), "Setting final event to stop clock"
        yield Console.reset_cue_list(), "Resetting cue list"

    def qmeo_frame(self, Console, frame, cue_duration, wm, frames, i):
        # Get ready to record cue with the new CPV updates.
        current_frame_number = self.scene.frame_current
        argument_one = Console.make_record_qmeo_cue_argument(self.cue_list, current_frame_number, cue_duration)

        # Get ready to record the cue while also binding cue to its event.
        timecode = EventUtils.frame_to_timecode(frame)
        argument_two = Console.make_record_qmeo_event_argument(self.event_list, frame, timecode)

        wm.progress_update(i / len(frames) * 100)
        
        # Go ahead and actually send the final command
        self.scene.frame_set(frame)
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
        time.sleep(.1)
        yield Console.send_frame(argument_one, argument_two), "Recording frame"
        time.sleep(self.scene.orb_chill_time)
