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

# ==================================
# CUSTOM FUNCTIONS - WITH PARAMETERS
# ==================================

'''
OVERVIEW
--------

You can provide a function with inputs.

The placeholders for these inputs are called "parameters"

The actual values that get put in the the parameters are called "arguments"

'''

# 1. WRITE A FUNCTION WITH PARAMETERS
# Write a function called simple_function_2 with a parameter
# called "text_message".
# Then inside the function, print out that text with
# "This is your message: <text_message>"
# Afterwards, call the function 2 times.
def simple_function_2(text_message):
    print(f"this is your message: {text_message}")

simple_function_2("I am a person!")
simple_function_2("I am a dog!")
    

# 2. INCORRECTLY CALLING A FUNCTION
# What happens if you don't provide an argument when the
# function is expecting one?
# simple_function_2() # this will throw an error


# 3. ADDING DEFAULT VALUES TO FUNCTIONS 
# Make a new function, called simple_function_3 that does the same thing
# as simple_function_2, but add a default value of "this is the default"
# for the parameter text_message.
def simple_function_3(text_message = "this is the default"):
    print(f"this is your message: {text_message}")

clear_screen()
simple_function_3("I am a person!")
simple_function_3()


'''
Note, that if you add a default value to a parameter, all parameters after
if in the function definition must also have default values.
'''

# 4. FUNCTION WITH 2 PARAMETERS, 1 OF THEM DEFAULT
# Make a new function, called simple_function_4 that has 2 parameters:
# text_message_1 and text_message_2. Make it print out the concatenation
# of the two messages.
# For the sake of practice, make text_message_1 have a default value,
# and text_message_2 not have a default try to run it and notice the error
# you get. 

def simple_function_4(text_message_1 = "default #1", text_message_2):
    print(f"this is your concetated message: {text_message_1} {text_message_2}")

clear_screen()
simple_function_4("first message", "A really great 2nd message")
simple_function_4("first message")