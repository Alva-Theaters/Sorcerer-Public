# SPDX-FileCopyrightText: 2025 Alva Theaters
#
# SPDX-License-Identifier: GPL-3.0-or-later

from .operators import *


keymap_data = {
    "3D View": {
        "space_type": "VIEW_3D",
        "items": [
            ({"idname": "alva_object.object_controller", "key": 'P', "value": 'PRESS'}, None),
            ({"idname": "alva_tool.ghost_out", "key": 'G', "value": 'PRESS', "shift": True}, None)
        ]
    },
    "Sequencer": {
        "space_type": "SEQUENCE_EDITOR",
        "items": [
            ({"idname": "alva_sequencer.command_line", "key": 'C', "value": 'PRESS'}, None),
            ({"idname": "alva_orb.orb", "key": 'SPACE', "value": 'PRESS', "shift": True}, {'as_orb_id': 'sequencer'}),
            ({"idname": "alva_tool.ghost_out", "key": 'G', "value": 'PRESS', "shift": True}, None),
            ({"idname": "alva_sequencer.scale_strips", "key": 'S', "value": 'PRESS'}, None),
            ({"idname": "alva_sequencer.extrude_strips", "key": 'E', "value": 'PRESS'}, None),
            ({"idname": "alva_sequencer.duplicate_pattern", "key": 'E', "value": 'PRESS', "shift": True}, None),
            ({"idname": 'alva_common.deselect_all', "key": 'D', "value": 'PRESS'}, None),
            ({"idname": 'alva_sequencer.add_color', "key": 'Z', "value": 'RELEASE'}, None),
            ({"idname": 'alva_sequencer.add_color_kick', "key": 'Z', "value": 'PRESS'}, None),
            ({"idname": 'alva_sequencer.add_color_pointer', "key": 'Z', "value": 'PRESS', "shift": True}, None),
            ({"idname": 'alva_sequencer.bump_vertical', "key": 'U', "value": 'PRESS'}, {"direction": 1}),
            ({"idname": 'alva_sequencer.bump_vertical', "key": 'U', "value": 'PRESS', "shift": True}, {"direction": -1}),
            ({"idname": 'alva_sequencer.bump_horizontal', "key": 'L', "value": 'PRESS'}, {"direction": -1}),
            ({"idname": 'alva_sequencer.bump_horizontal', "key": 'R', "value": 'PRESS'}, {"direction": 1}),
            ({"idname": 'alva_sequencer.bump_horizontal', "key": 'L', "value": 'PRESS', "shift": True}, {"direction": -5}),
            ({"idname": 'alva_sequencer.bump_horizontal', "key": 'R', "value": 'PRESS', "shift": True}, {"direction": 5}),
            ({"idname": "alva_sequencer.properties", "key": 'M', "value": 'PRESS'}, None),
            ({"idname": "alva_sequencer.formatter", "key": 'F', "value": 'PRESS'}, None)
        ]
    },
    "Node Editor": {
        "space_type": "NODE_EDITOR",
        "items": [
            ({"idname": "alva_node.formatter", "key": 'F', "value": 'PRESS'}, None),
            ({"idname": "alva_tool.ghost_out", "key": 'G', "value": 'PRESS', "shift": True}, None)
        ]
    },
    "Property Editor": {  # Cue Switcher
        "space_type": "PROPERTIES",
        "items": [
            ({"idname": "alva_cue.take", "key": 'ONE', "value": 'PRESS'}, {"index": 1}),
            ({"idname": "alva_cue.take", "key": 'TWO', "value": 'PRESS'}, {"index": 2}),
            ({"idname": "alva_cue.take", "key": 'THREE', "value": 'PRESS'}, {"index": 3}),
            ({"idname": "alva_cue.take", "key": 'FOUR', "value": 'PRESS'}, {"index": 4}),
            ({"idname": "alva_cue.take", "key": 'FIVE', "value": 'PRESS'}, {"index": 5}),
            ({"idname": "alva_cue.take", "key": 'SIX', "value": 'PRESS'}, {"index": 6}),
            ({"idname": "alva_cue.take", "key": 'SEVEN', "value": 'PRESS'}, {"index": 7}),
            ({"idname": "alva_cue.take", "key": 'EIGHT', "value": 'PRESS'}, {"index": 8}),
            ({"idname": "alva_cue.take", "key": 'NINE', "value": 'PRESS'}, {"index": 9}),
            ({"idname": "alva_cue.take", "key": 'ZERO', "value": 'PRESS'}, {"index": 10}),

            ({"idname": "alva_cue.take", "key": 'ONE', "value": 'PRESS', "shift": True}, {"index": 11}),
            ({"idname": "alva_cue.take", "key": 'TWO', "value": 'PRESS', "shift": True}, {"index": 12}),
            ({"idname": "alva_cue.take", "key": 'THREE', "value": 'PRESS', "shift": True}, {"index": 13}),
            ({"idname": "alva_cue.take", "key": 'FOUR', "value": 'PRESS', "shift": True}, {"index": 14}),
            ({"idname": "alva_cue.take", "key": 'FIVE', "value": 'PRESS', "shift": True}, {"index": 15}),
            ({"idname": "alva_cue.take", "key": 'SIX', "value": 'PRESS', "shift": True}, {"index": 16}),
            ({"idname": "alva_cue.take", "key": 'SEVEN', "value": 'PRESS', "shift": True}, {"index": 17}),
            ({"idname": "alva_cue.take", "key": 'EIGHT', "value": 'PRESS', "shift": True}, {"index": 18}),
            ({"idname": "alva_cue.take", "key": 'NINE', "value": 'PRESS', "shift": True}, {"index": 19}),
            ({"idname": "alva_cue.take", "key": 'ZERO', "value": 'PRESS', "shift": True}, {"index": 20})
        ]
    }
}


