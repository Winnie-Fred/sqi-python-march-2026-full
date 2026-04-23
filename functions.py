"""
A file to explain functions to Mr. Ope
"""

# DRY - Don't Repeat Yourself

# A strong password:
# Is at least 8 characters long.
# Contains both uppercase and lowercase characters.
# Contains at least one digit.
# Contains at least one special character (e.g., !@#$%^&*()).



# def is_strong_password(password):
#     has_at_least_8_chars = len(password) >= 8

#     has_upper = False
#     has_lower = False
#     has_digit = False
#     has_special_char = False

#     special_chars = "!@#$%^&*()"

#     for char in password:
#         if char.isupper():
#             has_upper = True
#         elif char.islower():
#             has_lower = True
#         elif char.isdigit():
#             has_digit = True
#         elif char in special_chars:
#             has_special_char = True

#     print(all([has_upper, has_lower, has_digit, has_special_char, has_at_least_8_chars]))

# is_strong_password("Passw0rd!")
# is_strong_password("p@$$W0rd!")
# is_strong_password("12345678")



# def greet():
#     print("Hello, and good morning! ☀️")


# greet()

# def greet_v2(name):
#     print(f"Hello, and good morning {name}! 👋")

# greet_v2("Ope")
# greet_v2("Dele")
# greet_v2("Winnie")
# greet_v2("Tobi")


# def square(num):
#     print(num ** 2)

# square(6)
# square(4)
# square(3)
# square(7)
# square(9)

# def add_two_nums(num1, num2):
#     print(num1 + num2)

# add_two_nums(8, 4)



# 1. Create a function called `sing` that takes in nothing and prints "I am singing"
# 2. Create a function called `person_sings` that takes in a string `name` and prints "{name} is singing"
# 3. Create a function called `perform_duet` that takes in 2 strings `person1` and `person2` and prints "{person1} and {person2} are singing"
# 4. Create a function called `perform_harmony` that takes in a list called `people` and prints out for each person
# `{person} is singing`
# e.g. if the list is ["Winnie", "Tobi", "Ope", "Dele"], the output of the function call is


# perform_harmony(["Winnie", "Tobi", "Ope", "Dele"])
# Winnie is singing
# Tobi is singing
# Ope is singing
# Dele is singing


# perform_harmony(["James", "Janet", "John"])
# James is singing
# Janet is singing
# John is singing



# print("Lorem ipsum dolor")  # 1

# def greet():
#     print("sit amet")  # 3, 6
#     print('Hello World!')  # 4, 7

# print('tempor incididunt ut labore')  # 2
# greet()
# print("consectetur adipiscing elit")  # 5
# greet()
# print("Nemo enim ipsam voluptatem")  # 8




# print("The sun rises in the east")  # 1


# def greet():
#     print("How's it going?")  # 2, 5, 7, 10
#     print("Stay curious, stay kind.")  # 3, 6, 8, 11


# greet()

# print("Midnight thoughts and coffee sips")  # 4
# greet()
# greet()
# print("Learning never exhausts the mind")  # 9
# greet()
# print("Wander often, wonder always")  # 12


# def add_two_numbers_print(first_num, second_num):
#     print(first_num + second_num)


# add_two_numbers_print(4, 7)


# upper_name = "James".upper()

# print(upper_name)

# def add_two_numbers_return(first_num, second_num):
#     return first_num + second_num



# result = add_two_numbers_return(5, 8)
# print(result)

# print(add_two_numbers_return(5, 8))



# def upper_and_lower(name):
#     return name.upper(), name.lower()

# # result = upper_and_lower("Kenneth")

# # print(result)

# upper, lower = upper_and_lower("Kenneth")

# print(upper)
# print(lower)


# my_list = [1, 2, 3]
# my_list.append(4)
# popped = my_list.pop(1)
# print(popped)

# print(my_list)

# def add_two_numbers_return(first_num, second_num):
#     print(first_num + second_num)


# add_two_numbers_return(5, 2)


# def add_two_numbers_return(first_num, second_num):
#     return (first_num + second_num)


# print(add_two_numbers_return(5, 2))

# sum_of_nums = add_two_numbers_return(2, 8)

# print(sum_of_nums)



# Write a function called `raise_to_power` that takes in `base` and `exponent` and returns base raised to the power of exponent

# Sample execution:
# print(raise_to_power(4, 3))
# 64

# result = raise_to_power(5, 2)
# print(result)
# 25

# def upper_and_lower(name: str):
#     return name.upper(), name.lower()


# print(upper_and_lower("James"))

# type hint or annotation


# def show_name_with_len(names_with_lens: list[tuple[str, int]]):
#     # for name, len in names_with_lens:
#     #     print(f"{name} -> {len}")

