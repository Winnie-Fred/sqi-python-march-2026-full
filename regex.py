import re

# # Example 1: Simple match
# pattern = r"\bword\b"
# text = "A word in a sentence."
# match = re.search(pattern, text)
# if match:
#     print(match)
#     print("Match found:", match.group())  # Match found: word

# matching

# # Example 2: Find all occurrences
# pattern = r"\d+"
# text = "There are 123 apples and 456 oranges."
# matches = re.findall(pattern, text)
# print("Numbers found:", matches)  # Numbers found: ['123', '456']


# Example 3: Replace text
# pattern = r"\s+"
# text = "This   is a test."
# new_text = re.sub(pattern, " ", text)
# print("Replaced text:", new_text)  # Replaced text: This is a test.



# # Example 1: Match an email address
# pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# text = "Contact us at support@example.com for more info."
# match = re.search(pattern, text)
# if match:
#     print("Email found:", match.group())  # Email found: support@example.com



# # Example 2: Extract dates in YYYY-MM-DD format
# pattern = r"\b\d{4}-\d{2}-\d{2}\b"
# text = "The event is on 2023-08-15. Deadline is 2023-08-01."
# dates = re.findall(pattern, text)
# print("Dates found:", dates)  # Dates found: ['2023-08-15', '2023-08-01']

pattern = r"^\(\d{3}\) \d{3}-\d{4}$"
phone_number = "(123) 456-7890"
if re.match(pattern, phone_number):
    print("Valid phone number")  # Valid phone number
else:
    print("Invalid phone number")