import json

# File to store books
data_file = "library.json"

# Load existing library data
def load_library():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save library data
def save_library(library):
    with open(data_file, "w") as file:
        json.dump(library, file, indent=4)

# Add a book
def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = int(input("Enter publication year: "))
    genre = input("Enter genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    save_library(library)
    print("Book added successfully!")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    library = [book for book in library if book["title"].lower() != title.lower()]
    save_library(library)
    print("Book removed successfully!")
    return library

# Search for a book
def search_book(library):
    query = input("Enter book title or author to search: ").lower()
    results = [book for book in library if query in book["title"].lower() or query in book["author"].lower()]
    if results:
        for book in results:
            print_book(book)
    else:
        print("No matching books found.")

# Display all books
def display_books(library):
    if not library:
        print("Library is empty.")
    else:
        for book in library:
            print_book(book)

# Display book details
def print_book(book):
    print(f"\nTitle: {book['title']}\nAuthor: {book['author']}\nYear: {book['year']}\nGenre: {book['genre']}\nRead: {'Yes' if book['read'] else 'No'}\n")

# Display statistics
def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percent_read = (read_books / total_books * 100) if total_books > 0 else 0
    print(f"Total Books: {total_books}\nRead Books: {read_books}\nPercentage Read: {percent_read:.2f}%")

# Main menu
def main():
    library = load_library()
    while True:
        print("\nPersonal Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(library)
        elif choice == "2":
            library = remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()