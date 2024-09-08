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

def local_with_same_name():
    global example_variable
    example_variable = "I am local to local_with_same_name"
    print(example_variable)

example_variable = "I am global"

# try calling local_with_same_name
# try to predict, what will print out when you run it?


# now print out example_variable. Will its value change?


'''
Key point to remember:
    If you need to change the value of a global variable, you can do it by using the global keyword
    inside of a function.

    I recommend you don't do this.

'''