# SPDX-FileCopyrightText: 2025 Alva Theaters
#
# SPDX-License-Identifier: GPL-3.0-or-later

import bpy
from bpy.types import Object, Light, Node, PropertyGroup, Strip
import spy
from spy.rainbow import *
import time
from functools import wraps
from typing import Union, List

from .stop import check_flags
from .find_parent import FindParent
from .update_others import UpdateOtherSelections
from .publish.batch_send import batch_send
from .cpv_validate import is_invalid
from .publish.simplify import simplify

change_requests = []

def DEBUG():
    return bpy.context.scene.scene_props.service_mode


'''
The CPV system is essentially a communication protocol similar to DMX used only in Sorcerer.

A CPV request is a tuple containing Channel, Parameter, Value. 

A CPV request is made any time a single controller wishes to make a parameter change on the console.
We use the CPV protocol to standardize how all parameter change requests are made no matter the 
controller type, no matter the space_type. In frame change and during playback, CPV requests are
compared to one another for common simplification and harmonization to avoid spamming contradictory 
messages and to batch commands together.
'''

def time_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        if DEBUG(): spy.utils.alva_log('time', f"TIME: cpv_generator took {time.time() - start:.4f} seconds")
        return result
    return wrapper


class CPVGenerator:
    def __init__(self, controller, context, Parameter):
        self.controller: Union[Object, Light, Node, PropertyGroup, Strip] = controller
        self.Parameter: spy.types.FixtureParameter = Parameter
        self.parent: Union[Object, Light, Node, PropertyGroup, Strip] = FindParent(controller).execute()
        self.Engine: spy.types.Engine = spy.context.engine_selector.execute(self.parent)
        self.context = context
        self.should_stop = check_flags(self)
        self.use_harmonizer = context.scene.scene_props.use_harmonizer


    @time_logger
    def execute(self) -> None:
        if DEBUG(): spy.utils.alva_log('cpv_generator', f"\n{CPV}########################################################\n# CPV Update {GREEN}STARTING{CPV} for {RESET}{self.Parameter.as_idname}\n{CPV}########################################################")
        scene = self.context.scene.scene_props

        scene.restrict_spy_update = True

        if self.should_stop: 
            print_end_update("should_stop()")
            return
        
        CPVs: List[spy.types.CPV] = self.Engine.execute(self, self.Parameter)

        scene.restrict_spy_update = False

        if not CPVs:
            spy.utils.alva_log('cpv_generator', "No CPVs returned by engine.")
            print_end_update("No CPVs")
            return
        
        invalid_CPVs = [item for CPV in CPVs for item in (is_invalid(CPV) or [])]

        if invalid_CPVs:
            spy.utils.limp_mode(
                self.context, 
                systems=1, 
                label="Malformation", 
                error_type="CPV", 
                explanation=str(invalid_CPVs)
            )
            spy.utils.alva_log('cpv_generator', f"\n{RED}ERROR: {RESET}{invalid_CPVs}\n")
            print_end_update("Invalid CPVs")
            return

        if not scene.use_harmonizer:
            CPVs = simplify(CPVs)
        #else: simplify() responsibility moves to EX_BatchSendLighting_NOREV in frame_publish

        if self.use_harmonizer:
            global change_requests
            change_requests.extend(CPVs)
            if DEBUG(): spy.utils.alva_log('cpv_generator', f"{CPV}Appending CPVs to Harmonizer: {RESET}{[(CPV.channel, CPV.parameter_name, CPV.value) for CPV in CPVs]}")
            print_end_update("Returned CPVs to Harmonizer")
            return
        
        batch_send(self.context.scene, CPVs)
        print_end_update("Sent in Batch, Updating Others Now")
        UpdateOtherSelections(self).execute()


def print_end_update(reason):
    if DEBUG(): spy.utils.alva_log('cpv_generator', f"{CPV}########################################################\n# CPV Update {RED}ENDING{CPV} per {RESET}{reason}{CPV}\n########################################################\n")


def test_cpv_generator(SENSITIVITY): # Return True for fail, False for pass
    return False
