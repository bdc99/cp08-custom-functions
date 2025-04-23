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

# 1. MATH FUNCTION PRACTICE
# write a function that accepts 2 numbers, then divides
# the first by the second and multiplies it by 100
# don't worry about cases where you'd divide zero.
# just ignore that possibility. this is just simple practice.
# call the function and print the result

def math_function(number_1 = 1, number_2 = 2):
    result = (number_1 / number_2) * 100
    return result


input_1 = input("Enter first: ")
input_2 = input("Enter second: ")
stored_result = math_function(input_1, input_2)
print(stored_result)