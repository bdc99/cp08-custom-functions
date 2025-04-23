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


# 2. FUNCTION, WITH PARAMETERS, NO RETURN
# Write a function that accepts a parameter with your name. Insert your name
# into the function and have it print "Welcome to class, <name>!"
def function_1(name):
    print(f"welcome to class, {name}!")

my_name = "ben"
function_1 = my_name



# 3. FUNCTION, WITH PARAMETERS & RETURN
# Write a function that accepts a parameter with your name. 
# keep the function printing "Welcome to class, <name>!" but also return the
# first letter of your name.
# Then outside of your function, print out "This is the first letter of my name: x"

def function_3(name):
    print(f"welcome to class, {name}!")

    return name(0)

my_name = "Ben"
first_letter = function_3(my_name)

print(f"the first letter of my name is {first_letter}")
