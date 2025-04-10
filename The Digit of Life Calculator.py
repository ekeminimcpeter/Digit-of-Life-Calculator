# Author: Ekemini Peter
# Date: 26/12/2024
# Revision: 0
# Description: Original implementation of digit of life calculator
# Scope:
#   Ask the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY
#   Outputs the Digit of Life for the date
###############################################################################################

# Compute digit of life
def digit_of_life(user_birthday):

    # Initialise a variable to hold the sum of user birthday
    birthday_sum = 0
    if user_birthday.isdigit(): # check for validity of user input
        end_loop = False        # initial condition to start continuous loopinp
        while not end_loop:
            for elem in user_birthday:
                birthday_sum += int(elem)
            if len(str(birthday_sum)) == 1:
                print("Your digit of life is:", birthday_sum)
                end_loop = True # condition to end loop
            else:
                user_birthday = str(birthday_sum)
                birthday_sum = 0 
    else:
        print("Error: please enter birthday in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY!")

# Ask the user for his/her birthday
user_birthday = input("What is your birthday(in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY): ")

# Output digit of life
digit_of_life(user_birthday)
