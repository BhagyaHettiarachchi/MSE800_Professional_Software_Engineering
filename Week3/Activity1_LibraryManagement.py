#Add and Show books

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        self.books[title] = author
        print(f"Added: '{title}' by {author}")

    def show_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nBooks in Library:")
            for i, (title, author) in enumerate(self.books.items(), 1):
                print(f"{i}. {title} by {author}")

# Creating a Library object and using it
mini_library = Library()
mini_library.add_book("5AM Club", "Robin Sharma")
mini_library.add_book("Ikigai", "Hector")
mini_library.show_books()