common_ops = [
    ORB_OT_sync,
    TOPBAR_OT_alva_settings,
    TOPBAR_OT_alva_splash_screen,
    COMMON_OT_alva_copy_patch,
    COMMON_OT_alva_home_controller,
    COMMON_OT_alva_update_controller,
    COMMON_OT_alva_parameter_popup,
    COMMON_OT_alva_clear_solo,
    COMMON_OT_alva_white_balance,
    COMMON_OT_alva_apply_patch,
    COMMON_OT_alva_add_group,
    COMMON_OT_alva_remove_group,
    COMMON_OT_alva_bump_group,
    COMMON_OT_alva_add_graph_controller,
    COMMON_OT_alva_remove_graph_controller,
    COMMON_OT_alva_bump_graph_controller,
    COMMON_OT_alva_remove_channel_from_group,
    TOOL_OT_alva_ghost_out,
    TOOL_OT_alva_displays,
    TOOL_OT_alva_about,
    TOOL_OT_alva_stop_clocks,
    TOOL_OT_alva_copy_various_to_selected,
    WM_OT_alva_show_message
]


view3d_ops = [
    VIEW3D_OT_alva_add_driver,
    VIEW3D_OT_alva_toggle_object_mute,
    VIEW3D_OT_alva_pull_fixture_selection,
    VIEW3D_OT_alva_add_lighting_modifier,
    VIEW3D_OT_alva_remove_lighting_modifier,
    VIEW3D_OT_alva_bump_lighting_modifier,
    VIEW3D_OT_alva_summon_movers,
    VIEW3D_OT_alva_object_controller,
    VIEW3D_OT_alva_duplicate_object,
    VIEW3D_OT_alva_align,
    VIEW3D_OT_alva_distribute
]


text_ops = [
    TEXT_OT_alva_populate_macros,
    TEXT_OT_alva_send_text_to_3d,
    TEXT_OT_alva_template_add
]


strip_formatter_ops = [
    SEQUENCER_OT_alva_select_similar,
    SEQUENCER_OT_alva_formatter_select,
    SEQUENCER_OT_alva_frame_jump,
    SEQUENCER_OT_alva_hotkey_hint,
    SEQUENCER_OT_alva_copy_strip_attribute,
    SEQUENCER_OT_alva_set_timecode,
    SEQUENCER_OT_alva_start_end_mapping,
    SEQUENCER_OT_alva_sync_video_to_audio
]


sequencer_hotkeys_ops = [
    SEQUENCER_OT_alva_scale_strips,
    SEQUENCER_OT_alva_extrude_strips,
    SEQUENCER_OT_alva_duplicate_pattern,
    SEQUENCER_OT_alva_deselect,
    SEQUENCER_OT_alva_new_strip,
    SEQUENCER_OT_alva_new_kick,
    SEQUENCER_OT_alva_new_pointer,
    SEQUENCER_OT_alva_bump_horizontal,
    SEQUENCER_OT_alva_bump_vertical,
    SEQUENCER_OT_alva_format_strip,
    SEQUENCER_OT_alva_strip_media,
    SEQUENCER_OT_alva_mute,
    SEQUENCER_OT_alva_tc_left_five,
    SEQUENCER_OT_alva_tc_left_one,
    SEQUENCER_OT_alva_tc_right_one,
    SEQUENCER_OT_alva_tc_right_five,
    SEQUENCER_OT_alva_select_channel
]


sequencer_macro_ops = [
    SEQUENCER_OT_alva_fire_start_macro,
    SEQUENCER_OT_alva_fire_end_macro,
    SEQUENCER_OT_alva_flash_copy_down
]


sequencer_misc_ops = [
    SEQUENCER_OT_alva_analyze_song,
    SEQUENCER_OT_alva_add_offset,
    SEQUENCER_OT_alva_generate_strips,
    SEQUENCER_OT_alva_add_color_strip,
    SEQUENCER_OT_alva_delete_events,
    SEQUENCER_OT_alva_command_line,
    TOOL_OT_alva_duplicate_strip_to_above,
    SEQUENCER_OT_alva_add,
    SEQUENCER_OT_alva_refresh_audio_object_selection,
    SEQUENCER_OT_alva_bake_audio
]


preferences_ops = [
    PREFERENCES_OT_alva_set_context_to_scene,
    PREFERENCES_OT_alva_democratic,
    PREFERENCES_OT_alva_nondemocratic,
    PREFERENCES_OT_alva_save_dtp
]


node_ops = [
    NODE_OT_alva_node_formatter,
    NODE_OT_remove_direct_select,
    NODE_OT_alva_direct_select,
    NODE_OT_alva_bump_direct_select_up,
    NODE_OT_alva_bump_direct_select_down,
    NODE_OT_add_direct_select,
    NODE_OT_alva_mixer_add_choice,
    NODE_OT_alva_mixer_remove_choice,
    NODE_OT_alva_color_grid_button
]


cue_switcher_ops = [
    PROPERTIES_OT_alva_take_cue,
    PROPERTIES_OT_alva_cue_cut,
    PROPERTIES_OT_alva_cue_auto,
    PROPERTIES_OT_alva_cue_blue,
    PROPERTIES_OT_alva_cue_black,
    PROPERTIES_OT_alva_cue_restore,
    PROPERTIES_OT_alva_add_cue_list,
    PROPERTIES_OT_alva_remove_cue_list,
    PROPERTIES_OT_alva_add_cue_to_list,
    PROPERTIES_OT_alva_remove_cue_from_list,
    PROPERTIES_OT_alva_cue_self
]
