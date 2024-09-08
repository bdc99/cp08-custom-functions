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
    A key concept related to functions is called "Scope"
    
    Scope in Python determines where a variable can be accessed or modified in your code.
    Essentially, if a variable is defined inside a function, it's only available within that function (local scope);
    if it's defined outside the function, it can be accessed anywhere in the file (global scope).
    
    Understanding scope helps prevent conflicts between variables and makes your code easier to manage.

    local variable: defined inside of a function

    global variable: defined outside of a function.

'''

# you are given this function:

def my_function():
    local_variable = "I am local to my_function"
    print(local_variable)

my_function()


# try to print out local_variable outside the function:
#print(local_variable) # This will cause an error if it is run.




