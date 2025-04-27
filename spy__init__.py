'''
This is basically a copycat of Blender's bpy module.

Why is bpy? To open entry to devs without C++ Blender ovens. 
Why is bpy.types? Because modularization leads to less breakages. Best to keep type-specific logic localized.
Why is bpy.context? Because tons of finder functions are more likely to break.

Earlier versions of Sorcerer experienced a lot of the problems above, formerly solved by the Blender gods with bpy. 
So we solve the same problems with the crazy amazing solution that the Blender gods already figured out for us.
'''

from . import data  # For example, installed lighting consoles, not currently active lighting console. Only major changes.
from . import context  # For example, active, valid controllers currently in scene. Minor changes.
from . import types  # Extendables classes, like LightingConsole, SequencerStrip, Orb, LightingParameter, etc.
from . import utils  # Tools, both those that are dogfed and those only intended for end-user scripting.
