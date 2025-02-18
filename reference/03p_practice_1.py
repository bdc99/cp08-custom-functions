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

# ===========================
# CUSTOM FUNCTIONS - PRACTICE
# ===========================

# 1. FUNCTION, NO PARAMETERS OR RETURN
# Write a function that prints out
# "Welcome to class!" and then call the function

def function_1():
    print("Welcome to class")

function_1()

# 2. FUNCTION, WITH PARAMETERS, NO RETURN
# Write a function that accepts a parameter with your name. Insert your name
# into the function and have it print "Welcome to class, <name>!"
        
def function_2(name):
    print(f"Welcome to class, {name}!")

example_name = "Jacob"
function_2(example_name)

# Version 2.1, if you wanted a default value:
def function_2_1(name = "Jacob"):
    print(f"Welcome to class, {name}!")

example_name_2 = "James"
function_2_1(example_name_2) # we can pass a variable
function_2_1()

# 3. FUNCTION, WITH PARAMETERS & RETURN
# Write a function that accepts a parameter with your name. 
# keep the function printing "Welcome to class, <name>!" but also return the
# first letter of your name.
# Then outside of your function, print out "This is the first letter of my name: x"

def function_3(name = "jacob"):
    print(f"Welcome to class, {name}!")
    first_letter = name[0]
    return(first_letter)

example_name_3 = "John"
print(f"This is the first letter of my name: {function_3(example_name_3)}") 

