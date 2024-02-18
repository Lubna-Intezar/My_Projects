# Define a dictionary to store book information
books = {
    "1": {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "copies": 2},
    "2": {"title": "Pride and Prejudice", "author": "Jane Austen", "copies": 1},
    "3": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "copies": 3},
}

# Define a dictionary to store borrowed books for each user
borrowed_books = {}

# Define functions for each operation

def view_books():
    """Displays information about available books."""
    print("Available Books:")
    for book_id, book_info in books.items():
        print(f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}, Copies: {book_info['copies']}")

def check_out_book(user_id):
    """Allows users to check out a book."""
    book_id = input("Enter book ID: ")
    if book_id in books:
        if books[book_id]["copies"] > 0:
            books[book_id]["copies"] -= 1
            borrowed_books.setdefault(user_id, []).append(book_id)
            print("Book checked out successfully!")
        else:
            print("Sorry, this book is not available.")
    else:
        print("Invalid book ID.")

def return_book(user_id):
    """Allows users to return a book."""
    book_id = input("Enter book ID to return: ")
    if book_id in borrowed_books.get(user_id, []):
        books[book_id]["copies"] += 1
        borrowed_books[user_id].remove(book_id)
        print("Book returned successfully!")
    else:
        print("You haven't borrowed this book.")

def view_borrowed_books(user_id):
    """Displays the list of books borrowed by the user."""
    if borrowed_books.get(user_id):
        print("Borrowed Books:")
        for book_id in borrowed_books[user_id]:
            print(f"ID: {book_id}, Title: {books[book_id]['title']}")
    else:
        print("You haven't borrowed any books.")

# Main program loop
while True:
    print("\nLibrary Management System")
    print("1. View Available Books")
    print("2. Check Out a Book")
    print("3. Return a Book")
    print("4. View Borrowed Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_books()
    elif choice == "2":
        user_id = input("Enter your user ID: ")
        check_out_book(user_id)
    elif choice == "3":
        user_id = input("Enter your user ID: ")
        return_book(user_id)
    elif choice == "4":
        user_id = input("Enter your user ID: ")
        view_borrowed_books(user_id)
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice.")

'''Explanation:

The books dictionary stores information about each book, including its ID, title, author, and available copies.
The borrowed_books dictionary keeps track of borrowed books for each user, with user IDs as keys and lists of book IDs as values.
Each function is defined with clear explanations of its purpose.
The view_books function displays information about all available books.
The check_out_book function allows users to choose a book, checks availability, updates the book dictionary, and adds the book to the user's borrowed list.
The return_book function allows users to return a book, updates the book dictionary, and removes it from the user's borrowed list.
The view_borrowed_books function displays the list of books borrowed by a specific user.
The main program loop provides a menu for users to interact with the system.'''