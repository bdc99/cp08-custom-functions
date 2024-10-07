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

# ====================================================
# SCOPE - ALTERING A GLOBAL VARIABLE INSIDE A FUNCTION
# ====================================================

'''
OVERVIEW
--------

If you want to change the value of a global variable in a function (not just
reference the value of it) then you need to use the keyword "global" before
referencing the variable name.

Again, I usually don't recommend doing this, but this is good to know.

'''
# 1. ALTERING A GLOBAL VARIABLE INSIDE A FUNCTION:
# you are given this function:
def local_with_same_name():
    global example_variable
    example_variable = "This is a new value!"
    print(example_variable)

example_variable = "I am global"

# try calling local_with_same_name
# try to predict, what will print out when you run it?
local_with_same_name()

# now print out example_variable. Will its value change?
print(example_variable)
