# print("Beginning of file")

# # if = "hello"

# [1, 2, 3][100]
    
# print("end of file")


# [1, 2, 3, 4, 5, 6]
# position = 1

# EAFP vs LBYL
# Easier to Ask for Forgiveness than Permission VS Look Before You Leap

# import logging

# try:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     result = num1 / num2
#     [1, 2, 3][8000]
# except ZeroDivisionError as e:
#     print(f"Cannot divide by zero: {e}")
# except ValueError as e:
#     print(f"num1 and num2 must be integers: {e}")
# except Exception as e:
#     print(f"Ooops! Something went wrong: {e}")
# else:
#     print(f"The result is {result}")


# Ask the user for their age, and tell them their birth year
# if they enter a non-integer, or they enter a negative number, print "Invalid age" and
# keep asking them until they enter a valid age and then show their birth year



# Quiz Score Tracker

# Write a program that keeps asking a user to enter their quiz scores (out of 100).

# Rules:
# The user can enter multiple scores, one at a time.
# If the user enters:
# A non-integer → print "Invalid score" and ask again
# A number less than 0 or greater than 100 → print "Score must be between 0 and 100" and ask again
# Keep accepting scores until the user enters -1 (this means they are done)
# After the user finishes:
# Print the average score
# Print the highest score entered
# 💻 Sample Execution
# Enter score: 80
# Enter score: 95
# Enter score: hello
# Invalid score
# Enter score: 120
# Score must be between 0 and 100
# Enter score: 70
# Enter score: -1
# ✅ Expected Output
# Average score: 81.67
# Highest score: 95
# 📝 Notes:
# Assume at least one valid score will be entered before -1
# Average should be shown with 2 decimal places


# ATM Withdrawal Checker

# Write a program that asks the user how much money they want to withdraw from an ATM.

# Requirements:
# The user must enter a number.
# If the user enters:
# A non-number → print "Invalid amount"
# A negative number or zero → print "Invalid amount"
# An amount greater than ₦50,000 → print "Exceeds withdrawal limit"
# Keep asking the user until they enter a valid amount.

# Once a valid amount is entered, print:

# Withdrawal of ₦<amount> successful
# 💻 Sample Execution
# Enter amount to withdraw: hello
# Invalid amount

# Enter amount to withdraw: -2000
# Invalid amount

# Enter amount to withdraw: 100000
# Exceeds withdrawal limit

# Enter amount to withdraw: 20000
# Withdrawal of ₦20000 successful


# --------------------------------CUSTOM EXCEPTIONS--------------------------------

# Ask the user for their age, and tell them their birth year
# if they enter a non-integer, or they enter a negative number, print "Invalid age" and
# keep asking them until they enter a valid age and then show their birth year

# from datetime import datetime

# # class InvalidAgeError(Exception):
# #     pass

# class InvalidAgeError(Exception):
#     def __init__(self, age, *args):
#         super().__init__(*args)
#         self.age = age


# while True:

#     try:
#         age = int(input("How old are you now?: "))
#         if age < 0:
#             raise InvalidAgeError(age, "Invalid age entered: Age cannot be negative")
#     except ValueError as e:
#         print(f"Invalid age: {e}")
#         continue
#     except InvalidAgeError as e:
#         print(e)
#         print(e.age)
#     else:
#         current_year = datetime.now().year
#         birth_year = current_year - age
#         print(f"You were born in {birth_year}.")
#         break


# --------------------------------CUSTOM EXCEPTIONS--------------------------------


def main():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 / num2
        # [1, 2, 3][8000]
    except ZeroDivisionError as e:
        print(f"Cannot divide by zero: {e}")
    except ValueError as e:
        print(f"num1 and num2 must be integers: {e}")
    except Exception as e:
        print(f"Ooops! Something went wrong: {e}")
    else:
        print(f"The result is {result}")
    finally:
        print("This block will always run")


try:
    main()
except KeyboardInterrupt:
    print("Exiting program")