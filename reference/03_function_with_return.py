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

# ==============================
# CUSTOM FUNCTIONS - WITH RETURN
# ==============================

'''
OVERVIEW
--------

return values instantly end your function.
They send back any variable back to where it was called.

So if you want to store the returned variable, do something like:
    stored_variable = function_name("argument")

functions can only return one variable.
If you want to return many variables, put it in a list, tuple, dictionary, etc.

'''

# 1. FUNCTION WITH RETURN
# Write a function called simple_function_5 with a parameter called
# "text_message". But, instead of printing out
# "This is your message: <text message>" return the string.
# call the function and print out the returned value.

def simple_function_5(text_message):
    return f"This is your message: {text_message}"

returned_value_1 = simple_function_5("First try")
print(returned_value_1)


# 2. FUNCTION WITH MULTIPLE RETURNS
# Write a function called simple_function_6 with a parameter called
# "text_message". If text_message is equal to "Dumb" then return
# "That is mean!". Otherwise, just return text_message.
# Call the function and print out the returned value.

def simple_function_6(text_message, another):
    if text_message == "Dumb":
        return "That is mean!"
    
    return f"This is your message: {text_message}"

returned_value_2 = simple_function_6("Dumb")
print(returned_value_2)

