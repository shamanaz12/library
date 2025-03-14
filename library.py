import csv
import os
import pandas as pd

class Library:
    def __init__(self, filename="books.csv"):
        self.filename = filename
        self.load_books()

    def load_books(self):
        """Load books from CSV file or create new file"""
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Title", "Author", "Year", "Published Year", "Views"])
        self.books = pd.read_csv(self.filename).to_dict(orient="records")

    def save_books(self):
        """Save books to CSV file"""
        df = pd.DataFrame(self.books)
        df.to_csv(self.filename, index=False)

    def add_book(self, title, author, year, published_year, views):
        """Add a new book to the library"""
        self.books.append({
            "Title": title,
            "Author": author,
            "Year": year,
            "Published Year": published_year,
            "Views": views
        })
        self.save_books()
        print(f"📖 '{title}' added to the library!")

    def view_books(self):
        """Display all books in the library"""
        if not self.books:
            print("📚 Library is empty! Add some books first.")
            return
        print("\n📚 Your Personal Library:")
        for idx, book in enumerate(self.books, 1):
            print(f"{idx}. {book['Title']} - {book['Author']} ({book['Year']}), "
                  f"Published: {book['Published Year']}, Views: {book['Views']}")

    def search_book(self, title):
        """Search for a book by title"""
        found_books = [book for book in self.books if book["Title"].lower() == title.lower()]
        if found_books:
            for book in found_books:
                print(f"✅ Found: {book['Title']} by {book['Author']} ({book['Year']}), "
                      f"Published: {book['Published Year']}, Views: {book['Views']}")
        else:
            print(f"❌ '{title}' not found!")

    def delete_book(self, title):
        """Delete a book from the library"""
        for book in self.books:
            if book["Title"].lower() == title.lower():
                self.books.remove(book)
                self.save_books()
                print(f"🗑️ '{title}' deleted from the library!")
                return
        print(f"❌ '{title}' not found!")

# 🟢 Run the Library System
if __name__ == "__main__":
    my_library = Library()
    
    while True:
        print("\n📚 Personal Library System 📚")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter book year: ")
            published_year = input("Enter published year: ")
            views = input("Enter number of views: ")
            my_library.add_book(title, author, year, published_year, views)
        
        elif choice == "2":
            my_library.view_books()
        
        elif choice == "3":
            title = input("Enter book title to search: ")
            my_library.search_book(title)
        
        elif choice == "4":
            title = input("Enter book title to delete: ")
            my_library.delete_book(title)
        
        elif choice == "5":
            print("📚 Exiting... Goodbye!")
            break
        
        else:
            print("❌ Invalid choice! Please enter a valid option.")
