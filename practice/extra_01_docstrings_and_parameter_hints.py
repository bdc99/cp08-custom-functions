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

# =========================
# DOCSTRINGS AND TYPE HINTS
# =========================

'''
OVERVIEW
--------
Docstrings are just comments placed in the very first line of a function to
explain what the function does.

Type hints are when you note what data type a parameter is expected to receive
and also what data type a function is expected to return. They can be useful,
but just remember that python is dynamically typed, so it doesn't force the 
data types to align with the type hints.
'''

def addition_message(num_1, num_2):
    sum = num_1 + num_2
    return f"The sum of {num_1} and {num_2} is {sum}."

print(addition_message(10, 5))

# 1. ADD A DOCSTRING
# Inside of addition_message, write a comment using triple quotes """ or '''
# Then hover your mouse over where you call addition_message and notice how
# the comment appears.


# 2. ADD TYPE HINTS TO PARAMETERS
# Inside of addition_message, after each parameter add : followed by the
# data type that you are expecting. If you are expecting potentially multiple
# data types you can separate them with a |
# (assuming you are using python 3.10 or above)


# 3. ADD RETURN TYPE HINT
# Inside of addition_message, after the parentheses, but before the colon,
# add -> str to indicate that the funciton is intended to return a string.