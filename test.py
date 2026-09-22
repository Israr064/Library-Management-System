# Testing the Code
from book import Book
from member import Member
from library import Library

Lib = Library

B1 = Book("Programing", "Bilal Ahmed", 101)
B2 = Book("EPM", "Bilal Ahmed", 102)
B3 = Book("Isl", "Bilal Ahmed", 103)

M1 = Member(1,"Israr")
M2 = Member(2,"Ibrar")


Lib = Library()

books = [B1,B2,B3]
for b in books:
    Lib.add_book(b)

members = [M1,M2]
for member in members:
    Lib.add_member(member)

Lib.display_all_books()
Lib.display_all_members()