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

# =======================
# *ARGS and **KWARGS
# =======================

'''
OVERVIEW
--------
Sometimes you may want to pass in a variable number of arguments into a
function (for example, print() lets you pass in as many thigns as you want
separated by commas).

To allow for this, you can add * to a parameter, which means it will be
interpreting any number of arguments you give it as going into that parameter
as a list of arguments. This is referred to as *args

You can do the same thing with key-value pairs, by using ** which is referred
to as **kwargs
'''


# 1. USING *ARGS
# Write a function called sum_numbers takes any number of numbers and returns
# their sum. Use *args to handle an unknown number of arguments.
# (you don't have to call it args, but you do need the *)
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(10, 2, 3, 17)) 

# 2. USING **KWARGS
# Write a function called send_email. It always requires a "to" parameter.
# However, all the other info is sometimes optional (e.g. subject, body, sender
# importantance, etc.). Use **kwargs to allow the caller of the function to
# insert whatever info they want to the email. Use kwargs.get to check if specific
# info is there and return all the email info in a combined string.

def send_email(to, **kwargs):
    subject = kwargs.get('subject', 'No Subject')
    body = kwargs.get('body', 'No Body Content')
    sender = kwargs.get('sender', 'noreply@example.com')
    important = kwargs.get('important', False)

    email_info = f"To: {to}\nFrom: {sender}\nSubject: {subject}\nBody: {body}\nImportant: {important}"
    return email_info

# Sending an email with only the required parameter
send_email('recipient@example.com')

# Sending an email with additional optional parameters
send_email('recipient@example.com', subject="Meeting Reminder", body="Don't forget our meeting tomorrow!", important=True)