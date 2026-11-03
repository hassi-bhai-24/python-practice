"""
Library Management System
● Book class with title, author, ISBN
● Library class managing book collection
● Methods: add_book(), find_book(), list_books()
"""






class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")





class Library:
    def __init__(self):
        self.books = []   # list to store Book objects

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                print("Book Found:")
                book.display()
                return
        print("Book not found")

    def list_books(self):
        if not self.books:
            print("No books in library")
        else:
            print("Library Books:")
            for book in self.books:
                book.display()







library = Library()

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Find Book")
    print("3. List Books")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        book = Book(title, author, isbn)
        library.add_book(book)

    elif choice == "2":
        isbn = input("Enter ISBN to search: ")
        library.find_book(isbn)

    elif choice == "3":
        library.list_books()

    elif choice == "4":
        print("Exiting Library System")
        break

    else:
        print("Invalid choice, try again")

















