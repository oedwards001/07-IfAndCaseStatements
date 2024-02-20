txt = "The quick brown fox jumps over the lazy dog."

##############################################################################
# Done: 1. (2 pts)
#
#   Write a function called is_positive() that takes one parameter:
#     - number (float)
#   that returns True if the number given is either 0 or positive and returns
#   False if the number given is negative.
#
#   Your solution should use an if statement and should return the actual
#   values True or False (not just strings that say "True" or "False")
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def is_positive(number):
    if number == 0 or number > 0:
        return True
    else: 
        return False


###############################################################################
# Done: 2. (2 pts)
#
#   Write a function called contains() that takes two parameters:
#     - str (string)
#     - substr (string)
#   and checks if the substring *substr* is contained within the string *str*
#
#   The function should return the value True if the substring is within the
#   string and False if it is not within the string.
#
#   You should use an if statement in your solution.
#
#   You can test your function by calling it using the string I have provided
#   at the top of this file or by creating your own strings to use.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
str = txt
substr = "The quick brown fox"

def contains(str, substr):
    if substr in str:
        return True
    else:
        return False


###############################################################################
# Dones: 3. (3 pts)
#
#   Write a function called display_rating() that takes one parameter:
#     - rating (float)
#   that displays a short description for each rating that one might get on a
#   review for something like a product or a service.
#
#   For example, if the function gets a 4.8 it should print something like:
#
#       "Contratulations! You received a score of 4.8!"
#
#   or if it gets a rating of 1.2 it would print something like:
#
#       "You could use some improvement. You received a score of 1.2."
#
#   You should have a different message for each of these ranges of ratings:
#     - less than or equal to 5 and greater than or equal to 4
#     - less than 4 and greater than or equal to 3
#     - less than 3 and greater than or equal to 2
#     - less than 2 and greater than or equal to 1
#
#   If it receives anything outside those ranges, it should print:
#
#       "Invalid score given."
#
#   You can test this function by calling it with various ratings.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def display_rating(rating):

    if rating <= 5 and rating >= 4:
        print(f"Congratulations! You received a score of {rating}!")
    elif rating < 4 and rating >= 3:
        print(f"Your product was close to excellent. You received a score of {rating}.")
    elif rating < 3 and rating >= 2:
        print(f"Pretty good, but this item needs some improvement.  You received a score of {rating}.")
    elif rating < 2 and rating >= 1:
        print(f"This thing is very poorly designed, try again. You received a score of {rating}.")
    else:
        print("Invalid score given.")
        
display_rating(3.7)