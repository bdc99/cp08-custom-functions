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

# ========================================
# SCOPE - CLARIFICATIONS ON VARIABLE NAMES
# ========================================

'''
OVERVIEW
--------

Even if a variable defined in a function has the same name as a 
global variable, it will still be a local variable.

'''

# 1. WILL example_variable CHANGE ITS VALUE?
# you are given this function:
def local_with_same_name():
    example_variable = "I am local to local_with_same_name"
    print(example_variable)

# and this global variable
example_variable = "I am global"

# try calling local_with_same_name
# try to predict: what will print out when you run it?
local_with_same_name()

# now print out example_variable. Will its value change?
print(example_variable)

'''
TIP
---

To avoid confusing yourself, try to not call local and global variables
the same thing.
'''