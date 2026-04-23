# OOP - Object Oriented Programming

# paradigm - a way of programming

# structural, modular, oop, functional


# oop => classes and objects and methods


# capital or upper camel casing

# BankAccount bank_account bankAccount
# snake_casing
# camelCasing
# PascalCasing
# kebab-casing 
# sqi-python-mar-2026

# class ClassExample:
#     pass



# class Person:
#     def __init__(self, first_name: str, last_name: str, age: int, height: float, is_dark: bool, is_male: bool):
#         print("__init__ running")
#         self.person_first_name = first_name
#         self.person_last_name = last_name
#         self.age = age
#         self.height = height
#         self.is_dark = is_dark
#         self.is_male = is_male

    
#     def walk(self):
#         print("I am walking")

#     def introduce_oneself(self):
#         gender = "male" if self.is_male else "female"
#         print(f"My name is {self.person_first_name} {self.person_last_name}. I am {gender}. I am {self.age} years old")

#     def say_mood(self, mood, time_of_day):
#         print(f"I am {mood} {time_of_day}.")



# # objects
# ope = Person("Ope", "Nelson", 39, 1.78, False, True)
# winnie = Person("Winifred", "Igboama", 24, 1.56, True, False)

# # encapsulation

# print(ope.age)
# winnie.walk()
# ope.introduce_oneself()
# print(ope.person_first_name)
# winnie.say_mood("happy", "today")



# Create a class called BankAccount with the attributes bank_name, account_holder, is_savings, account_balance
# A BankAccount has the methods `deposit`, `withdraw`, `account_details`

# class BankAccount:
#     """This is a bank account class that helps to withdraw and deposit money"""
#     def __init__(self, bank_name: str, account_holder: str, is_savings: bool, account_balance: float):
#         self.bank_name = bank_name
#         self.account_owner = account_holder
#         self.account_balance = account_balance
#         self.has_above_50000 = account_balance > 50000
#         self.account_type = "SAVINGS" if is_savings else "CURRENT"

#     def account_details(self):
#         return f"""
# Account Owner: {self.account_owner}
# Account Balance: {self.account_balance}
# Account Type: {self.account_type}
# """

#     def deposit(self, amount: float):
#         self.account_balance += amount
#         return "Deposit successful"

#     def withdraw(self, amount: float):
#         if amount > self.account_balance:
#             return "Insufficient funds"
#         self.account_balance -= amount
#         return "Withdrawal successful"


# account_one = BankAccount("Opay", "Winifred Igboama", True, 9000.54)
# account_two = BankAccount("First Bank", "Ope Nelson", False, 900_000_000.08)

# # print(account_one.account_balance)
# # account_one.account_balance = 7655.67
# # print(account_one.account_balance)

# print(account_one.account_details())
# print(account_one.deposit(5678))
# print(account_one.account_details())


# print(account_two.account_details())
# print(account_two.withdraw(5400.56))
# print(account_two.account_details())




# 1. Create a class called Car with the following attributes:
#    - brand
#    - model
#    - year
#    - horsepower
#    - fuel_type
#
#    The class should have a method called car_info() that returns:
#    "This is a {year} {brand} {model} with {horsepower} HP running on {fuel_type}."
#
#    After defining the class, create 3 different Car objects with different values.



# 2. Create a class called Student with the following attributes:
#    - name
#    - age
#    - grades (a list of integers)
#
#    The class should have two methods:
#    - average_grade(): returns the average of all grades
#    - is_passing(): returns True if the average grade is >= 50, otherwise False
#
#    After defining the class, create 2 different Student objects with different values.

# another name for object is instance



# class Circle:
#     PI = 22 / 7

#     def __init__(self, radius):
#         self.radius = radius
#         self.diameter = radius * 2

#     def area(self):
#         # return self.PI * (self.radius ** 2)
#         return Circle.PI * (self.radius ** 2)
    
#     def circumference(self):
#         # return 2 * self.PI * self.radius
#         return 2 * Circle.PI * self.radius
    

# circle = Circle(6)
# print(circle.area())

# print(circle.PI)

# print(Circle.PI)



# class Circle:
#     PI = 22 / 7

#     def __init__(something, radius):
#         something.radius = radius
#         something.diameter = radius * 2

#     def area(anything):
#         # return anything.PI * (anything.radius ** 2)
#         return Circle.PI * (anything.radius ** 2)
    
#     def circumference(sonmething_else):
#         # return 2 * sonmething_else.PI * sonmething_else.radius
#         return 2 * Circle.PI * sonmething_else.radius
    

