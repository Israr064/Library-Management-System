# Main file
from book import Book
from library import Library

Book1 = Book("Python","Peter",111)
Book2 = Book("C++","Peter",111)
Book3 = Book("Java","Peter",111)
Book4 = Book("HTML","Peter",111)

Lib1 = Library()

Lib1.add_book(Book1)
Lib1.add_book(Book2)
Lib1.add_book(Book3)
Lib1.add_book(Book4)

Lib1.show_books()
Lib1.display_all_books()