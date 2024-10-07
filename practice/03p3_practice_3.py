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

# =======================================
# CUSTOM FUNCTIONS - REFACTORING PRACTICE
# =======================================

'''
OVERVIEW
--------

One primary benefit of writing functions is to decrease repeating similar code
over and over.

Use practice file to "refactor" existing code to make it more succinct and 
efficient. "Refactoring" just refers to improving code without altering its
actual functionality.

'''

'''
SITUATION
---------

I'm giving you data on 3 students: their GPA, their ACT score, and if they got FAFSA approved.

I want to calculate if BYU will give them a scholarship. This occurs in 2 situations:
    - Their GPA is at least 3.0 and their ACT is at least 25, OR
    - They are FAFSA approved

Note that this is made up and simplified, its just for practice.

The code below is already written for you. Look after this code for your task instructions.
'''
# Student 1 data: GPA, ACT score, FAFSA approved
student1_gpa = 3.5
student1_act = 28
student1_fafsa_approved = False

if (student1_gpa >= 3.0 and student1_act >= 25) or student1_fafsa_approved:
    print("Student 1 qualifies for a scholarship.")
else:
    print("Student 1 does not qualify for a scholarship.")

# Student 2 data: GPA, ACT score, FAFSA approved
student2_gpa = 3.2
student2_act = 23
student2_fafsa_approved = False 
if (student2_gpa >= 3.0 and student2_act >= 25) or student2_fafsa_approved:
    print("Student 2 qualifies for a scholarship.")
else:
    print("Student 2 does not qualify for a scholarship.")

# Student 3 data: GPA, ACT score, FAFSA approved
student3_gpa = 2.8
student3_act = 30
student3_fafsa_approved = True
if (student3_gpa >= 3.0 and student3_act >= 25) or student3_fafsa_approved:
    print("Student 3 qualifies for a scholarship.")
else:
    print("Student 3 does not qualify for a scholarship.")

# 1. YOUR TASK:
# Rewrite the code above by making a function so you aren't repeating the same
# if statements over and over.
# Call your function check_scholarship that accepts 3 parameters: GPA, ACT,
# and FAFSA_approved. It should return a statement on if a student qualified
# or not for a scholarship. Then call the function 3 times and print out
# whether each of the below 3 students should get a scholarship.

# Data for each student
student1_gpa = 3.5
student1_act = 28
student1_fafsa_approved = True

student2_gpa = 3.2
student2_act = 23
student2_fafsa_approved = False

student3_gpa = 2.8
student3_act = 30
student3_fafsa_approved = False