# my_circle = Circle(7)

# print(my_circle)

# circle = Circle(6)
# print(circle.area())


# 1. Create a class called Laptop with the following attributes:
#    - brand
#    - ram (in GB)
#    - storage (in GB)
#    - price
#
#    The class should have two methods:
#    - upgrade_ram(extra_ram): increases the ram by extra_ram
#    - laptop_info(): returns "{brand} laptop with {ram}GB RAM and {storage}GB storage costs {price}."
#
#    After defining the class, create 2 different Laptop objects with different values.





# 2. Create a class called Employee with the following attributes:
#    - name
#    - position
#    - salary
#
#    The class should have two methods:
#    - give_raise(amount): increases salary by amount
#    - employee_info(): returns "{name} works as a {position} and earns {salary} per year."
#
#    After defining the class, create 3 different Employee objects with different values.


# class Book:
#     def __init__(self, author: str, title: str, no_of_pages: int, is_fiction: bool, year_of_pub: int):
#         self.author = author
#         self.title = title
#         self.no_of_pages = no_of_pages
#         self.is_fiction = is_fiction
#         self.year_of_pub = year_of_pub



# class Library:
#     def __init__(self, books: list[Book]):
#         self.books = books

#     def add_book(self, book: Book):
#         self.books.append(book)

#     def how_many_pages(self):
#         return sum(book.no_of_pages for book in self.books)


# book1 = Book(author="George Orwell", title="1984", no_of_pages=328, is_fiction=True, year_of_pub=1949)
# book2 = Book(author="Michelle Obama", title="Becoming", no_of_pages=448, is_fiction=False, year_of_pub=2018)
# book3 = Book(author="J.K. Rowling", title="Harry Potter and the Philosopher's Stone", no_of_pages=223, is_fiction=True, year_of_pub=1997)

# print(book1)
# print(book2)
# print(book3)

# community_library = Library([book1, book2])
# community_library.add_book(book3)
# print(community_library.books)  # 
# print(community_library.how_many_pages())



# A CartItem is made up of item, price and qty
# A Cart is made up of a list of CartItems
# A Cart can return its total


# cart_item1 = CartItem("eggs", 250, 4)
# cart_item2 = CartItem("bread", 1200, 6)
# cart = Cart([cart_item1, cart_item2])
# print(cart.cart_total()) # -> 8200


# class CartItem:
#     def __init__(self, item: str, price: int, quantity: int):
#         self.item = item
#         self.price = price
#         self.quantity = quantity

# class Cart:
#     def __init__(self, items: list[CartItem]):
#         self.items = items

#     def cart_total(self):
#         return sum(item.price * item.quantity for item in self.items)
    

# cart_item1 = CartItem("eggs", 250, 4)
# cart_item2 = CartItem("bread", 1200, 6)
# cart = Cart([cart_item1, cart_item2])
# print(cart.cart_total()) # -> 8200


# class CartItem:
#     def __init__(self, item: str, price: int, quantity: int):
#         self.item = item
#         self.price = price
#         self.quantity = quantity

#     def total(self):
#         return self.price * self.quantity

# class Cart:
#     def __init__(self, items: list[CartItem]):
#         self.items = items

#     def cart_total(self):
#         return sum(item.total() for item in self.items)
    

# cart_item1 = CartItem("eggs", 250, 4)
# cart_item2 = CartItem("bread", 1200, 6)
# cart = Cart([cart_item1, cart_item2])
# print(cart.cart_total()) # -> 8200


# Movie Ticket Booking System

# A cinema is building a simple system to calculate the total cost of tickets purchased by a customer.

# Each ticket type has:

# a movie name
# a price per ticket
# a number of tickets purchased

# The system should compute the total cost for all tickets in a booking.

# Sample Execution
# ticket1 = Ticket("Avengers", 3500, 3)
# ticket2 = Ticket("Lion King", 2500, 2)

# booking = Booking([ticket1, ticket2])
# print(booking.total_cost())

# Expected Output
# 15500



# Exercise: Notes & Notebook System

# A simple note-taking app allows users to organize their thoughts.

# Each note has:

# a title
# a content/body text

# The notebook stores multiple notes and should provide useful functionality.

# Sample Execution
# note1 = Note("Shopping List", "eggs milk bread butter")
# note2 = Note("Ideas", "build an app write a book")
# note3 = Note("Reminder", "call mom tomorrow")

# notebook = Notebook([note1, note2, note3])

# print(notebook.total_words())
# print(notebook.find_by_keyword("app"))

# Expected Output
# 12
# Ideas



# # -------------INSTANCE ATTRIBUTES OUTSIDE __INIT__----------------

# class CartItem:

#     def __init__(self, item: str, price: int, quantity: int):
#         self.item = item
#         self.price = price
#         self.quantity = quantity
#         self.my_total = 0
#         print("__init__ running")

#     def total(self):
#         self.my_total = self.price * self.quantity
#         return self.price * self.quantity
    
#     def display_cart(self):
#         print(f"CartItem has {self.item} that costs {self.price}. Total is {self.my_total}")

# class Cart:
#     HAS_WHEELS = True
#     def __init__(self, items: list[CartItem]):
#         self.items = items

#     def cart_total(self):
#         return sum(item.total() for item in self.items)
    
# cart_item = CartItem("eggs", 250, 4)
# cart_item.total()
# cart_item.display_cart()

# # -------------INSTANCE ATTRIBUTES OUTSIDE __INIT__----------------


# -------------MAGIC DUNDER METHODS----------------
# magic double-underscore method
# class CartItem:

#     def __init__(self, item: str, price: int, quantity: int):
#         self.item = item
#         self.price = price
#         self.quantity = quantity
#         self.my_total = 0
#         print("__init__ running")

#     # def __str__(self):
#     #     return f"CartItem has {self.item} that costs {self.price} -> {self.total()}"
    
#     def __repr__(self):
#         return f'CartItem(item="{self.item}", price={self.price}, quantity={self.quantity})'

#     def total(self):
#         self.my_total = self.price * self.quantity
#         return self.price * self.quantity
    
#     def display_cart(self):
#         print(f"CartItem has {self.item} that costs {self.price}. Total is {self.my_total}")

# class Cart:
#     HAS_WHEELS = True
#     def __init__(self, items: list[CartItem]):
#         self.items = items

#     def __len__(self):
#         return len(self.items)

#     def cart_total(self):
#         return sum(item.total() for item in self.items)
    
# cart_item1 = CartItem("eggs", 250, 4)

# # print(cart_item1)

# # print(str(cart_item1))

# cart_item2 = CartItem("bread", 450, 10)
# # print(cart_item2)

# # print(repr(cart_item1))
# # print(repr(cart_item2))

# cart = Cart([cart_item1, cart_item2])
# cart = Cart([cart_item1, cart_item2, cart_item1, cart_item2])

# print(len(cart))

# -------------MAGIC DUNDER METHODS----------------



# -------------ISINSTANCE()----------------

# num = 10
# print(isinstance(num, int))
# print(isinstance(num, bool))


# class CartItem:

#     def __init__(self, item: str, price: int, quantity: int):
#         self.item = item
#         self.price = price
#         self.quantity = quantity
#         self.my_total = 0
#         print("__init__ running")

#     # def __str__(self):
#     #     return f"CartItem has {self.item} that costs {self.price} -> {self.total()}"
    
#     def __repr__(self):
#         return f'CartItem(item="{self.item}", price={self.price}, quantity={self.quantity})'

#     def total(self):
#         self.my_total = self.price * self.quantity
#         return self.price * self.quantity
    
#     def display_cart(self):
#         print(f"CartItem has {self.item} that costs {self.price}. Total is {self.my_total}")

# class Cart:
#     HAS_WHEELS = True
#     def __init__(self, items: list[CartItem]):
#         self.items = items

#     def __len__(self):
#         return len(self.items)

#     def cart_total(self):
#         return sum(item.total() for item in self.items)
    
# cart_item1 = CartItem("eggs", 250, 4)

# # print(cart_item1)

# # print(str(cart_item1))

# cart_item2 = CartItem("bread", 450, 10)
# # print(cart_item2)

# # print(repr(cart_item1))
# # print(repr(cart_item2))

# cart = Cart([cart_item1, cart_item2])
# cart = Cart([cart_item1, cart_item2, cart_item1, cart_item2])

# print(isinstance(cart, Cart))
# print(isinstance(cart, CartItem))

# -------------ISINSTANCE()----------------




# ENCAPSULATION
# INHERITANCE
# POLYMORPHISM


# class Animal:
#     def __init__(self, name: str, type: str, has_wings: bool, has_tail: bool, is_mammal: bool, sound: str):
#         self.name = name
#         self.type = type
#         self.has_wings = has_wings
#         self.has_tail = has_tail
#         self.is_mammal = is_mammal
#         self.sound = sound

#     def introduce_yourself(self):
#         # ternary operator
#         return f"I am a/an {self.type}. My name is {self.name}. It is {self.has_wings} that I have wings. I {self.sound}."
        


# fido = Animal("Fido", "cat", False, True, True, "meow")
# print(fido.introduce_yourself())

# # MRO - Method Resolution Order

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name, type, False, True, True, "bark")
#         self.breed = breed

#     def introduce_yourself(self):
#         animal_intro = super().introduce_yourself()
#         return animal_intro + f" I am a/an {self.breed}."
    
#     def bark(self):
#         return "I am barking"

# jaguar = Dog("Jaguar", "German Sherpherd")
# print(jaguar.introduce_yourself())
# print(jaguar.sound)
# print(jaguar.name)
# print(jaguar.bark())




# Exercise: Digital Library System

# You are modeling a simple system for a digital library.

# 🎯 What is expected
# There should be a base class representing a general library item.
# The class should store basic information such as:
# title
# creator (e.g., author, director, etc.)
# whether it is available
# The class should include a method that describes the item in a sentence.
# There should be a child class that represents a specific type of item (e.g., a Book).
# This child class should:
# Extend the base class
# Add at least one extra property (e.g., number of pages, genre, etc.)
# Modify the description method to include the extra detail
# There should be another child class representing a different type of item (e.g., Movie or Magazine).
# This class should:
# Also inherit from the base class
# Have its own unique attribute
# Provide its own version of the description
# Demonstrate:
# Creating objects from each class
# Accessing attributes
# Calling methods
# How inheritance changes behavior


# ▶️ Example Execution
# book1 = Book("1984", "George Orwell", True, 328)
# print(book1.describe())

# movie1 = Movie("Inception", "Christopher Nolan", False, 148)
# print(movie1.describe())

# print(book1.title)
# print(movie1.is_available)



# ✅ Expected Output (example)
# This item is titled 1984 by George Orwell. It is available. It has 328 pages.
# This item is titled Inception by Christopher Nolan. It is not available. Duration is 148 minutes.
# 1984
# False



# ------------------------------------------------------POLYMPORPHISM------------------------------------------------------

# morphine, muffin, morphing

# class Device:
#     def operate(self):
#         print("Operating device")

# class SmartPhone:
#     def operate(self):
#         print("Operating Smartphone")

# class AirConditioner:
#     def operate(self):
#         print("Operating Air Conditioner")

    
# device = Device()
# smartphone = SmartPhone()
# ac = AirConditioner()

# devices = [device, smartphone, ac]

# for device in devices:
#     device.operate()


# class Device:
#     def operate(self):
#         print("Operating device")

# class SmartPhone(Device):
#     pass

# class AirConditioner(Device):
#     pass

    
# device = Device()
# smartphone = SmartPhone()
# ac = AirConditioner()

# devices = [device, smartphone, ac]

# for device in devices:
#     device.operate()




# --------------------------------INHERITANCE EXAMPLE-------------------------------------

# FANTASY GAME


# You are building a simple simulation of a fantasy battle. Create different types of game 
# characters.

# 1. Create a base class
# Create a class called GameCharacter that has:
# Attributes:
# name (string)
# health (integer)
# attack_power (integer)

# Methods:
# A method attack(target) that reduces the target's health by self.attack_power.


class GameCharacter:
    def __init__(self, name: str, health: int, attack_power: int):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target: GameCharacter):
        if self == target:
            print(f"{self.name} cannot attack themself")
            return

        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name}!")
        print(f"{target.name}'s health is now {target.health}")



# 2. Create subclasses
# Warrior
# Has an extra attribute: armor (integer)
# Override attack(target) so that it deals extra 10 damage.


# Mage
# Has an extra attribute: mana (integer)
# Override attack(target) so that it uses 5 mana each time it attacks. 
# If mana is less than 5, print "Not enough mana to attack".

# 3. Handle cases where the target is the same as the attacker.


class Warrior(GameCharacter):
    def __init__(self, name, health, attack_power, armor):
        super().__init__(name, health, attack_power)
        self.armor = armor

    def attack(self, target):
        target.health -= 10
        super().attack(target)
    

class Mage(GameCharacter):
    def __init__(self, name, health, attack_power, mana):
        super().__init__(name, health, attack_power)
        self.mana = mana

    def attack(self, target):
        if self.mana < 5:  # guard
            print("not enough mana to attack")
            return
        super().attack(target)
        self.mana -= 5


