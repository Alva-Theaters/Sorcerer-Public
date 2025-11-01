# SPDX-FileCopyrightText: 2025 Alva Theaters
#
# SPDX-License-Identifier: GPL-3.0-or-later

'''
Alva Sorcerer is an authoring software for ALVA content. 
ALVA stands for Animated Lighting, Video, & Audio. 
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

from .source.events import *


ADDON_REGISTER  = [
    IN_OnRegister_NOREV  # Boring technical stuff. 
]

DEPSGRAPH_UPDATE = [ # Also added to FRAME_LOAD
    IN_UpdateSpyContext_NOREV,  # Heeeeeeey everyone, here's the stuff you need!
    INEX_SoundFlies_NOREV,  # Make birds fly. Make helicopters soar. Make the rain patter.
    IN_SetTransformableControllers_DEPSGRAPH_FRAME_PUBLISH,  # Find the moovy stuff.
    IN_SetTransformingControllers_NOREV,  # Find the moovy stuff that's moving.
    IN_SetTransformablesOld_NOREV,  # Write down where everyone is so we know who moved next time.
    EX_FireTransformUpdates_NOREV,  # Let the moovy stuff do their stuff.
    EX_FireSEM_NOREV,  # Make the cats (moving lights) chase the lasers (the mesh representing a SEM).
    EX_FireDrivers_NOREV,  # Just drag the unicorn up to make it light up!
]

PLAY = [
    IN_UpdateSpyContext_NOREV,  # This has to go here too because the Python API is not decoupled from pointer dereferences.*
    IN_SetPlayingTrue_STOP,  # Heeeeey everyone, show starts now!
    EX_HouseLightsDown_STOP,  # I can't see the stage lighting IF THE HOUSE LIGHTS ARE UP.
    IN_SetStripMapping_STOP,  # Figure out what the sequence editor strips want us to do and when.
    EX_StartLightingClock_STOP,  # Lighting console GO.
    EX_StartMusic_STOP,  # Somebody start the music. Anyone.
    EX_FireCuehead_NOREV  # Cue stack why do you NEVER pay attention to timeline scrubbing? Oh. We only tell you stuff during playback. You're supposed to be on cue 21 so we can see the transition between 21 and 22 but you're still on 49 so go to 21 now.
]

FRAME_LOAD = [
    IN_UpdateSpyContext_NOREV,  # This has to go here too because the Python API is not decoupled from pointer dereferences.*
    INEX_SoundFlies_NOREV,  # Make birds fly. Make helicopters soar. Make the rain patter.
    EX_Scrubbing_NOREV,  # Hey lighting console clock, just kidding, we're over here now.
    EX_FireStrips_NOREV,  # Do any stuff the sequence editor wanted us to do this frame.
    IN_SetUseHarmonizerTrue_FRAME_PUBLISH,  # Dude, stop, you're not the only one who matters now. Wait.
    IN_SetLightingControllersList_FRAME_LOAD,  # OK, who all can speak?
    IN_SetLightingUpdatesList_FRAME_PUBLISH,  # And who is speaking right now?
    IN_FireLightingUpdatesList_NOREV,  # Everyone who has stuff to say, figure out what you want to say.
    IN_ClearControllersIfNotPlaying_FRAME_LOAD  # There's no work tomorrow so fire all the employees.
]

FRAME_PUBLISH = [
    IN_SetLightingRequests_FRAME_PUBLISH,  # Collect everything everyone wanted to say.
    IN_HarmonizeLightingRequests_NOREV,  # Draft a settlement agreement so that no one gets upset.
    EX_BatchSendLighting_NOREV,  # Don't send the county a million emails each with its own settlement agreement.
    IN_SetUseHarmonizerFalse_FRAME_LOAD,  # Hey guys you can talk on your own now, don't need to wait anymore.
    IN_ClearLightingRequests_FRAME_LOAD  # Why does my desktop have 290,523 files on it?
]

STOP = [
    IN_SetPlayingFalse_PLAY,  # Show's over.
    EX_HouseLightsUp_PLAY,  # Hey yo. OTHER PEOPLE NEED TO SEE STUFF too.
    EX_StopLightingClocks_PLAY,  # Lighting console why are you still doing stuff? We're done.
    EX_StopMusic_PLAY,  # I can't hear the director if THE MUSIC IS STILL PLAYING
    IN_ClearStripMapping_PLAY  # The sequencer editor changes its hair color every morning so just give up.
]


''' 
*

What the heck does "the Python API is not decoupled from pointer dereferences" mean?

When you mess with stuff in Blender, Blender needs to tell all of Blender what you did so Blender 
can figure out what to do about it. That's the depsgraph. 

The Python API is what lets us do things with Blender using computer code without having to be a 
Blender god. 

Pointer dereferences is Blender god speak for Blender threw something away.

So what this whole phrase is saying is that when we do stuff while the depsgraph is doing stuff, 
the depsgraph might throw stuff away that we need. Because the Python API looks directly at stuff
the depsgraph might throw away. So we need to run a program that stores all the stuff we need, to 
decouple it from pointer dereferences manually.'''
