import os
os.system("")

def main():
    menu_choice: str
    available_books: list[str] = return_available_books()
    borrowed_books: list[str] = []

    is_program_running = True
    
    while is_program_running:
        print("\n"*2)
        menu_choice = return_menu_choice()
        print("\n"*20)
        # Choose the correct function based on user input
        match menu_choice:
            case "1":
                display_available_and_borrowed_books(available_books, borrowed_books)
            case "2":
               available_books, borrowed_books = borrow_a_book(available_books, borrowed_books)
            case "3":
               available_books, borrowed_books = return_a_book(available_books, borrowed_books)
            case "4":
                print("Thank you for using the Library Borrowing Program")
                is_program_running = False
            
def return_available_books():
    return [
    "To Kill a Mockingbird",
    "1984",
    "Pride and Prejudice",
    "The Great Gatsby",
    "Moby-Dick",
    "War and Peace",
    "Crime and Punishment",
    "The Catcher in the Rye",
    "Brave New World",
    "The Lord of the Rings",
    "Jane Eyre",
    "Wuthering Heights",
    "The Hobbit",
    "Fahrenheit 451",
    "One Hundred Years of Solitude",
    "The Picture of Dorian Gray",
    "Anna Karenina",
    "Slaughterhouse-Five",
    "The Brothers Karamazov",
    "Les Misérables"
]

def find_int_choice(min_value: int, max_value: int) -> int:
    user_choice = input("Enter your choice =>")
    print(user_choice)

    correct_choices: list[str] = []
    for i in range(max_value):
        correct_choices.append(str(i+1))

    # Check for correct entry
    while not (user_choice in correct_choices):
        # RED = "\033[31m" RED +
        # RESET = "\033[0m" + RESET
        print(f"{user_choice} is an invalid menu entry.")
        user_choice = input("enter correct menu entry =>")
    return user_choice

def return_menu_choice() -> int:
    # Ask the user to enter their choice
    print("""1. Display available and borrowed books
2. Borrow a book
3. Return a book
4. Exit the program.
    """)
    menu_choice = find_int_choice(1, 4)
    return menu_choice

def display_available_and_borrowed_books(available_books: list[str],
                                         borrowed_books: list[str]):
    # Display the borrowed books
    print("List of Borrowed Books\n" + "="*22)
    for i in range(len(borrowed_books)):
        print(str(i+1) + f". {borrowed_books[i]}")

    print("\n"*2)

    # Display the available books
    print("List of Available Books\n" + "="*22)
    for i in range(len(available_books)):
        print(str(i+1) + f". {available_books[i]}")

def borrow_a_book(available_books: list[str],
                  borrowed_books: list[str]) -> tuple[list[str], list[str]]:
    print(f"Enter the number of book to borrow, or {len(available_books)+1} to exit.")
    for i in range(len(available_books)+1):
        print( (str(i+1) + ". " + available_books[i]) if i < len(available_books) else str(i+1) + ". Exit")        
    book_choice = find_int_choice(1, len(available_books)+1)
    if (book_choice == str(len(available_books)+1)):
        print("\n"*2)
        print("Exiting without borrowing a book...")
    else:
        print("\n"*2)
        print(f"Borrowing the following book: {available_books[int(book_choice) - 1]}")
        borrowed_books.append(available_books.pop(int(book_choice) - 1))

    return available_books, borrowed_books

def return_a_book(available_books: list[str],
                  borrowed_books: list[str]) -> tuple[list[str], list[str]]:
    print(f"Enter the number of book to return, or {len(borrowed_books)+1} to exit.")
    for i in range(len(borrowed_books)+1):
        print( (str(i+1) + ". " + borrowed_books[i]) if i < len(borrowed_books) else str(i+1) + ". Exit")        
    book_choice = find_int_choice(1, len(borrowed_books)+1)
    if (book_choice == str(len(borrowed_books)+1)):
        print("\n"*2)
        print("Exiting without returning a book...")
    else:
        print("\n"*2)
        print(f"Returning the following book: {borrowed_books[int(book_choice) - 1]}")
        available_books.append(borrowed_books.pop(int(book_choice) - 1))

    return available_books, borrowed_books

if __name__ == "__main__":
    main()


