# SPDX-FileCopyrightText: 2025 Alva Theaters
#
# SPDX-License-Identifier: GPL-3.0-or-later

'''
__________________________________________________________________________________
EVENT MANAGER OBJECTIVES:

This script is here to define what happens on events like play, stop, 
scrub, frame change, and translate/transform. This script encompasses
3D audio and lighting, but most of the code is for lighting.

We need to basically simulate a full-blown theatrical lighting console
and Dolby Atmos sound system inside Blender. Unlike a lighting console,
Sorcerer works primarily with f-curves. That presents many unique 
challenges. 

    Objective 1. Harmonize.
        Traditional animation is different from ALVA lighting animation
        because traditional 3D animation doesn't usually require 
        controlling hundreds of completely separate objects at once, 
        outside simulations at least. For this reason, we need to use
        a controller-based approach where you control objects more 
        indirectly. However, you can have hundreds of different controllers, 
        and each controller can target whatever it wants whenever it wants.
        As a result, they can tend to disagree. So we need to harmonize
        the disagreements so we don't spam the lighting console with 
        contradictory commands. We also want to simplify them as best
        we can to minimize bandwidth usage. We even give the user 
        Level of Detail (LOD) options they can use to make less important 
        controllers only go every other frame or every third frame.

    Objective 2. Sync.
        We need to keep the lighting console's timecode clock in sync with 
        Blender's timecode clock during playback. We do this with singular
        OSC commands, not by actually streaming a continuous timecode 
        signal. This way, it's far, far simpler for the end user. It even 
        works through WiFi. We can get away with this where others can't 
        because Sorcerer is not intended for realtime use at FOH during 
        final shows. It's a lot like how you don't keep a video editor
        open when you show a movie to an audience. You instead render out
        the movie, close the video editor (in this case Sorcerer), and play
        back the movie with something else that's far better for a realtime,
        high stress, high reliability environment.

        In addition to just keeping timecode in sync, we also have little
        optional things we'd like to do on play and on stop. For example,
        turning the house lights down a little on play, turning them back
        up on stop, firing the latest cue in the sequencer if we are starting
        from the middle of a cue sequence (otherwise you would have to 
        constantly scrub backwards to fire the most relevant cue or the stage
        may look completely wrong for the moment you're working on.) The 
        user can turn all these things off and on in Sorcerer Preferences.

    Objective 3. Fix Blender's Depsgraph.
        Blender's depsgraph system does not automatically run the updaters
        of custom properties when they are updated by fcurves during frame 
        change or playback. That means we need to sort of build our own 
        depsgraph system that just looks for stuff that changed since the 
        last frame. That way we know what stuff needs to be done during frame
        change.

    Objective 4 (solved by automation.py).
        Say you use Sorcerer to make a super emotional, lifelike, fluid,
        organic, natural, and lively lighting animation that is so amazing
        that no one has ever seen stage lights move, dance and breath the way
        you just made them move, dance, and breath. But the problem you
        now have is that Blender does this stuff by sending a crap ton of
        OSC commands. It's not very reliable. It lags. It's slow. It really
        stinks for continuous, real-time playback. It's fine for design work
        but certainly not for the final show. It's like video editors: the 
        playback inside the video editor kind of stinks until you render the 
        video. So we need a way to get all the animation stuff (and other 
        types of stuff) from Blender onto the console where it can be 
        "played back" reliably.

        If you want to play a Blender animation on a lighting console, you 
        can't just load the .blend file on the lighting console and merge 
        the f-curve data onto, well, there's nothing to merge it to. Lighting 
        consoles kinda sorta do super simple curves in their effect editors, 
        but those are extremely primitive compared to the graph editors in 3D 
        animation suites like Blender and Maya. So we need a way to force-feed 
        this f-curve data down the console's throat in a way it can understand.

        So what we do is we basically have this automatic Orb assistant 
        manually animate the sequence on the console frame-by-frame by hitting 
        record cue for every frame. And then we bind each cue to the right 
        timecode frame on the console's event list.

        We call the end result a "qmeo". A qmeo is like a video, but every 
        frame is a lighting cue, not a picture. To make a qmeo actually work, 
        we need 4 things:

            a. The console needs to have the cue for each timecode frame
               stored on its own hard drive, preferably in an out-of-the-way
               cue list. The cue transition time needs to reflect the frame
               rate.

            b. The console needs to have an event list that binds each cue
               to its respective timecode frame. This way we don't have to
               worry about them getting out of sync from using imprecise 
               cue timings.

            c. The user needs an extremely simple way to record and play 
               back these qmeos. Preferably, the user is able to just go to
               a specific cue or fire a specific macro. The qmeo plays, the
               qmeo finishes, and the qmeo stops its own clock when its done
               so that the user doesn't have to.

            d. While Sorcerer is building a qmeo, the user needs to be able
               to escape out of that process without terminating Blender. 
               Especially if they accidentally started to build a super long
               qmeo.

        We solve all these problems with the Orb assistant. Most buttons 
        in Sorcerer's UI that use the purple orb icon are Orb operators. 
        See automation_manager.py to learn how we do it.


    Objective 5 (solved by the CPV folder).
        Sorcerer is almost its own full blown lighting console with its own army 
        of different controller types that can all be trying to do stuff to the 
        same stuff at once. That creates two problems:
         
            1. Sorcerer does not send DMX, it doesn't have a patch page,
               but it still needs to know things about specific fixtures or 
               its commands to the lighting console won't make any sense.

            2. We can't have all our controllers speaking whatever language they 
               choose. They need to all speak the same language. That language is 
               called CPV. A CPV request is a tuple in the form of

               (Channel, Parameter, Value)

        Every single controller that ever wants to make a change to a parameter
        on the console must make a change request in the CPV format. This 
        is how we keep everything sorted out in the data flow.

        We need to keep this so organized because we often need to do a ton of 
        stuff to the requests to make them kosher for the fixture on the console.
        For example, mapping values to the right min/max, appending appropriate 
        enable and disable commands for things like strobe (we definitely don't
        want the user to have to manually enable such things. If they increase 
        strobe value, we can reasonably infer they want the strobe on), and 
        setting the argument to be relative or absolute based on the controller
        type. We complete all these operations at various stages, so the CPV
        format is very important.

        See the cpv folder to see how we manage the primary control flow.

        
    Objective 6. 3D Audio Panner.
        This is currently out of order, but will be repaired soon. If you need 
        it, go back to Alva Sequencer where it still works.

        Actually just kidding, it's fixed now, just need to update this...


Hopefully that provides you a general idea of what Sorcerer does, what kinds 
of problems it solves, and how it solves them.
'''

