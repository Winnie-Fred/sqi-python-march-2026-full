# Print only even numbers from 2 to 10 (do not use += 2)
# Expected Output:
# 2
# 4
# 6
# 8
# 10



# for i in [1, 2, 3, 4]:
#     print(i)
# else:
#     print("Loop has ended")



# i = 1

# while i < 11:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Loop has stopped")



# adjectives = ["fierce", "majestic", "playful"]
# animals = ["lion", "eagle", "dolphin"]

# for adj in adjectives:
#     for animal in animals:
#         print(adj, animal)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


# for i in matrix:
#     for j in i:
#         print(j)

adjectives = ["fierce", "majestic", "playful"]
animals = ["lion", "eagle", "dolphin", "zebra"]

smallest = min(adjectives, animals, key=len)

# print(smallest)

# for i in range(len(smallest)):
#     adj = adjectives[i]
#     animal = animals[i]

#     print(adj, animal)


# print(list(enumerate(adjectives)))
# print(list(zip(adjectives, animals)))

# print(list(range(1, 7)))

# for i in range(1, 7):
#     print(i)


# for items in zip(adjectives, animals):
#     adj, animal = items
#     print(adj, animal)

# for adj, animal in zip(adjectives, animals):
#     print(adj, animal)


# is_happy = False

# if is_happy:
#     pass    

# print("End of file")


# for i in [1, 2, 3, 4, 5]:
#     pass

# print("End of file")


# Print a square of stars
# Ask the user to enter a number
# Example 1:
# Input: 3

# Output:
# ***
# ***
# ***

# Example 2:
# Input: 5

# Output:
# *****
# *****
# *****
# *****
# *****


# Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 12 = 60


# LiMiTleSs


# word = input("Enter a word: ")

# result = ""

# for i in range(len(word)):
#     if i % 2 == 0:
#         result += word[i].upper()
#     else:
#         result += word[i].lower()

# print(result)


# word = input("Enter a word: ")
# to_upper = True
# result = ""

# for i in range(len(word)):
#     if to_upper:
#         result += word[i].upper()
#     else:
#         result += word[i].lower()
#     to_upper = not(to_upper)

# print(result)




# ***********************************LIST COMPREHENSIONS****************************************

# fruits = ["apple", "banana", "cherry", "date", "eggplant"]

# fruits_copy = fruits.copy()

# fruits_upper = []

# for fruit in fruits:
#     fruits_upper.append(fruit.upper())

# print(fruits)
# print(fruits_upper)




# fruits = ["apple", "banana", "cherry", "date", "eggplant"]

# fruits_upper = [fruit.upper() for fruit in fruits]

# print(fruits_upper)


# words = ["random", "terrible", "chalk", "dirt", "fool", "hippoppotamus"]

# # [6, 8, 5, 4, 4, 13]

# len_words = [len(word) for word in words]

# print(len_words)


# len_words = []

# for word in words:
#     len_words.append(len(word))




# countries = ["Nigeria", "Japan", "Togo", "Ghana", "Tanzania", "USA", "Australia", "Algeria"]

# [1, 2, 0, 2, 3, 1, 3, 2]


# countries = ["Nigeria", "Japan", "Togo", "Ghana", "Tanzania", "USA", "Australia", "Algeria"]

# developed_countries = ["USA", "Australia", "Japan"]

# developing_countries = [country.upper() for country in countries if country not in developed_countries]

# print(developing_countries)


# numbers = [1, 8, 34, 76, 55, 43, 29, 38]

# odd_numbers = 

# tribes = ["Igbo", "Yoruba", "Hausa", "Efik", "Igala", "Ibibio", "Ijaw"]

# not_hausa = (tribe for tribe in tribes if tribe != "Hausa")


# print(not_hausa)



# tribes = ["Igbo", "Yoruba", "Hausa", "Efik", "Igala", "Ibibio", "Ijaw"]

# not_hausa = []

# for tribe in tribes:
#     if tribe != "Hausa":
#         not_hausa.append(tribe)

# print(not_hausa)

# tribes = ["Igbo", "Yoruba", "Hausa", "Efik", "Igala", "Ibibio", "Ijaw"]
# tribes_that_start_with_i = [tribe for tribe in tribes if tribe.startswith("I")]
# print(tribes_that_start_with_i)


# tribes_that_start_with_i = [tribe for tribe in tribes if tribe.lower().startswith("i")]
# print(tribes_that_start_with_i)


# tribes = ["Igbo", "Yoruba", "Hausa", "Efik", "Igala", "Ibibio", "Ijaw"]
# tribes.append("Igala")
# tribes_that_start_with_i = [tribe for tribe in tribes if tribe[0].upper() == "I"]
# print(tribes_that_start_with_i)


# ***********************************LIST COMPREHENSIONS****************************************


# Assignment

# --------------------------------LIST COMPREHENSION EXERCISES--------------------------------
# 1. Create a list of the square of each number
# Input: [1, 2, 3, 4, 5]
# Expected Output: [1, 4, 9, 16, 25]
digits = [1, 2, 3, 4, 5]


# 2. Create a list of names that contain the letter 'a'
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: ["Sara", "Amanda"]
names = ["John", "Sara", "Mike", "Amanda"]


# 3. Create a list of Booleans indicating if each number is greater than 10
# Input: [5, 12, 3, 18, 7]
# Expected Output: [False, True, False, True, False]
values = [5, 12, 3, 18, 7]