#     for item in names_with_lens:
#         name, len = item
#         print(f"{name} -> {len}")


# names_with_their_lens = [("James", 5), ("John", 4), ("Kenneth", 7)]
# show_name_with_len(names_with_their_lens)



# books: list[dict[str, str | int]] = [
#     {"title": "And then there were None", "year_published": 2022},
#     {"title": "The Silent Patient", "year_published": 2002},
#     {"title": "Things Fall Apart", "year_published": 1998},
#     {"title": "The Concubine", "year_published": 1902},
# ]




# 2. Write a function is_even(n) that returns True if n is even and False if n is odd.

# def is_even(n: int):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
    
# print(is_even(5))
# print(is_even(6))


# def is_even(n: int):
#     if n % 2 == 0:
#         return True
#     return False
    
# print(is_even(5))
# print(is_even(6))


# def is_even(n: int):
#     return n % 2 == 0
    
# print(is_even(5))
# print(is_even(6))


# 4. Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter.
# is_alliteration(‘Levelheaded llama’) —> True
# is_alliteration(‘Crazy Kangaroo’) –> False



# 1. Create a function called turn_to_upper(names) that takes in a list of names, and returns a list of names uppercased. After, print the result of the function.
# For example, if names is ["Winifred", "Wilfred", "Justin", "Augusta"], the result would be [ "WINIFRED", "WILFRED", "JUSTIN", "AUGUSTA"]


# ------------------------------------------ASSIGNMENT CORRECTION------------------------------------------------


# 2, 10, 3, 4, 14

# 2. Create a function called get_middle_name that accepts one paramter `name_dict` that takes in a dictionary with keys "first", "middle", and "last".
# The function should return only the middle name.
# For example, if name_dict is {"first": "Tola", "middle": "James", "last": "Akin"}, then the result would be "James". Another example is if name_dict is {"middle": "Chioma", "first": "Ada", "last": "Okeke"}, the result would be "Chioma".

# def get_middle_name(name_dict: dict[str, str]):
#     if "middle" in name_dict:
#         return name_dict["middle"]
#     return None

# Edge cases
# Happy path

# def get_middle_name(name_dict: dict[str, str]):
#     return name_dict.get("middle")


# print(get_middle_name({"first": "Tola", "middle": "James", "last": "Akin"}))
# print(get_middle_name({"middle": "Chioma", "first": "Ada", "last": "Okeke"}))
# print(get_middle_name({"first": "Ada", "last": "Okeke"}))
# print(get_middle_name({}))

# 10. Create a function called merge_lists that takes in two lists and returns one combined list without duplicates.
# For example, if list1 = [1, 2, 3] and list2 = [3, 4, 5], the result would be [1, 2, 3, 4, 5].

# def merge_lists(list1: list[int], list2: list[int]) -> list[int]:
#     # return list(set(list1 + list2))
#     return list(set([*list1, *list2]))


# print(merge_lists([1, 2, 3], [3, 4, 5]))


# list1 = [1, 2, 3]
# list2 = [3, 4, 5]

# [1, 2, 3, 3, 4, 5]


# flattened_list = [*list1, *list2]
# print(flattened_list)

# *args and **kwargs

# 3. Write a function is_prime(n) that returns True if n is a prime number and False otherwise.


# def is_prime(n):
#     if n <= 1:
#         return False

#     for i in range(2, int(n ** 1/2) + 1):
#         if n % i == 0:
#             return False

#     return True


# print(is_prime(9))


# 4. Using the is_prime(n) function from number 3, write a function that asks a user for an input n and returns all the prime numbers up to n.

# def list_primes(n):

#     pass


# print(list_primes(input("Enter the vakue of n: ")))


# def list_primes():
#     n = int(input("Enter the value of n: "))
#     primes_up_to_n = []
#     i = 0
#     while True:
        
#         if is_prime(i):
#             primes_up_to_n.append(i)

#         if i == n:
#             break

#         i += 1
#     return primes_up_to_n

# print(list_primes())


# 14. Write a function is_pangram(text) to check whether a string is a pangram or not. 
# Note: A pangram is a word or sentence that contains every letter of the alphabet at  
# least once. For example: “The quick brown fox jumps over the lazy dog”.
# Hint: Import and use the string module.

# import string

# def is_pangram(text: str):
#     text = text.lower()
#     alphabets = string.ascii_lowercase
#     # return set(alphabets).issubset(text)
#     return set(alphabets) <= set(text)


# print(is_pangram("The quick brown fox jumps over the lazy dog."))  # True
# print(is_pangram("Pack my box with five dozen liquor jugs."))  # True
# print(is_pangram("The five boxing wizards jump quickly."))  # True
# print(is_pangram("The quick brown fox"))  # False

