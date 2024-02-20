###############################################################################
# Done: 1. (3 pts)
#
#   Write a function called color_picker() that prints out a message to a user.
#
#   This function should do the following:
#     1. Prompt the user to enter the name of a color.
#     2. Using case statements, if it matches the color that they picked, it should print out a success message like so:
#           "Success! You picked red."
#        Do NOT use f-strings here. Just use regular strings and use the case statement to pick which string to print.
#     3. You should have a case for at least 5 colors of your choosing.
#     3. If the user picks a color that you do not have a case for, it should print:
#           "Unknown Color!"
#
#   Make sure you call your function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def color_picker():

    command = input("Please enter the name of a color: ")

    match command:

        case "yellow":
            print("Success! You picked yellow!")
        case "turquoise":
            print("Success! You picked turquoise!")
        case "blue":
            print("Success! You picked blue!")
        case "red":
            print("Success! You picked red!")
        case "orange":
            print("Success! You picked orange!")

        case other:
            print("Unknown Color!")
        
color_picker()


###############################################################################
# Done: 2. (3 pts)
#
#   Write a function called grade() that tells a student what letter grade they
#   got on an assignment based on the percentage they indicate.
#
#   This function should do the following:
#     1. Prompt the user to enter a percentage. They should enter the
#        percentage as a decimal (so an 85% should be entered as 0.85)
#     2. Using case statements, check which range the percentage is in and print a statement telling the user what grade they got on the assignment. It should look something like:
#           "You received a(n) A."
#     3. Your ranges should match a standard grading scale where greater than or equal to 90% is an A, etc.
#     4. If the user enters an invalid percentage, the function should print:
#           "Invalid Score!"
#
#   Make sure you call your function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def grade():

    command = float(input("Please enter your percentage grade as a decimal: "))

    match command:

        case _ if command >= 0.90:
            print("You received a(n) A.")
        
        case _ if command >= 0.80:
            print("You received a(n) B.")
        
        case _ if command >= 0.70:
            print("You received a(n) c.")

        case _ if command >= 0.60:
            print("You received a(n) D.")
        
        case _ if command >= 0.50:
            print("You received a(n) F.")

        case other:
            print("Invalid Score!")
grade()
