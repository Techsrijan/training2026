class Book:
    # Class variable shared by all instances
    library_name = "Central City Library"

    def __init__(self, title, author, price):
        # Instance variables unique to each object
        self.title = title
        self.author = author
        self.price = price

    # 1. INSTANCE METHOD
    # Uses 'self' to access and modify unique object data
    def apply_discount(self, percentage):
        discount_amount = self.price * (percentage / 100)
        self.price -= discount_amount
        return f"New price of '{self.title}' is ₹{self.price:.2f}"

    # 2. CLASS METHOD
    # Uses 'cls' to work with class data or create new instances (Factory Method)
    @classmethod
    def change_library(cls, new_name):
        cls.library_name = new_name
        return f"Library system updated to: {cls.library_name}"

    @classmethod
    def from_csv_string(cls, csv_string):
        # Parses a string to create and return a new Book object
        title, author, price_str = csv_string.split(",")
        return cls(title.strip(), author.strip(), float(price_str))

    # 3. STATIC METHOD
    # Isolated utility function that does not need 'self' or 'cls'
    @staticmethod
    def is_valid_isbn(isbn_string):
        # Strips dashes and checks if the length is a standard 13 digits
        clean_isbn = isbn_string.replace("-", "")
        return len(clean_isbn) == 13


# ==========================================
# EXECUTION AND TESTING
# ==========================================

# --- Testing Static Method ---
# Called directly on the class without creating an object
print("--- Static Method Output ---")
print("Is valid ISBN?:", Book.is_valid_isbn("978-3-16-148410-0"))
print()

# --- Testing Class Method (Factory Constructor) ---
# Creates a new book instance using a formatted string
print("--- Class Method Output (Factory) ---")
csv_data = "Python Basics, John Doe, 499.00"
book1 = Book.from_csv_string(csv_data)
print(f"Created Book: '{book1.title}' by {book1.author}")
print()

# --- Testing Instance Method ---
# Modifies the specific data of the 'book1' object
print("--- Instance Method Output ---")
print(book1.apply_discount(10))  # Applies 10% discount to book1
print()

# --- Testing Class Method (State Modification) ---
# Changes a variable that impacts the entire class structure
print("--- Class Method Output (State Change) ---")
print(Book.change_library("Global Digital Library"))
# Confirming the change reflects on the individual instance
print(f"Book1 belongs to: {book1.library_name}")