# ------------------------------------------ASSIGNMENT CORRECTION------------------------------------------------



# def greet(name, time_of_day):
#     print(f"Hello, {name}. Good {time_of_day}")

# greet(time_of_day="afternoon", name="Kemi")



# def greet(time_of_day, name="Stranger"):
#     print(f"Hello, {name}. Good {time_of_day}")

# greet(name="Kemi", time_of_day="afternoon")




# -------------------------------------*ARGS AND **KWARGS-------------------------------------*

# def greet_everyone(names: list):
#     for name in names:
#         print(f"Heyyy, {name}")

    
# greet_everyone(["Kemi", "Favour", "Tina", "Matilda"])

# def greet_everyone(*names):
#     for name in names:
#         print(f"Heyyy, {name}")

# greet_everyone()
# greet_everyone("Kemi")
# greet_everyone("Kemi", "Favour", "Tina", "Matilda")

# print("ebjnfk",'efbnjkmd,l2;.s1/',"yeguifo,d.", 7, True, None)
# print()

# def greet_everyone_with_emojis(**names_with_emojis):
#     for name, emoji in names_with_emojis.items():
#         print(f"{name} {emoji}")

# # greet_everyone_with_emojis()
# # greet_everyone_with_emojis(winnie="😀")
# # greet_everyone_with_emojis(winnie="😀", ope="😩", tobi="🤗")

# names_with_emojis = {'winnie Igboama': '😀', 'ope': '😩', 'tobi': '🤗'}

# greet_everyone_with_emojis(**names_with_emojis)

# -------------------------------------*ARGS AND **KWARGS-------------------------------------*



# *-------------------------------------RECURSION-------------------------------------*

# def power(base, exponent):
#     if exponent == 0:  # Base case
#         return 1
#     else:
#         return base * power(base, exponent - 1)  # Recursive call
    

# print(power(2, 998))  # Output: 8

# 2 * power(2, 2)

# 2 * 2 * power(2, 1)

# 2 * 2 * 2 * power(2, 0)

# 2 * 2 * 2 * 1 = 8


# import random


# account_numbers = [2, 7]

# def generate_account_number():
#     account_number = random.randint(1, 10)
#     if account_number in account_numbers:
#         print(f"{account_number} is already taken")
#         return generate_account_number()
#     print(f"Account number generated: {account_number}")
#     account_numbers.append(account_number)
#     return account_number

# while True:
#     generate_account_number()
#     stop = input("Enter 'x' to stop or leave blanl to continue: ").strip().lower()

#     if stop == "x":
#         print("Exiting")
#         break


# *-------------------------------------RECURSION-------------------------------------*



# *-------------------------------------SCOPE-------------------------------------*

# global_var = 12

# def my_function():
#     local_var = 10  # Local scope
#     print(local_var)
#     global global_var
#     global_var = 20
#     print("Printing from inside the function: ", global_var)

# my_function()
# print("Printing from outside the function", global_var)

# *-------------------------------------SCOPE-------------------------------------*



# *-------------------------------------DOCSTRINGS-------------------------------------*

# docstrings - documentation strings
# def add_two_nums(a, b):
#     """
#     Adds two integers a and b.
#     Returns a + b.
#     """

#     return a + b

# print(add_two_nums(4, 7))

# *-------------------------------------DOCSTRINGS-------------------------------------*



# *-------------------------------------ARGS and KWARGS assignment correction-------------------------------------*
# 14. Create a function called sum_scores_and_bonuses that returns the total of all numbers passed, including keyword values.

# Test Data:
# print(sum_scores_and_bonuses(10, 20, bonus1=5, bonus2=15))
# print(sum_scores_and_bonuses(100, bonus=50))

# Expected Output:
# 50
# 150


# def sum_scores_and_bonuses(*scores, **bonuses):
#     return sum(scores) + sum(bonuses.values())


# print(sum_scores_and_bonuses(10, 20, bonus1=5, bonus2=15))
# print(sum_scores_and_bonuses(100, bonus=50))



# 15. Create a function called longest_word that returns the longest string from all the values passed in (args + kwargs).

# Test Data:
# print(longest_word("cat", "hippopotamus", animal="giraffe", bird="eagle"))
# print(longest_word("short", name="exaggeration", tool="pen"))

# Expected Output:
# hippopotamus
# exaggeration


# def longest_word(*args, **kwargs):
#     return max(list(args) + list(kwargs.values()), key=len)


# print(longest_word("cat", "hippopotamus", animal="giraffe", bird="eagle"))
# print(longest_word("short", name="exaggeration", tool="pen"))

# *-------------------------------------ARGS and KWARGS assignment correction-------------------------------------*