# 4. Create a list of the last characters of each word
# Input: ["dog", "cat", "lion", "tiger"]
# Expected Output: ["g", "t", "n", "r"]
animals = ["dog", "cat", "lion", "tiger"]

# --------------------------------LIST COMPREHENSION EXERCISES--------------------------------


# ----------------------------------------------------------------ASSIGNMENT CORRECTION----------------------------------------------------------------


# 2. Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts. Example:
# Input: "hello world"
# Output: Vowels: 3, Consonants: 7


# text = input("Enter some text: ").lower()

# vowels = "aeiou"
# vowel_count = 0
# consonant_count = 0

# for char in text:
#     if not char.isalpha():
#         continue

#     if char in vowels:
#         vowel_count += 1
#     else:
#         consonant_count += 1

# print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")
    



# 6. Write a program that takes an integer input n from the user and prints the first 
# n numbers in the Fibonacci sequence. Example:
# Input: 10
# Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# fibonacci = [0, 1]

# n = int(input("Enter the length of the fibonacci sequence: "))


# for i in range(n-2):
#     next_num = fibonacci[i] + fibonacci[i+1]
#     fibonacci.append(next_num)
#     print(fibonacci)

# print(fibonacci)

# 9. Collect a string from the user and use a loop to count the frequency of each character 
# in the string. Print each character along with its frequency. Example:
# Input: "hello"
# Output:
# h: 1
# e: 1
# l: 2
# o: 1

# occurences = {}

# text = input("Enter some text: ")

# for char in text:
#     if char not in occurences:
#         occurences[char] = 1
#     else:
#         occurences[char] += 1


# for char, occurence in occurences.items():
#     print(f"{char}: {occurence}")


# -------------------------------looping through a dict-------------------------------

# states_and_capitals = {"Ondo": "Akure", "Anambra": "Awka", "Oyo": "Ibadan", "Osun": "Osogbo"}

# for state in states_and_capitals:
#     print(state)

# for capital in states_and_capitals.values():
#     print(capital)


# for state in states_and_capitals.keys():
#     print(state)

# print(states_and_capitals.keys())  # dict_keys -> list
# print(states_and_capitals.values())  # dict_values -> list
# print(states_and_capitals.items())  # dict_items -> list of tuples

# for state, capital in states_and_capitals.items():
#     print(f"The capital of {state} is {capital}")

# -------------------------------looping through a dict-------------------------------


# 12. Collect a string from the user and use a loop to count the number of words in the string. 
# Print the count. Example:
# Input: "Hello world from Python"
# Output: 4

# text = input("Enter some text: ")

# no_of_words = 0

# words = text.split()

# print(words)

# for word in words:
#     no_of_words += 1

# print(no_of_words)


# ----------------------------------------------------------------ASSIGNMENT CORRECTION----------------------------------------------------------------



# ----------------------------------------------------------------COMPREHENSIONS cont'd----------------------------------------------------------------


# Create a list of multiples of 4 between 2 and 45 using a list comprehension
# [4, 8, 12, ..., 32, 36, 40, 44]



# ----------------------------------------------------------------COMPREHENSIONS cont'd----------------------------------------------------------------






# ----------------------------------------------------------------DICTIONARY COMPREHENSIONS----------------------------------------------------------------

# languages = ["Python", "Javascript", "Elixir", "Ruby", "C++", "Go"]

# # {"Python": 6, "Javascript": 10, "Elixir": 6, "Ruby": 4, "C++": 3, "Go": 2}

# len_languages = {language: len(language) for language in languages}

# print(len_languages)


# ----------------------------------------------------------------DICTIONARY COMPREHENSIONS----------------------------------------------------------------


# ----------------------------------------------------------------GENERATORS----------------------------------------------------------------


# tribes = ["Igbo", "Yoruba", "Hausa", "Efik", "Igala", "Ibibio", "Ijaw"]

# # tribe_starts_with_i = [True, False, False, False, True, True, True]

# tribe_starts_with_i = [tribe.lower().startswith("i") for tribe in tribes]

# all_start_with_i = all(tribe_starts_with_i)

# print(all_start_with_i)


# tribes = ["Igbo", "Yoruba", "Hausa", "Efik", "Igala", "Ibibio", "Ijaw"]

# # tribe_starts_with_i = [True, False, False, False, True, True, True]

# tribe_starts_with_i = (tribe.lower().startswith("i") for tribe in tribes)

# all_start_with_i = all(tribe_starts_with_i)

# print(all_start_with_i)


# print(all([True, False, False, False, True, True, True]))
# print(all([True, True, True, True]))
# print(any([True, False, False, False, True, True, True]))
# print(any([False, False, False]))
# print(all([False, False, False]))

# 5. Are all the numbers greater than 10?
# Input: [5, 12, 3, 18, 7]
# Expected Output: False
# values = [5, 12, 3, 18, 7]

# greater_than_10 = (value > 10 for value in values)

# all_greater_than_10 = all(greater_than_10)

# print(all_greater_than_10)


# values = [5, 12, 3, 18, 7]

# all_greater_than_10 = all(value > 10 for value in values)

# print(all_greater_than_10)


# 6. Is there any name that contains the letter 'a'?
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: True
# names = ["John", "Sara", "Mike", "Amnd"]

# any_name_contains_a = any("a" in name.lower() for name in names)

# print(any_name_contains_a)


# ----------------------------------------------------------------GENERATORS----------------------------------------------------------------
