import os
import platform

def clear_screen():
    """
    Clears the terminal screen to make it easier to follow along with code.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# =======================
# IMPORTING LOCAL MODULES
# =======================

'''
OVERVIEW
--------
Often, for better organization, programmers will place some of their functions
in a separate .py file (called a module)

To do this, the .py file (module) needs to be in the same folder, or in the
system path (see the textbook for more details). The module also can't start
with numbers in the filename.

Typically, you would put all of your import statemetns at the very top of the 
.py file. That way, anything below can access them.

SYNTAX
------
You can import a whole module:

    import module_name

You can shorten the name of the module by creating an alias with "as":

    import module_name as mn

You can also import a specific function/variable from a module like this:

    from module_name import function_name

You can also import everything from a module doing this:

    from module_name import *
'''


# 1. IMPORT A LOCAL MODULE
# In this folder, I've included a module (a .py file) called "example_module"
# Take a look at it. Then, in this file, import the module and then call
# the multiply_2_numbers module and print the result.
import example_module

print(example_module.multiply_2_numbers(2,4))

# 2. GIVE A MODULE A NICKNAME
# Import example_module again, but rename it to "em". Then call
# multiply_2_numbers again and print the result.

import example_module as em
print(em.multiply_2_numbers(2,4))


# 3. IMPORT A SPECIFIC FUNCTION
# Use the "from x import x" syntax to specifically import multiply_2_numbers
# Call it again and print the result.
from example_module import multiply_2_numbers

print(multiply_2_numbers(2,4))

# 4. IMPORT EVERYTHING FROM A MODULE
# This is generally considered bad practice, but you can import everything
# from a module using the syntax "from x import *". 
# Import all the functions from exmaple_module, then run subtract_2_numbers
# and print the result.

from example_module import *
print(subtract_2_numbers(10,8))