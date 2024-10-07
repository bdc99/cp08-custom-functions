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

# =============
# SCOPE - LOCAL
# =============

'''
OVERVIEW
--------

A key concept related to functions is called "Scope"

Scope in Python determines where a variable can be accessed or
modified in your code.

LOCAL SCOPE
-----------
Variables defined inside of a function.

If a variable is defined inside a function, it's only available within that function (local scope);

Understanding scope helps prevent conflicts between variables and makes your
code easier to manage.

'''

# 1. TRYING TO ACCESS LOCAL SCOPE VARIABLES
# Given this function:

def my_function():
    local_variable = "I am local to my_function"
    print(local_variable)

my_function()

# try to print out local_variable outside the function:





