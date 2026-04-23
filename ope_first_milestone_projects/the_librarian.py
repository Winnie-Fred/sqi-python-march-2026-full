# Project Overview:
# Create a simple library management system where users can add, view, update, and delete 
# books in a file named `the_librarian.py`.

# Requirements:
# Data Storage: Use a list of dictionaries to store book information. Each book should have the following attributes:
# Title (string)
# Author (string)
# Year of publication (int)
# ISBN (string)
# Available (boolean)
# Functions/Actions:
# add_book(): Add a new book to the library.
# view_books(): Display all the books in the library.
# update_book(isbn): Update the information of a book given its ISBN.
# delete_book(isbn): Remove a book from the library using its ISBN.
# search_book(title): Search for a book by its exact title.
# borrow_book(isbn): Mark a book as borrowed (not available).
# return_book(isbn): Mark a book as returned (available).
# User Interface: Use a loop to display a menu and prompt the user for an action above until they choose to exit. Assume the user always inputs the correct data types.

library = [
    {"title": "Things Fall Apart", "author": "Chinua Achebe", "year": 1997, "isbn": "877-678-788-299", "available": True},
    {"title": "And then there were None", "author": "Agetha Christie", "year": 1907, "isbn": "877-298-788-629", "available": False},
]

# library = []

def find_book_by_isbn(isbn):
    for book in library:
        if book["isbn"] == isbn:
            return book
    return None
    
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = int(input("Enter year of publication: "))
    isbn = input("Enter ISBN: ")

    existing_book = find_book_by_isbn(isbn)
    if existing_book is not None:
        print("A book with this ISBN already exists.")
        return
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "isbn": isbn,
        "available": True
    }
    library.append(book)
    print("Book added successfully.")

def view_books():
    if not library:
        print("No books in the library.")
        return
    
    print("\nLibrary Books:")
    for book in library:
        print("----------------------------")
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Year:", book["year"])
        print("ISBN:", book["isbn"])
        print("Available:", book["available"])
    print("----------------------------")

def update_book(isbn):
    book = find_book_by_isbn(isbn)

    if book is None:
        print("Book not found.")
        return
    print("Enter new details for the book:")
    # book["title"] = input("New title: ")
    # book["author"] = input("New author: ")
    # book["year"] = int(input("New year of publication: "))
    # book["isbn"] = input("New ISBN: ")

    book["title"] = input(f"New title or leave blank to use '{book['title']}': ") or book["title"]
    book["author"] = input(f"New author or leave blank to use '{book['author']}': ") or book["author"]
    book["year"] = input(f"New year of publication or leave blank to use '{book['year']}': ") or book["year"]
    if book["year"]:
        book["year"] = int(book["year"])
    book["isbn"] = input(f"New ISBN or leave blank to use '{book['isbn']}': ") or book["isbn"]

    

    print("Book updated successfully.")

def delete_book(isbn):
    book = find_book_by_isbn(isbn)

    if book is None:
        print("Book not found")
        return
    library.remove(book)
    print("Book deleted successfully.")

def search_book(title):
    for book in library:
        if book["title"] == title:
            print("Book found:")
            print("----------------------------")
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Year:", book["year"])
            print("ISBN:", book["isbn"])
            print("Available:", book["available"])
            print("----------------------------")
            return
    print("Book not found.")

def borrow_book(isbn):
    book = find_book_by_isbn(isbn)

    if book is None:
        print("Book not found.")
        return

    if not book["available"]:
        print("Book is already borrowed.")
    else:
        book["available"] = False
        print("Book borrowed successfully.")


def return_book(isbn):
    book = find_book_by_isbn(isbn)

    if book is None:
        print("Book not found.")
        return

    if book["available"]:
        print("Book is already available in the library.")
    else:
        book["available"] = True
        print("Book returned successfully.")

def menu():
    while True:
        print("\n ===== Library Management System ====")
        print("1. Add book")
        print("2. View books")
        print("3. Update book")
        print("4. Delete book")
        print("5. Search book by title")
        print("6. Borrow book")
        print("7. Return book")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            isbn = input("Enter ISBN of the book to update: ")
            update_book(isbn)

        elif choice == "4":
            isbn = input("Enter ISBN of the book to delete: ")
            delete_book(isbn)

        elif choice == "5":
            title = input("Enter exact title of the book to search: ")
            search_book(title)

        elif choice == "6":
            isbn = input("Enter ISBN of the book to borrow: ")
            borrow_book(isbn)

        elif choice == "7":
            isbn = input("Enter ISBN of the book to return: ")
            return_book(isbn)

        elif choice == "8":
            print("Exiting program. Goodbye.")
            break

        else:
            print("Invalid choice. Please try again.")
menu()