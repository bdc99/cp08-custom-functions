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
    you can give functions arguments. To do this,
    define a parameter after the function name when defining the function.

    Parameters take on the value of the argument given to them.

'''

# Write a function called simple_function_2 with a parameter called "text_message".
# Then inside the function, print out that text with "This is your message: " before the text passed as an argument


# call the function a couple of times:


# What happens if you don't provide an argument?



# Make a new function, called simple_function_3 that does the same thing,
# but add a default value of "this is the default" for the parameter text_message.
