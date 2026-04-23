# Project Overview:
# Develop a simple Computer-Based Testing (CBT) program in Python that hardcodes a set of 
# at least 5 objective questions and their answers. The program should ask these questions 
# to the user one by one and display the user's score at the end.

# Requirements:
# Hardcode Questions and Answers:
# Create at least 5 objective questions (multiple choice or true/false).
# Hardcode these questions and their correct answers in your program.
# Question Prompting:
# Prompt the user with each question one by one.
# Allow the user to input their answer for each question.
# Scoring System:
# Compare the user's answers with the correct answers.
# Keep track of the user's score.
# Display Results:
# At the end of the quiz, display the user's total score.

questions = [
    {'question': "What type is returned when two lists are concatenated?", 'options': ['a. List', 'b. String', 'c. Error'], 'answer': 'a'},

    {'question': 'Who created Python programming language?', 'options': ['a. Tobi Dada', 'b. Dennis Ritchie', 'c. Guido Van Rossum'], 'answer': 'c'},

    {'question': 'Is Python an interpreted or compiled language?', 'options': ['a. Interpreted', 'b. Compiled', 'c. No Idea'], 'answer': 'a'},

    {'question': 'Is Python a strongly typed or loosely typed language?', 'options': ['a. Strongly typed', 'b. Loosely typed', 'c. No Idea'], 'answer': 'b'},

    {'question': 'Which data type is used to store multiple items in a single variable?', 'options': ['a. Integer', 'b. List', 'c. Boolean'], 'answer': 'b'},

    {'question': 'What keyword is used to define a function in Python?', 'options': ['a. func', 'b. def', 'c. function'], 'answer': 'b'},

    {'question': 'Which of these is a valid Python variable name?', 'options': ['a. 1name', 'b. name_1', 'c. name-1'], 'answer': 'b'},

    {'question': 'Which keyword is used for a conditional statement in Python?', 'options': ['a. if', 'b. for', 'c. while'], 'answer': 'a'},

    {'question': 'Which function is used to get input from the user?', 'options': ['a. get()', 'b. input()', 'c. read()'], 'answer': 'b'},

    {'question': 'Which loop is used when the number of iterations is known?', 'options': ['a. while loop', 'b. for loop', 'c. do-while loop'], 'answer': 'b'},
]
total_score = 0

for question in questions:
    print("\n" + question["question"])

    for option in question["options"]:
        print(option)

    user_answer = input("Enter your answer: ").lower()

    if user_answer == question["answer"]:
        print("Correct")
        total_score += 1
    else:
        print("Wrong answer, try again some other time.")
print("\nQuiz completed!")
print("Your total score is:", total_score, "out of", len(questions))