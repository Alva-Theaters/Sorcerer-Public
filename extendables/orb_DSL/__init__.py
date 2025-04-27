# SPDX-FileCopyrightText: 2025 Alva Theaters
#
# SPDX-License-Identifier: GPL-3.0-or-later


'''
This is a simple scripting language used to control Orb operators. Each script is a plain text file where each line represents 
one action. Lines consist of a command followed by arguments, and optionally a comment after a # symbol. The parser reads these 
scripts line by line and sends the corresponding actions to the console.

Commands include:

- key: simulates pressing one or more keys. You can separate multiple keys with commas or spaces.
- key_up / key_down: simulates releasing or pressing down a single key.
- softkey / softkey_down: selects or presses down a numbered softkey.
- cmd: sends a command string to the console. These strings can include placeholders in {braces} which will be filled in using 
       values passed to the parser.
- raw: inserts a full object (usually a list of strings) passed to the parser. This is typically used to type a series of lines.

You can include placeholders in command strings, like {macro_number}, and provide the value when calling the parser. 
For example, cmd "Delete Macro {macro_number}" would become cmd "Delete Macro 5" if macro_number=5 is passed in.

Comments can be added to any line using #. They are ignored by the parser and meant to describe what each line does.

Example:

key live                                         # Going live
key macro, macro                                 # Entering macro mode
cmd "Delete Macro {macro_number} Enter Enter"    # Deleting macro
cmd "{macro_number} Enter"                       # Recreating macro
key_up macro                                     # Resetting macro key
softkey 6                                        # Edit softkey
raw tokens                                       # Typing macro lines
softkey_down 6                                   # Typing done
key live                                         # Back to live

Blank lines and comment-only lines are ignored. The goal of this DSL is to make console scripting easy to read and write with 
minimal boilerplate.

For context, Orb operators have a ton of abstraction. That's because 

       1. They run on a generator, for early termination via ESC key 
       2. They run on multiple console types based on settings
       3. They use global launch, exit, and cancel sequences in addition to local logic
       4. They can also be created implicitly via functions in spy.types.SequencerStrip classes

This means that there is no Orb operator class that just has all its stuff in one place. The DSL is typically for reusable macros.
Use the execute method in the spy.types.Orb for the higher level local Pythonic logic.
'''