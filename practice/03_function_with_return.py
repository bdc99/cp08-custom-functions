# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

###########################
# START READING HERE
###########################

'''
    return values instantly end your function.
    They send back any variable back to where it was called.
    So if you want to store the returned variable, do something like:
        stored_variable = function_name("argument")

    functions can only return one variable. If you want to return many variables, put it in a list, tuple, dictionary, etc.

'''

# Write a function called simple_function_4 with a parameter called "text_message".
# but, instead of printing out "This is your message: " with the text_message appended, return that value.


# call simple_function_4. Store the value it returns in a variable, then print out that variable.



# call simple_function_4, but print out the returned variable directly (e.g. don't store the returned variable in a new variable):