LEGEND = '''
<INTERNAL OR EXTERNAL SIDE EFFECT>_<ActionName>_<REVERSE_LOCATION>

prefix
IN_ = has internal side effects
EX_ = has external side effects, such as on the lighting console
INEX_ = internal and external side effects

suffix 
_[the name of the CONSTANT list where the side effect is reversed]
_NOREV = Side effect is not and does not need to be reversed
'''

from .events import *

ADDON_REGISTER  = [
    IN_LoadMacroButtons_NOREV  # This just loads a dumb UI list. Must be done here because of dumb Blender context rules. 
]

DEPSGRAPH_UPDATE = [ # Also added to FRAME_LOAD, or frame_change_pre bpy handler, since depsgraph does not fire on frame change.
    IN_UpdateSpyContext_NOREV,  # Update spy API's spy.context, our version of bpy.context, for Sorcerer's needs. Reduce finder funcs.
    INEX_SoundFlies_NOREV,  # Render the 3D audio soundscape. Make birds fly. Make helicopters soar.
    IN_SetTransformableControllers_DEPSGRAPH_FRAME_PUBLISH,  # Find stuff like SEM's, drivers, influencers, etc
    IN_SetTransformingControllers_NOREV,  # Find the ones actually transforming.
    IN_SetTransformablesOld_NOREV,  # Store current stuff in memory so we can compare next time.
    EX_FireTransformUpdates_NOREV,  # Fire the update/CPV process based on those transforms.
    EX_FireSEM_NOREV  # Fire the update/CPV on the SEM ones.
]

PLAY = [
    IN_SetPlayingTrue_STOP,  # This helps us track the context for the fade engine.
    EX_HouseLightsDown_STOP,  # Can't see the stage lighting with house up, so decrease.
    IN_SetStripMapping_STOP,  # Create a map of all lighting strips in the sequencer with options = {'EVENT_MANAGER'}
    EX_StartLightingClock_STOP,  # Start the event list clock on the lighting console.
    EX_StartMusic_STOP,  # Play the song on Qlab if there's a sound stip with a music cue set.
    EX_FireCuehead_NOREV  # Fire the most recent cue not about to be triggered normally to correct lighting-state.
]

FRAME_LOAD = [
    EX_Scrubbing_NOREV,  # If user scrubs in Blender, we need to update the console since we don't stream true timecode.
    EX_FireStrips_NOREV,  # Use the strip mapping dictionary to fire strip stuff if there's stuff in current frame's key.
    IN_SetUseHarmonizerTrue_FRAME_PUBLISH,  # For context-tracking for the fade engine stuff.
    IN_SetLightingControllersList_FRAME_LOAD,  # Find all the lighting controllers in the scene we need to check.
    IN_SetLightingUpdatesList_FRAME_PUBLISH,  # Check those controllers for changes (from animation f-curves).
    IN_FireLightingUpdatesList_NOREV,  # Fire the update/CPV process for those animation changes since Blender won't.
    IN_ClearControllersIfNotPlaying_FRAME_LOAD  # Clear the memory if it may not be the same next time (not in playback).
]

FRAME_PUBLISH = [
    IN_SetLightingRequests_FRAME_PUBLISH,  # Store all current CPV requests.
    IN_HarmonizeLightingRequests_NOREV,  # Harmonize those so they do not conflict with each other.
    EX_BatchSendLighting_NOREV,  # Send them in batches, not in 1,000 separate packets.
    IN_SetUseHarmonizerFalse_FRAME_LOAD,  # Update context.
    IN_ClearLightingRequests_FRAME_LOAD  # Clear memory for next time.
]

STOP = [
    IN_SetPlayingFalse_PLAY,  # Update context.
    EX_HouseLightsUp_PLAY,  # Turn the house lights back up since other people exist too.
    EX_StopLightingClocks_PLAY,  # Stop the event list clocks on the console.
    EX_StopMusic_PLAY,  # Stop the music on Qlab.
    IN_ClearStripMapping_PLAY  # Clear strip mapping memory.
]
