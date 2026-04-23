def addition(num1, num2):
    print(f"{num1} + {num2} = {num1+num2}")

def subtraction(num1, num2):
    print(f"{num1} - {num2} = {num1-num2}")

def multiplication(num1, num2):
    print(f"{num1} X {num2} = {num1*num2}")

def division(num1, num2):
    if num2 == 0:
        print("Cannot divide by zero")
        return
    print(f"{num1} / {num2} = {num1/num2}")




print("Welcome to the Simple Calculator")
menu = """
Select operation:
add -  Addition
sub -  Subtraction
mul -  Multiplication
div -  Division
quit - Exit
"""


while True:
    print(menu)
    choice = input("Enter your choice from the menu above: ")

    if choice == "quit":
        print("goodbye👋")
        break

    if choice not in ["add", "sub", "mul", "div"]:
        print("Invalid operation")
        continue
    
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter second number: "))

    if choice == "add":
        addition(first_num, second_num)
    elif choice == "sub":
        subtraction(first_num, second_num)
    elif choice == "mul":
        multiplication(first_num, second_num)
    elif choice == "div":
        division(first_num, second_num)
