# SPDX-FileCopyrightText: 2025 Alva Theaters
#
# SPDX-License-Identifier: GPL-3.0-or-later

from bpy import spy
import time

from ..utils.osc import OSC
from .orb_DSL.parser import Parser

'''
To make your own custom Sorcerer sequencer strip type:

    1. Copy/paste the code below directly into Blender's text editor.
    2. Modify it as needed.
    3. Run it.
    4. Select your new strip type in the M menu that pops up when you have  color strip selected.

The strip types below are built into Sorcerer. Similar to Blender's bpy, Sorcerer's spy is
utilized both by the internal source code (as seen here) and by end-users extending the application.
'''


class CPV_LC_eos(spy.types.LightingConsole):
    as_idname = 'option_eos'
    as_label = "ETC Eos"
    as_description = "Eos-family console type"

    osc_address = "/eos/newcmd"
    rounding_points = 0

    absolute = {
        "intensity": "# at $ Enter",
        "pan": "# Pan at $ Enter",
        "tilt": "# Tilt at $ Enter",
        "diffusion": "# Diffusion at $ Enter",
        "strobe": "# Shutter_Strobe at $ Enter",
        "zoom": "# Zoom at $ Enter",
        "iris": "# Iris at $ Enter",
        "edge": "# Edge at $ Enter",
        "gobo": "# Gobo_Select at $ Enter",
        "gobo_speed": "# Gobo_Mode 191 Enter, # Gobo_Index/Speed at $ Enter",
        "changer_speed": "# Changer_Speed at $ Enter",
        "prism": "# Beam_Fx Select $ Enter",
        "rgb": "# Red at $1 Enter, # Green at $2 Enter, # Blue at $3 Enter",
        "cmy": "# Cyan at $1 Enter, # Magenta at $2 Enter, # Yellow at $3 Enter",
        "rgbw": "# Red at $1 Enter, # Green at $2 Enter, # Blue at $3 Enter, # White at $4 Enter",
        "rgba": "# Red at $1 Enter, # Green at $2 Enter, # Blue at $3 Enter, # Amber at $4 Enter",
        "rgbl": "# Red at $1 Enter, # Green at $2 Enter, # Blue at $3 Enter, # Lime at $4 Enter",
        "rgbaw": "# Red at $1 Enter, # Green at $2 Enter, # Blue at $3 Enter, # Amber at $4 Enter, # White at $5 Enter",
        "rgbam": "# Red at $1 Enter, # Green at $2 Enter, # Blue at $3 Enter, # Amber at $4 Enter, # Mint at $5 Enter",
    }

    increase = {
        "raise_intensity": "# at + $ Enter",
        "raise_pan": "# Pan at + $ Enter",
        "raise_tilt": "# Tilt at + $ Enter",
        "raise_diffusion": "# Diffusion at + $ Enter",
        "raise_strobe": "# Shutter_Strobe at + $ Enter",
        "raise_zoom": "# Zoom at + $ Enter",
        "raise_iris": "# Iris at + $ Enter",
        "raise_edge": "# Edge at + $ Enter",
        "raise_gobo": "# Gobo_Select at + $ Enter",
        "raise_gobo_speed": "# Gobo_Mode 191 Enter, # Gobo_Index/Speed at + $ Enter",
        "raise_changer_speed": "# Changer_Speed at + $ Enter",
        "raise_prism": "# Beam_Fx Select + $ Enter",
        "raise_rgb": "# Red at + $1 Enter, # Green at + $2 Enter, # Blue at + $3 Enter",
        "raise_cmy": "# Cyan at + $1 Enter, # Magenta at + $2 Enter, # Yellow at + $3 Enter",
        "raise_rgbw": "# Red at + $1 Enter, # Green at + $2 Enter, # Blue at + $3 Enter, # White at + $4 Enter",
        "raise_rgba": "# Red at + $1 Enter, # Green at + $2 Enter, # Blue at + $3 Enter, # Amber at + $4 Enter",
        "raise_rgbl": "# Red at + $1 Enter, # Green at + $2 Enter, # Blue at + $3 Enter, # Lime at + $4 Enter",
        "raise_rgbaw": "# Red at + $1 Enter, # Green at + $2 Enter, # Blue at + $3 Enter, # Amber at + $4 Enter, # White at + $5 Enter",
        "raise_rgbam": "# Red at + $1 Enter, # Green at + $2 Enter, # Blue at + $3 Enter, # Amber at + $4 Enter, # Mint at + $5 Enter",
    }

    decrease = {
        "lower_intensity": "# at - $ Enter",
        "lower_pan": "# Pan at - $ Enter",
        "lower_tilt": "# Tilt at - $ Enter",
        "lower_diffusion": "# Diffusion at - $ Enter",
        "lower_strobe": "# Shutter_Strobe at - $ Enter",
        "lower_zoom": "# Zoom at - $ Enter",
        "lower_iris": "# Iris at - $ Enter",
        "lower_edge": "# Edge at - $ Enter",
        "lower_gobo": "# Gobo_Select at - $ Enter",
        "lower_gobo_speed": "# Gobo_Mode 191 Enter, # Gobo_Index/Speed at - $ Enter",
        "lower_changer_speed": "# Changer_Speed at - $ Enter",
        "lower_prism": "# Beam_Fx Select - $ Enter",
        "lower_rgb": "# Red at - $1 Enter, # Green at - $2 Enter, # Blue at - $3 Enter",
        "lower_cmy": "# Cyan at - $1 Enter, # Magenta at - $2 Enter, # Yellow at - $3 Enter",
        "lower_rgbw": "# Red at - $1 Enter, # Green at - $2 Enter, # Blue at - $3 Enter, # White at - $4 Enter",
        "lower_rgba": "# Red at - $1 Enter, # Green at - $2 Enter, # Blue at - $3 Enter, # Amber at - $4 Enter",
        "lower_rgbl": "# Red at - $1 Enter, # Green at - $2 Enter, # Blue at - $3 Enter, # Lime at - $4 Enter",
        "lower_rgbaw": "# Red at - $1 Enter, # Green at - $2 Enter, # Blue at - $3 Enter, # Amber at - $4 Enter, # White at - $5 Enter",
        "lower_rgbam": "# Red at - $1 Enter, # Green at - $2 Enter, # Blue at - $3 Enter, # Amber at - $4 Enter, # Mint at - $5 Enter"
    }

    def __init__(self, scene):
        self.scene = scene

    def format_value(value):
        '''We have to do this stuff because Eos interprets "1" as 10, "2" as 20, etc.'''
        if -10 < value < 10:
            return f"{'-0' if value < 0 else '0'}{abs(value)}"
        return str(value)
    


    # Common Actions --------------------------------------------------------------------------------------------------
    def key(self, key_strings):
        if not isinstance(key_strings, list):
            key_strings = [key_strings]

        for key_string in key_strings:
            OSC.press_lighting_key(key_string)

    
    def key_up(self, key_string):
        OSC.send_osc_lighting(f"/eos/key/{key_string}", "0", tcp=True)


    def key_down(self, key_string):
        OSC.send_osc_lighting(f"/eos/key/{key_string}", "1", tcp=True)


    def enter(self, key_string):
        OSC.send_osc_lighting(f"/eos/key/{key_string}", "1", tcp=True)
        OSC.send_osc_lighting(f"/eos/key/{key_string}", "1", tcp=True)


    def softkey(self, key_string):
        OSC.send_osc_lighting(f"/eos/softkey/{key_string}", "1", tcp=True)
        OSC.send_osc_lighting(f"/eos/softkey/{key_string}", "0", tcp=True)


    def softkey_up(self, key_string):
        OSC.send_osc_lighting(f"/eos/softkey/{key_string}", "0", tcp=True)


    def softkey_down(self, key_string):
        OSC.send_osc_lighting(f"/eos/softkey/{key_string}", "1", tcp=True)


    def cmd(self, command_string):
        OSC.send_osc_lighting(self.osc_address, command_string, tcp=True)


    def raw(self, pairs):
        if not isinstance(pairs, list):
            pairs = [pairs]

        for (address, argument) in pairs:
            OSC.send_osc_lighting(address, argument, tcp=True)


    def save_console_file(self):
        if self.scene.is_console_saving:
            self.key_down("shift")
            self.key("update")
            time.sleep(2)
            self.key_up("shift")


    def prepare_console_for_automation(self):
        yield self.record_snapshot(), "Saving your screen"
        yield self.save_console_file(), "Saving the console file"


    def record_snapshot(self):
        snapshot = str(self.scene.orb_finish_snapshot)
        self.cmd(f"Record Snapshot {snapshot} Enter Enter")


    def restore_snapshot(self):
        snapshot = str(self.scene.orb_finish_snapshot)
        self.cmd(f"Snapshot {snapshot} Enter")


    def restore_console_to_normal_following_automation(self):
        self.key("live")
        yield self.restore_snapshot(), "Restoring your screen"


    def record_cue(self, cue_number, cue_duration):
        self.key("live")
        self.cmd(f"Cue {str(cue_number)} Time {cue_duration} Enter")

    def record_discrete_time(self, type_id, members_str, discrete_time):
        argument = f"{type_id} {members_str} Time {discrete_time.zfill(2)} Enter"
        self.cmd(argument)

    def update_cue(self):
        self.key(["update", "enter"])


    def delete_cue_list(self, cue_list):
        self.cmd(f"Delete Cue {cue_list} / Enter Enter")

    def reset_cue_list(self):
        self.cmd("Cue 1 / Enter")

    def final_event_stop_clock(self, event_list, final_frame, timecode, end_macro):
        self.cmd(f"Event {event_list} / {str(final_frame)} Time {str(timecode)} Show_Control_Action Macro {str(end_macro)} Enter")


    def make_record_qmeo_cue_argument(self, cue_list, current_frame_number, cue_duration):
        return f"Record Cue {str(cue_list)} / {str(current_frame_number)} Time {str(cue_duration)} Enter Enter"
    
    def make_record_qmeo_event_argument(self, event_list, frame, timecode):
        return f"Event {event_list} / {str(frame)} Time {str(timecode)} Show_Control_Action Cue {str(frame)} Enter"

    def send_frame(self, argument_one, argument_two):
        self.cmd(argument_one)
        self.cmd(argument_two)


    def prepare_patch(self):
        self.key("blind")
        self.cmd("Patch Enter")

    def patch_light(self, chan, pos_x, pos_y, pos_z, or_x, or_y, or_z, uni, addr):
        self.cmd(f"Chan {chan} Position {pos_x} / {pos_y} / {pos_z} Enter, Chan {chan} Orientation {or_x} / {or_y} / {or_z} Enter, Chan {chan} at {str(uni)} / {str(addr)} Enter")

    def select_lights(self, lights):
        self.cmd(f"Chan {lights} Enter Enter Full Enter")

    def record_group(self, lights, group_number):
        self.key("live")
        self.cmd(f"Chan {lights} Record Group {group_number} Enter Enter")


    def record_one_line_macro(self, macro_number, macro_text):
        yield from Parser(self).execute('eos', 'record_one_line_macro', macro_number=macro_number, macro_text=macro_text)

    def record_multiline_macro(self, macro_number, tokens):
        yield from Parser(self).execute('eos', 'record_multiline_macro', macro_number=macro_number, tokens=tokens)

    def record_timecode_macro(self, macro_number, event_list_number, state='enable'):
        yield from Parser(self).execute('eos', 'record_timecode_macro', macro_number=macro_number, event_list_number=event_list_number, state=state)

    def delete_recreate_event_list(self, event_list_number, end_frame, fps):
        end_frame -= 1
        yield from Parser(self).execute('eos', 'delete_recreate_event_list', event_list_number=event_list_number, end_frame=end_frame, fps=fps)

    def patch_sem(self, fixture, sem_chan, pos_x, pos_y, pos_z, or_x, or_y, or_z, focus_palette):
        yield from Parser(self).execute('eos', 'patch_sem', fixture=fixture, sem_chan=sem_chan, pos_x=pos_x, pos_y=pos_y, pos_z=pos_z, or_x=or_x, or_y=or_y, or_z=or_z, focus_palette=focus_palette)

