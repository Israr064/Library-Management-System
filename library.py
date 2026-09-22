# Library class:

# Constructor mein ek empty list self.books = [] aur self.members = [] ho
# Method add_book(book) — jo ek Book object list mein add kare
# Method add_member(member) — jo ek Member object list mein add kare
# Method display_all_books() — jo saari books ki info loop se print kare (display_info() call karke)
# Method display_all_members() — jo saare members ki info loop se print kare
from member import Member
from book import Book

class Library:
    def __init__(self):
        self.books = []
        self.members = []

 # Adding books in list 
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library.")


 # Adding members in list       
    def add_member(self,member):
        self.members.append(member)
        print(f"Name: {member.name} is added to library")
 

    def display_all_books(self):
        num = 1
        print("\n --- ALL Books ---")
        for book in self.books:
            print(f"Book {num}: ")
            num += 1
            book.display_info()

    def display_all_members(self):
        print("\n --- ALL Members ---")
        num = 1
        for member in self.members:
            print(f"Member {num}:")
            num += 1
            member.display_info()



