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
The whole point of writing functions is to decrease repetition,
and create code that has a specific purpose that can be reused multiple times.
'''


# PRACTICE
'''
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

'''
YOUR TASK:

After this code, try and rewrite it using a function that would make it so you aren't repeating the same if statements over and over.
Use a function called check_scholarship that accepts 3 parameters: GPA, ACT, and FAFSA_approved.
It should return a statement on if a student qualified or not for a scholarship.

'''

##################
# REWRITE THE BETTER CODE HERE:
#################

# Defining a function to determine scholarship eligibility using individual parameters
def check_scholarship(gpa, act, fafsa_approved):
    if (gpa >= 3.0 and act >= 25) or fafsa_approved:
        return "Qualifies for a scholarship."
    else:
        return "Does not qualify for a scholarship."

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

# Checking scholarship eligibility for each student
print(f"Student 1: {check_scholarship(student1_gpa, student1_act, student1_fafsa_approved)}")
print(f"Student 2: {check_scholarship(student2_gpa, student2_act, student2_fafsa_approved)}")
print(f"Student 3: {check_scholarship(student3_gpa, student3_act, student3_fafsa_approved)}")