class CPV_LC_grandma_3(spy.types.LightingConsole):
    as_idname = 'grandma3'
    as_label = "grandMA3"
    as_description = "grandMA3 family console type"

    osc_address = "/cmd"
    rounding_points = 2

    absolute = {
        "intensity": "Fixture # at $",
        "pan": "Fixture #; Attribute Pan at $",
        "tilt": "Fixture #; Attribute Tilt at $",
        "diffusion": "Fixture #; Attribute Frost1 at $",
        "zoom": "Fixture #; Attribute Zoom at $",
        "iris": "Fixture #; Attribute Iris at $",
        "edge": "Fixture #; Attribute Focus1 at $",
        "rgb": "Fixture #; Attribute ColorRGB_R at $1; Attribute ColorRGB_G at $2; Attribute ColorRGB_B at $3",
        "cmy": "Fixture #; Attribute ColorRGB_C at $1; Attribute ColorRGB_M at $2; Attribute ColorRGB_Y at $3",
        "rgbw": "Fixture #; Attribute ColorRGB_R at $1; Attribute ColorRGB_G at $2; Attribute ColorRGB_B at $3; Attribute ColorRGB_W at $4",
        "rgba": "Fixture #; Attribute ColorRGB_R at $1; Attribute ColorRGB_G at $2; Attribute ColorRGB_B at $3; Attribute ColorRGB_A at $4",
        "rgbl": "Fixture #; Attribute ColorRGB_R at $1; Attribute ColorRGB_G at $2; Attribute ColorRGB_B at $3; Attribute ColorRGB_L at $4",
        "rgbaw": "Fixture #; Attribute ColorRGB_R at $1; Attribute ColorRGB_G at $2; Attribute ColorRGB_B at $3; Attribute ColorRGB_A at $4; Attribute ColorRGB_W at $5",
        "rgbam": "Fixture #; Attribute ColorRGB_R at $1; Attribute ColorRGB_G at $2; Attribute ColorRGB_B at $3; Attribute ColorRGB_A at $4; Attribute ColorRGB_M at $5",
    }

    increase = {
        "raise_intensity": "Fixture # at + $",
        "raise_pan": "Fixture #; Attribute Pan at + $",
        "raise_tilt": "Fixture #; Attribute Tilt at + $",
        "raise_diffusion": "Fixture #; Attribute Frost1 at + $",
        "raise_zoom": "Fixture #; Attribute Zoom at + $",
        "raise_iris": "Fixture #; Attribute Iris at + $",
        "raise_edge": "Fixture #; Attribute Focus1 at + $",
        "raise_rgb": "Fixture #; Attribute ColorRGB_R at + $1; Attribute ColorRGB_G at + $2; Attribute ColorRGB_B at + $3",
        "raise_cmy": "Fixture #; Attribute ColorRGB_C at + $1; Attribute ColorRGB_M at + $2; Attribute ColorRGB_Y at + $3",
        "raise_rgbw": "Fixture #; Attribute ColorRGB_R at + $1; Attribute ColorRGB_G at + $2; Attribute ColorRGB_B at + $3; Attribute ColorRGB_W at + $4",
        "raise_rgba": "Fixture #; Attribute ColorRGB_R at + $1; Attribute ColorRGB_G at + $2; Attribute ColorRGB_B at + $3; Attribute ColorRGB_A at + $4",
        "raise_rgbl": "Fixture #; Attribute ColorRGB_R at + $1; Attribute ColorRGB_G at + $2; Attribute ColorRGB_B at + $3; Attribute ColorRGB_L at + $4",
        "raise_rgbaw": "Fixture #; Attribute ColorRGB_R at + $1; Attribute ColorRGB_G at + $2; Attribute ColorRGB_B at + $3; Attribute ColorRGB_A at + $4; Attribute ColorRGB_W at + $5",
        "raise_rgbam": "Fixture #; Attribute ColorRGB_R at + $1; Attribute ColorRGB_G at + $2; Attribute ColorRGB_B at + $3; Attribute ColorRGB_A at + $4; Attribute ColorRGB_M at + $5",
    }
    
    decrease = {
        "lower_intensity": "Fixture # at - $",
        "lower_pan": "Fixture #; Attribute Pan at - $",
        "lower_tilt": "Fixture #; Attribute Tilt at - $",
        "lower_diffusion": "Fixture #; Attribute Frost1 at - $",
        "lower_zoom": "Fixture #; Attribute Zoom at - $",
        "lower_iris": "Fixture #; Attribute Iris at - $",
        "lower_edge": "Fixture #; Attribute Focus1 at - $",
        "lower_rgb": "Fixture #; Attribute ColorRGB_R at - $1; Attribute ColorRGB_G at - $2; Attribute ColorRGB_B at - $3",
        "lower_cmy": "Fixture #; Attribute ColorRGB_C at - $1; Attribute ColorRGB_M at - $2; Attribute ColorRGB_Y at - $3",
        "lower_rgbw": "Fixture #; Attribute ColorRGB_R at - $1; Attribute ColorRGB_G at - $2; Attribute ColorRGB_B at - $3; Attribute ColorRGB_W at - $4",
        "lower_rgba": "Fixture #; Attribute ColorRGB_R at - $1; Attribute ColorRGB_G at - $2; Attribute ColorRGB_B at - $3; Attribute ColorRGB_A at - $4",
        "lower_rgbl": "Fixture #; Attribute ColorRGB_R at - $1; Attribute ColorRGB_G at - $2; Attribute ColorRGB_B at - $3; Attribute ColorRGB_L at - $4",
        "lower_rgbaw": "Fixture #; Attribute ColorRGB_R at - $1; Attribute ColorRGB_G at - $2; Attribute ColorRGB_B at - $3; Attribute ColorRGB_A at - $4; Attribute ColorRGB_W at - $5",
        "lower_rgbam": "Fixture #; Attribute ColorRGB_R at - $1; Attribute ColorRGB_G at - $2; Attribute ColorRGB_B at - $3; Attribute ColorRGB_A at - $4; Attribute ColorRGB_M at - $5",
    }


consoles = [
    CPV_LC_eos,
    CPV_LC_grandma_3
]


def register():
    for cls in consoles:
        spy.utils.register_class(cls)


def unregister():
    for cls in reversed(consoles):
        spy.utils.as_unregister_class(cls)