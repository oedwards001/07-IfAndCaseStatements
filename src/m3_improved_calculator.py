# GOT HElP FROM JOSH, SOFTWARE ENGINEER STUDENT

import math

def add(first_param, second_param):
    addition = first_param + second_param
    return addition    
  
def subtract(first_param, second_param):
    subtraction = first_param - second_param
    return subtraction

def multiply(first_param, second_param):
    multiplication = first_param*second_param
    return multiplication

def divide(first_param, second_param):
    division = first_param / second_param
    return division

def power(first_param, second_param):
    powerraise = math.pow(first_param, second_param)
    return powerraise
###############################################################################
# Done: 1. (4 pts)
#
#   In this module, we will improve upon the calculator that we built in the
#   Session 5 coding exercises.
#
#   First, you will need to grab the functions that you wrote for each of the
#   four main operations:
#     - add
#     - subtract
#     - multiply
#     - divide
#
#   You can simply copy and paste them into this file at the top (above this
#   _TODO_)
#
#   For this _TODO_, we will be rewriting our main() function.
#
#   First, copy your main() function from Session 5 m3 todo #2 and rename it
#   to if_calc().
#
#   Next, make these modifications
#     1. Add another prompt for the user asking which operation they want to
#        do. Make sure to show the user this key in the prompt.
#           (+) Add
#           (-) Subtract
#           (*) Multiply
#           (/) Division
#        The user should then enter one of the operators to indicate which
#        operation they want to do. Make sure you save this to a variable.
#
#     2. Now, using if statements, check which operator the user put and only
#        do the calculation that the user specified instead of all of them. If
#        the user, put something other than one of the operators, print:
#           "Invalid Operation!"
#
#   Your solution should still function just like it did in Session 5 (except
#   for the changes outlined above)   
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def if_calc():

    print("Hello, how are you?")

    number1 = input("Please enter your first number: ") 
    number1 = int(number1) 
    
    number2 = input("Please enter your second number: ")
    number2 = int(number2)
    
    addition = add(first_param=number1, second_param=number2) 
    print(f"Add: {addition}") 

    subtraction = subtract(first_param=number1, second_param=number2)
    print (f"Subtract: {subtraction}")

    multiplication = multiply(first_param=number1, second_param=number2)
    print (f"Multiply: {multiplication}")

    division = divide(first_param=number1, second_param=number2)
    print (f"Divide: {division}")

    powerraise = power(first_param=number1, second_param=number2)
    print (f"Power: {powerraise}")

    print("(+) Add")
    print("(-) Subtract")
    print("(*) Multiply")
    print("(/) Division")
    chosen_operation = input("Which operation do you want to do? ")

    if chosen_operation == "add":
        print(addition)
    elif chosen_operation == "subtract":
        print(subtraction)
    elif chosen_operation == "multiply":
        print(multiplication)
    elif chosen_operation == "division":
        print(division)
    else:
        print("Invalid Operation!")


    print("Goodbye!")

    
###############################################################################
# Done: 2. (4 pts)
#
#   Now, do the same thing that you did in _TODO_ 1, but this time, use case
#   statements in your solution instead of if statements.
#
#   This time rename your function to case_calc(). Also, you do *not* need to
#   re-copy your operation functions. You can simply use them again.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def case_calc():

    print("Hello, how are you?")

    number1 = input("Please enter your first number: ") 
    number1 = int(number1) 
    
    number2 = input("Please enter your second number: ")
    number2 = int(number2)
    
    addition = add(first_param=number1, second_param=number2) 
    print(f"Add: {addition}") 

    subtraction = subtract(first_param=number1, second_param=number2)
    print (f"Subtract: {subtraction}")

    multiplication = multiply(first_param=number1, second_param=number2)
    print (f"Multiply: {multiplication}")

    division = divide(first_param=number1, second_param=number2)
    print (f"Divide: {division}")

    powerraise = power(first_param=number1, second_param=number2)
    print (f"Power: {powerraise}")

    print("(+) Add")
    print("(-) Subtract")
    print("(*) Multiply")
    print("(/) Division")
    
    command = input("Which operation do you want to do? ")

    match command:

        case "add":
            print(addition)
        case "subtract":
            print(subtraction)
        case "multiply":
            print(multiplication)
        case "division":
            print(division)
        case other:
            print("Invalid Operation!")


    print("Goodbye!")


