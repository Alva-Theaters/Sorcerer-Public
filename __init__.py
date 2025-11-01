# This file is part of Alva Sorcerer.
# Copyright (C) 2025 Alva Theaters

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''
==================================================================================
                           DESIGNED BY ALVA THEATERS
                            FOR THE SOLE PURPOSE OF
                              MAKING PEOPLE HAPPY
==================================================================================
'''

BECOME_A_STAGE_SORCERER = '''Hey there. You know what Blender is, right? It's this 
3D animation software that's pretty similar to the stuff they use to make animated 
movies like Frozen and Toy Story. And you know how at those big concerts how they 
have these armies of robot lights that move a lot? And you you know what Dolby Atmos 
is, right? It basically lets you make it sound like a helicopter is flying over your 
head in a theater. And you know how at those really big stadium concerts they 
sometimes have robot cameras that automatically point themselves at performers? And 
you know how in Blender, that 3D animation software, you control 3D characters with 
animation keyframes, and graph editors, and dopesheets, and NLA editors, to give you 
super detailed control?

Well, Alva Sorcerer connects Blender to the stage. 

ALVA stands for Animated Lighting, Video & Audio. Not automation, not show control, 
animation. Keyframes galore!

With Sorcerer, you can animate a stage with the same precision they get when 
animating Wall-E and Rapunzel and Toothless. The stage is now your character. 
Make it dance! Make it cry! Make it jump for joy!'''

bl_info = {
    "name": "Alva Sorcerer",
    "author": "Alva Theaters",
    "location": "ShaderEditor/View3D/Sequencer/TextEditor/Properties/GraphEditor",
    "version": (2, 2, 2),
    "blender": (4, 4, 1),
    "description": "3D animation in real life, for theatre, with Blender.",
    "wiki_url": "https://alva-sorcerer.readthedocs.io/en/latest/index.html#",
    "tracker_url": "https://sorcerer.alvatheaters.com/support",
    "category": "Stage Animation",
}

as_info = {
    "alpha": False,
    "beta": True,
    "rating": "Experimental",
    "restrictions_url": "https://github.com/Alva-Theaters/Sorcerer/discussions/55"
}

import bpy

from .source.addon_register import (
    assert_directory_name,
    assert_no_duplicates,
    assert_blender_version,
    append_spy_to_sys_modules,
)


def register():
    from .extendables_bpy import register_bpy_data
    from .extendables_spy import register_spy_data  # Sorcerer's own version of bpy, totally separate from bpy.
    from .source.maintenance.blendfinals import register_blendfinals_data  # Hook into integration testing add-on.

    assert_directory_name()
    assert_no_duplicates()
    assert_blender_version()
    append_spy_to_sys_modules()

    from .source.draw.icons.load_icons import register_icons
    register_icons()
    
    register_bpy_data()
    register_spy_data()
    register_blendfinals_data()
    bpy.app.timers.register(on_register, first_interval=.01)


def on_register():
    from .source.maintenance.unit_tests import test_sorcerer  # Unit testing runs on add-on register.
    from .source.events.jobs.on_addon_register import IN_OnRegister_NOREV
    from .source.spy.context import tag_update

    tag_update(bpy.context.scene)
    test_sorcerer()
    IN_OnRegister_NOREV(None, None).execute() # Requires this bpy.context.


def unregister():
    from .source.maintenance.blendfinals import unregister_blendfinals_data
    from .extendables_bpy import unregister_bpy_data
    from .extendables_spy import unregister_spy_data
    from .source.draw.icons.load_icons import unregister_icons
    unregister_blendfinals_data()
    unregister_spy_data()
    unregister_bpy_data()
    unregister_icons()
