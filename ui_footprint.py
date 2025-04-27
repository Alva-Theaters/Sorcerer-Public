# SPDX-FileCopyrightText: 2025 Alva Theaters
#
# SPDX-License-Identifier: GPL-3.0-or-later

from .as_ui import *

'''
This file is just a table of contents. 

    DO add stuff here if you are adjusting the UI footprint. 
    DO NOT add logic here. No ifs, no else's, no try excepts, no register functions. Just data.

Goal is to allow code-reader to exit early without wasting time reading through irrelevant, imperative code.
'''


class Topbar:
    appends = [
        (TOPBAR_MT_editor_menus, "prepend", draw_alva_topbar),  # [orb_icon] + [blender_icon] at the top left corner
        (TOPBAR_MT_edit, "append", draw_alva_edit),  # Sorcerer Preferences is on the main Edit menu, just like Blender's
        (TOPBAR_MT_render, "prepend", draw_alva_render),  # Render qmeo for scene
        (TOPBAR_MT_window, "append", draw_alva_window),  # Toggle the Topbar stuff on and off
        (TOPBAR_MT_help, "append", draw_alva_help),  # Manual, Tutorials, Support, and Community for Sorcerer
    ]


class View3D:
    panels = [
        VIEW3D_PT_alva_object_controller,  # An ML Editor like on ETC Eos that doesn't take up half the damn screen
        VIEW3D_PT_alva_lighting_modifiers,  # Control the lightscape with photo-editing-like tools
        VIEW3D_PT_alva_fixture_groups,  # Make, edit, and delete lighting groups
        VIEW3D_PT_alva_fixture_generator,  # Patch ETC Eos remotely from Sorcerer
        VIEW3D_PT_alva_service_mode,  # Debug Sorcerer directly from Blender in a secret UI panel
        VIEW3D_PT_alva_toolbar  # Quick buttons
    ]

    appends = [
        (VIEW3D_MT_view, "append", draw_alva_view3d_view),  # Toggle cmd_line and tool_settings
        (VIEW3D_HT_header, "append", draw_alva_view3d_cmd_line),  # Command line to ETC Eos
        (VIEW3D_HT_tool_header, "prepend", draw_alva_view3d_tool_settings)  # Network and ML Editor
    ]


class Sequencer:
    panels = [
        SEQUENCER_PT_alva_Lighting,  # Lighting-related controllers for the visual sequencer
        SEQUENCER_PT_alva_Video,  # Coming soon
        SEQUENCER_PT_alva_Audio,  # 3D audio-related controls for the visual sequencer
        SEQUENCER_PT_alva_toolbar  # Quick buttons
    ]

    appends = [
        (SEQUENCER_MT_view, "append", draw_alva_sequencer_view),  # Toggles for Add, Strip, and Cmd Line
        (SEQUENCER_MT_add, "append", draw_alva_sequencer_add_menu),  # Add Macro, Trigger, Cue, Flash, or Animation strips
        (SEQUENCER_MT_strip, "append", draw_alva_sequencer_strip_menu),  # Sequencer behavior toggles
        (SEQUENCER_HT_header, "append", draw_alva_sequencer_cmd_line),  # Command line for sequencer, not the console
    ]


class Node:
    panels = [
        NODE_PT_alva_node_formatter,  # Tool to help change things like name and color on nodes faster
        NODE_PT_alva_fixture_generator,  # Repeat of the remote patch panel in view3d
        NODE_PT_alva_fixture_groups,  # Repeat of the groups panel in view3d
        NODE_PT_alva_toolbar  # Quick buttons
    ]

    appends = [
        (NODE_MT_add, "append", draw_alva_node_add),  # Add our node types
        (NODE_HT_header, "append", draw_alva_node_header),  # Basically a mini version of Node Formatter
        (NODE_MT_view, "append", draw_alva_node_view),  # Toggle Add, Toolbar, and Formatter
    ]


class Graph:
    panels = [
        GRAPH_PT_alva_graph_groups,  # Access lighting groups from graph editor too
        GRAPH_PT_alva_graph_controllers  # Complete 100% of your work without ever leaving graph editor, if you wish
    ]

    appends = [
        (GRAPH_HT_header, "append", draw_alva_graph_header),  # Just the View Selected operator
    ]


class Scene:
    panels = [
        SCENE_PT_alva_cue_switcher,  # Take and fade between lighting cues just like on a video broadcast panel
        SCENE_PT_alva_stage_manager  # Stage-manage shows like a badass rocket launch director
    ]

    appends = [
        (PROPERTIES_HT_header, "append", draw_alva_view3d_tool_settings),  # Network settings
    ]


class Time:
    panels = [
        TIME_PT_alva_flags,  # Disable and enable groups together, like Nodes, Strips, Objects, etc
    ]

    appends = [
        (DOPESHEET_HT_header, "append", draw_alva_time_header),  # Global time and render settings
        (TIME_PT_playback, "prepend", draw_alva_time_playback),  # Draws timecode_expected_lag on built-in Playback popover
        (TIME_MT_view, "append", draw_alva_time_view),  # Toggle entire header
    ]


class Text:
    panels = [
        TEXT_PT_alva_macro_generator,  # Create multi-line macros for Eos in the text editor, with QWERTY and Copy/Paste
        TEXT_PT_alva_import_patch,  # Populate the Blender/Sorcerer scene from a USITT ASCII file created by the console
    ]

    appends = [
        (TEXT_HT_header, "append", draw_alva_view3d_tool_settings),  # Network settings
        (TEXT_MT_view, "append", draw_text_view),  # Toggle Network settings
        (TEXT_MT_templates, "prepend", draw_text_templates_menu),  # Python templates menu for Sorcerer's own add-on system
    ]


class RightClick:
    panels = [
        WM_MT_button_context,  # Import this built-in panel using pass
    ]

    appends = [
        (WM_MT_button_context, "append", draw_alva_right_click),  # Add to built-in panel
        (VIEW3D_MT_object_context_menu, "append", draw_alva_right_click),  # Add to view3d
        (SEQUENCER_MT_context_menu, "append", draw_alva_right_click),  # Add to sequencer
    ]
