# CSU Global Bookstore Points Program
# Program awards points based on the number of books purchased.

# Ask user for the number of books
books_str = input("Enter the number of books you purchased this month: ")

# Validate that input is digits (no negatives, no decimals)
if books_str.isdigit():
    books = int(books_str)

    # Use relational and Boolean logic to decide points
    if books == 0:
        points = 0
    elif books == 2:
        points = 5
    elif books == 4:
        points = 15
    elif books == 6:
        points = 30
    elif books >= 8:
        points = 60
    else:
        # Case when books = 1, 3, 5, or 7
        points = 0

    # Show results
    print(f"You purchased {books} books and earned {points} points.")
else:
    print("Please enter a valid whole number of books (0 or greater).")
