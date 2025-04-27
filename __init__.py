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
=====================================================================
                      DESIGNED BY ALVA THEATERS
                       FOR THE SOLE PURPOSE OF
                         MAKING PEOPLE HAPPY
=====================================================================
'''

bl_info = {
    "name": "Alva Sorcerer",
    "author": "Alva Theaters",
    "location": "ShaderEditor/View3D/Sequencer/TextEditor/Properties/GraphEditor",
    "version": (2, 1, 0),
    "blender": (4, 1, 0),
    "description": "3D animation in real life, for theatre, with Blender.",
    "wiki_url": "https://alva-sorcerer.readthedocs.io/en/latest/index.html#",
    "tracker_url": "https://sorcerer.alvatheaters.com/support",
    "category": "EMARs",
}

as_info = { # Used in Sorcerer's splash
    "alpha": False,
    "beta": True,
    "rating": "Experimental",
    "restrictions_url": "https://github.com/Alva-Theaters/Sorcerer/discussions/55"
}

from .utils.register_addon import RegisterAndUnregister

PACKAGE = __package__ # Because importing the following relative dicts is outsourced.

BPY_REGISTRATION_DEPSGRAPH = {
    'ui_lists': 'as_ui.ui_lists',  # 1
    'property_groups': 'makesrna.property_groups',  # 2
    'lighting': 'nodes.lighting',  # 3
    'audio': 'nodes.audio',  # 4
    'register_operators': 'operators.register_operators', # 5
    'rna_text': 'makesrna.rna_text',  # 6
    'rna_preferences': 'makesrna.rna_preferences',  # 7
    'rna_sequencer': 'makesrna.rna_sequencer',  # 8
    'rna_scene': 'makesrna.rna_scene',  # 9
    'rna_common': 'makesrna.rna_common',  # 10
    'register_ui': 'as_ui.register_ui',  # 11
    'menus': 'as_ui.menus',  # 12
    'event_handlers': 'events.event_handlers',  # 13
    'keymap': 'operators.keymap',  # 14
}

SPY_REGISTRATION_DEPSGRAPH = {
    'fixture_parameters': 'extendables.fixture_parameters',  # 1
    'languages': 'extendables.languages',  # 2
    'lighting_consoles': 'extendables.lighting_consoles',  # 3
    'lighting_controllers': 'extendables.lighting_controllers',  # 4
    'sequencer_strips': 'extendables.sequencer_strips', # 5
}


def do_not_register_because_this_is_a_public_window_only():
    from .utils.register_addon import add_spy_api_to_bpy_api, append_on_register_function
    add_spy_api_to_bpy_api()
    RegisterAndUnregister().register(BPY_REGISTRATION_DEPSGRAPH, PACKAGE)
    RegisterAndUnregister().register(SPY_REGISTRATION_DEPSGRAPH, PACKAGE)
    append_on_register_function()


def do_not_unregister_because_this_is_a_public_window_only():
    RegisterAndUnregister().unregister(SPY_REGISTRATION_DEPSGRAPH, PACKAGE)
    RegisterAndUnregister().unregister(BPY_REGISTRATION_DEPSGRAPH, PACKAGE)