# SAMPLE EXECUTION 1
warrior = Warrior(name="Thor", health=100, attack_power=10, armor=20)
mage = Mage(name="Merlin", health=100, attack_power=10, mana=10)
warrior.attack(mage)
# Output:
# Thor attacks Merlin!
# Merlin's health is now 80
mage.attack(warrior)
# Output:
# Merlin attacks Thor!
# Thor's health is now 90
mage.attack(warrior)
# Output:
# Merlin attacks Thor!
# Thor's health is now 80
mage.attack(warrior)
# Output:
# Not enough mana to attack
print(warrior.health)  # 80
print(mage.health)  # 80
print(mage.mana)  # 0


# SAMPLE EXECUTION 2
merlin = Mage(name="Merlin", health=100, attack_power=20, mana=10)
gaius = Mage(name="Gaius", health=100, attack_power=10, mana=30)

merlin.attack(gaius)
# Output:
# Merlin attacks Gaius
# Gaius’s health is now 80
gaius.attack(merlin)
# Output:
# Gaius attacks Merlin
# Merlin’s health is now 90
gaius.attack(gaius)
# Output:
# Gaius cannot attack themself
gaius.attack(merlin)
# Output:
# Gaius attacks Merlin
# Merlin’s health is now 80
merlin.attack(gaius)
# Output:
# Merlin attacks Gaius
# Gaius’s health is now 60
merlin.attack(gaius)
# Output:
# Not enough mana to attack





# --------------------------------INHERITANCE EXAMPLE-------------------------------------





# ------------------------------------------------------SPACECRAFT ASSIGNMENT------------------------------------------------------


# class Spacecraft:
#     def __init__(self, name: str, fuel: int):
#         self.name = name
#         self.fuel = fuel
#     def launch(self):
#         if self.fuel < 50:
#             print("Not enough fuel")
#         else:
#             print(f"Launching {self.name}")
#             self.fuel -= 50
#     def refuel(self, amount):
#         if amount < 0:
#             print("Cannot refuel with negative amount.")
#         else:
#             self.fuel += amount
#             print(f"Refueled {self.name} with {amount} units. Fuel is now {self.fuel}")

# class CargoShip(Spacecraft):
#     def __init__(self, name: str, fuel: int, cargo_weight: int):
#         super().__init__(name, fuel)
#         self.cargo_weight = cargo_weight
#     def launch(self):
#         fuel_needed = 50 + (self.cargo_weight * 2)
#         if self.fuel < fuel_needed:
#             print("Not enough fuel to launch")
#         else:
#             print(f"Launching {self.name} with cargo!")
#             self.fuel -= fuel_needed
# class PassengerShip(Spacecraft):
#     def __init__(self, name: str, fuel: int, passenger_count: int):
#         super().__init__(name, fuel)
#         self.passenger_count = passenger_count
#     def launch(self):
#         if self.passenger_count > 100:
#             print ("Too many passengers. Cannot launch.")
#         elif self.fuel < 50:
#             print("Not enough fuel to launch")
#         else:
#             print(f"Launching {self.name}")
#             self.fuel -= 50
 
# cargo_ship = CargoShip("Galactic Hauler", 200, 30)
# passenger_ship = PassengerShip("Star Voyager", 100, 80)

# # Attempt to launch both ships
# cargo_ship.launch()
# # Output: Launching Galactic Hauler with cargo!
# # Fuel after launch: 200 - (50 + 30*2) = 90

# passenger_ship.launch()
# # Output: Launching Star Voyager!
# # Fuel after launch: 100 - 50 = 50

# # Refuel both ships
# cargo_ship.refuel(50)
# # Output: Refueled Galactic Hauler with 50 units. Fuel is now 140.

# passenger_ship.refuel(30)
# # Output: Refueled Star Voyager with 30 units. Fuel is now 80.

# # Launch again after refueling
# cargo_ship.launch()
# # Output: Launching Galactic Hauler with cargo!
# # Fuel after launch: 140 - (50 + 30*2) = 30

# passenger_ship.launch()
# # Output: Launching Star Voyager!
# # Fuel after launch: 80 - 50 = 30

# # Try to refuel with invalid amount
# cargo_ship.refuel(-10)
# # Output: Cannot refuel with negative amount.

# # Test PassengerShip with too many passengers
# passenger_ship.passenger_count = 120
# passenger_ship.launch()
# # Output: Too many passengers. Cannot launch.

# # Try to launch cargo ship with low fuel
# cargo_ship.launch()
# # Output: Not enough fuel to launch.

# ------------------------------------------------------SPACECRAFT ASSIGNMENT------------------------------------------------------
