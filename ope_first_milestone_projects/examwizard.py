# Project Overview:
# Develop an Exam Wizard program in Python that hardcodes a set of at least 5 theory 
# questions and evaluates the student's answers based on the presence of specific keywords or phrases. The program should ask these questions to the user one by one and display the user's score at the end.

# Requirements:
# Hardcode Questions and Keywords:
# Create at least 5 theory questions.
# For each question, determine the essential keywords or phrases that should be included in the ideal answer.
# Assign weights to each keyword based on its importance.
# Question Prompting:
# Prompt the user with each question one by one.
# Allow the user to input their answer for each question.
# Scoring System:
# Evaluate the user's answers based on the presence of the specified keywords..
# Keep track of the user's score.
# Display Results:
# At the end of the quiz, display the user's total score out of the max score e.g. 10/12.

# Sample Question and Evaluation Criteria:
# Question: Explain the process of photosynthesis.

# Ideal Answer: Photosynthesis is a process used by plants and other organisms to convert light energy into chemical energy. It occurs in the chloroplasts of plant cells. The process involves the absorption of light by chlorophyll, the conversion of carbon dioxide and water into glucose and oxygen, and the storage of energy in the form of ATP.

# Keywords and Weights:
# Photosynthesis (2 points)
# Light energy (1 point)
# Chemical energy (1 point)
# Chloroplasts (2 points)
# Chlorophyll (1 point)
# Carbon dioxide (1 point)
# Water (1 point)
# Glucose (1 point)
# Oxygen (1 point)
# ATP (1 point)

# Example of Keyword-Based Marking:
# Student's Answer: Photosynthesis is a process in which plants use sunlight to make 
# food. It happens in the chloroplasts where chlorophyll absorbs light. The plants take in carbon dioxide and water, and produce glucose and oxygen.
# Marked Answer:
# Photosynthesis (2 points)
# Chloroplasts (2 points)
# Chlorophyll (1 point)
# Carbon dioxide (1 point)
# Water (1 point)
# Glucose (1 point)
# Oxygen (1 point)
# Total Score: 9 out of 12 points.

questions = [
    {
        "question": "Explain the process of photosynthesis.",
        "keywords": {
            "photosynthesis": 2,
            "light energy": 1,
            "chemical energy": 1,
            "chloroplasts": 2,
            "chlorophyll": 1,
            "carbon dioxide": 1,
            "water": 1,
            "glucose": 1,
            "oxygen": 1,
            "atp": 1
        }
    },
    {
        "question": "What is Python?",
        "keywords": {
            "programming language": 2,
            "interpreted": 1,
            "high-level": 1,
            "easy to read": 1
        }
    },
    {
        "question": "What is a variable in Python?",
        "keywords": {
            "store": 1,
            "data": 1,
            "value": 1,
            "memory": 1
        }
    },
    {
        "question": "Explain what a loop is.",
        "keywords": {
            "repeat": 2,
            "code": 1,
            "for loop": 1,
            "while loop": 1
        }
    },
    {
        "question": "What is a function in Python?",
        "keywords": {
            "block of code": 2,
            "reuse": 1,
            "def": 1,
            "task": 1
        }
    }
]
total_score = 0
max_score = 0

for item in questions:
    for weight in item["keywords"].values():
        max_score += weight
for item in questions:
    print("\n" + item["question"])
    user_answer = input("Your answer: ").lower()

    question_score = 0

    for keyword, weight in item["keywords"].items():
        if keyword in user_answer:
            question_score += weight

    print("Score for this question:", question_score)
    total_score += question_score

print("\nExam completed!")
print("Your total score is:", total_score, "out of", max_score)