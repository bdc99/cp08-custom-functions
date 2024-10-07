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

# ==============
# SCOPE - GLOBAL
# ==============

'''
OVERVIEW
--------

A key concept related to functions is called "Scope"

Scope in Python determines where a variable can be accessed or
modified in your code.

GLOBAL SCOPE
------------
Variables defined outside of a function.

If it's defined outside the function, it can be accessed anywhere in the
file (global scope), including inside functions.

Understanding scope helps prevent conflicts between variables and makes your
code easier to manage.


'''

# 1. ACCESSING GLOBAL VARIABLES
# given this variable and function:
global_variable = "I am global"

def access_global_variable():
    print(global_variable)

# try running the function access_global_variable:


# try printing global_variable directly.


'''
SHOULD YOU USE GLOBAL VARIABLES IN FUNCTIONS?
---------------------------------------------
Even though you can do this, it is HIGHLY RECOMMENDED
That you do not. It tends to create bugs in the long run.

You ideally ideally want functions to be self-contained.

If they are referencing variables outside the function, 
any time that variable is changed, it will alter how the function
runs in potentially unpredictable ways.

It is generally better to just pass in global variables as arguments:
'''

def better_version(local_variable):
    print(local_variable)

