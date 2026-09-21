# Library class:

# Constructor mein ek empty list self.books = [] aur self.members = [] ho
# Method add_book(book) — jo ek Book object list mein add kare
# Method add_member(member) — jo ek Member object list mein add kare
# Method display_all_books() — jo saari books ki info loop se print kare (display_info() call karke)
# Method display_all_members() — jo saare members ki info loop se print kare
from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self,book):
       self.books.append(book)

    def addd_member(self,member):
        self.members.append(member)

    def display_all_books(self):
        num = 1
        for book in self.books:
            print(f"\nBook :{num}")
            num += 1
            book.display_info()

    def display_all_members(self):
        num = 1
        for member in self.members:
            print(f"\nMember :{num}")
            num += 1
            member.display_info()


b1 = Book("Python","Peter",1)
b2 = Book("C++", "Harry",2)
b3 = Book("Java", "Michel",3)
m1 = Member(1,"Israr")
m2 = Member(2,"Ibrar")
L1 = Library()
L1.add_book(b1)
L1.add_book(b2)
L1.add_book(b3)
L1.display_all_books()

L1.addd_member(m1)
L1.addd_member(m2)
L1.display_all_members()


    