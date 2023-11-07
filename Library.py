# Low level design for Library management system:
# requirements:
# 1. there will be a user who wants to search and a book in library and assign it to that particular user if not alredy assigned to some one else.
# 2. write it using oops principle in python

class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_available = True

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.checked_out_books = []

class Library:

    def __init__(self) -> None:
        self.users = {}
        self.books = {}
        self.book_id_counter = 1
        self.user_id_counter = 1

    def add_user(self, name):
        user = User(name, self.user_id_counter)
        self.users[self.user_id_counter] = user
        self.user_id_counter += 1

    def add_book(self, title, author):
        book = Book(title, author, self.book_id_counter)
        self.books[self.book_id_counter] = book
        self.book_id_counter += 1
    
    def search_book(self, title, author):
        for book_id, book in self.books.items():
            if book.title == title and book.author == author and book.is_available:
                return book
        return None

    def checkout_book(self, user_id, book_id):
        user = self.users.get(user_id)
        book = self.books.get(book_id)

        if user and book:
            if book.is_available:
                user.checked_out_books.append(book)
                book.is_available = False
                return True
        return False
    def return_book(self, user_id, book_id):
        user = self.users.get(user_id)
        book = self.books.get(book_id)

        if user and book:
            if book not in user.checked_out_books:
                return False
            else:
                user.checked_out_books.remove(book)
                book.is_available = True
                return True
        return False
        

# Creating a library
library = Library()

# Adding books to the library
library.add_book("Book 1", "Author 1")
library.add_book("Book 2", "Author 2")
library.add_book("Book 3", "Author 3")

# Adding users to the library
library.add_user("User 1")
library.add_user("User 2")

# Searching for a book and assigning it to a user
user_id = 1
book_to_search = library.search_book("Book 1", "Author 1")

print("book_to_search==>", book_to_search)

if book_to_search:
    success = library.checkout_book(user_id, book_to_search.book_id)
    if success:
        print(f"Book '{book_to_search.title}' assigned to User {user_id}")
    else:
        print("Book is already assigned or not available")

# Returning a book
user_id = 1
book_id = 1  # You should obtain this from the book you've checked out
success = library.return_book(user_id, book_id)
if success:
    print(f"Book with ID {book_id} returned by User {user_id}")
else:
    print("User or book not found or the book was not checked out by the user")



#comment

# we can also move checkout_book and return_book method to user class as well

#chat gpt

# Yes, you can logically place the checkout_book and return_book methods in the User class. It's a valid design choice, and it aligns with the principles of encapsulation in object-oriented programming. Here's how you could do it:
