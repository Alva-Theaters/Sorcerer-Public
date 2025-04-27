# SPDX-FileCopyrightText: 2025 Alva Theaters
#
# SPDX-License-Identifier: GPL-3.0-or-later

import bpy

import shlex
from pathlib import Path
import time

class Parser:
    '''
    Problem: Writing code for Orb is long, boring, and tedious. It used to be a ton of 
    little helper functions. You would have to sort through a dozen interdependent helper 
    functions to figure out what any single orb button did. It worked, but wasn't easy to
    write or read.

    Solution: Now we've developed an innocent little Domain Specific Language (DSL) that
    makes writing Orb commands stupidly and painfully simple. With this, it could not 
    possibly be any simpler or it would be dead.

    Just write what the console should do in a txt file in plain English and it does it.

    This script is the boring backend. Each console has its own folder full of the txt file 
    scripts. This will eventually be implemented for the extendables API, but they can just 
    use regular Python until then.
    '''
    def __init__(self, Console):
        self.Console = Console


    def execute(self, console_name, script_name, **kwargs):
        filepath = self.find_filepath(console_name, script_name)
        dsl_text = self.load_text_from_file(filepath)
        logic = self.parse_macro_dsl(dsl_text, **kwargs) 
        yield from self.execute_logic(logic)

    def find_filepath(self, console_name, script_name):
        """
        Returns the full path to a script file given a console name (folder)
        and script name (without .txt). Assumes the folder is in the same dir
        as this script.
        """
        base_dir = Path(__file__).parent
        filepath = base_dir / console_name / f"{script_name}.txt"
        return filepath

    def load_text_from_file(self, filepath):
        with open(filepath, 'r') as f:
            dsl_text = f.read()
        return dsl_text

    def parse_macro_dsl(self, dsl_text, **kwargs):
        """
        Parse a custom DSL for macros into a list of (command, args, comment) tuples.
        Supports both string substitution and direct object injection (like raw tokens).
        """
        logic = []
        for line in dsl_text.strip().splitlines():
            code, *comment = line.split('#', 1)
            code = code.strip()
            if not code:
                continue

            comment = comment[0].strip() if comment else ""
            parts = shlex.split(code)
            if not parts:
                continue

            command = parts[0]
            args = " ".join(parts[1:])

            # Special handling: allow injecting full objects directly
            if command == "raw" and args in kwargs:
                arg_value = kwargs[args]
            else:
                try:
                    args_formatted = args.format(**kwargs)
                except KeyError as e:
                    raise ValueError(f"Missing value for DSL placeholder: {e}")
                arg_value = self.parse_args(command, args_formatted)

            logic.append((command, arg_value, comment))
        return logic

    def parse_args(self, command, args):
        """
        Parses args based on command type.
        Some commands like 'key', 'softkey' expect a list,
        others like 'key_up', 'softkey_down' expect a single value.
        """
        # Commands that expect a single string, not a list
        single_arg_commands = {"key_up", "key_down", "softkey", "softkey_down", "enter"}

        if command in ("cmd", "raw"):
            return args  # leave as-is (string or object)

        # Convert to list if needed
        arg_list = [arg.strip() for arg in args.replace(",", " ").split()]

        # Handle numeric string → list of digits
        converted = []
        for item in arg_list:
            if item.isdigit():
                converted.extend(list(item))
            else:
                converted.append(item)

        # Return a single string if only one item and command expects it
        if command in single_arg_commands and len(converted) == 1:
            return converted[0]

        return converted

    def execute_logic(self, logic):
        for funcname, item_list, report in logic:
            method = getattr(self.Console, funcname)
            yield method(item_list), report
            time.sleep(bpy.context.scene.orb_chill_time)