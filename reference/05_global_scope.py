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
def access_global_variable():
    print(global_variable)


global_variable = "I am global"

# try running the function access_global_variable:
access_global_variable()

# try printing global_variable directly.

print(global_variable)

'''
Key point:
    Even though you can do this, it is HIGHLY RECOMMENDED
    That you do not. It tends to create bugs in the long run.
    
    You ideally ideally want functions to be self-contained.
    
    If they are referencing variables outside the function, 
    any time that variable is changed, it will alter how the function
    runs in potentially unpredictable ways.
'''