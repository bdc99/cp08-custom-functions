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

# ===========================================
# CUSTOM FUNCTIONS - NO PARAMETERS, NO RETURN
# ===========================================

'''
OVERVIEW
--------

A function is just stored code that you can reuse!

Define a function with def
Then call it afterwards by writing the function name with parentheses

'''


# 1. SIMPLE FUNCTION:
# write a function called simple_function
# it should just print out "Wow this is a simple function" on one line
# and "Wow this is another line" after that.
# then call the function 3 times
def simple_function():
    print("wow this is a simple function")

simple_function()
simple_function()
simple_function()