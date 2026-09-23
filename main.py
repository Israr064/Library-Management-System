# Main file
from book import Book
from library import Library
from member import Member

Lib = Library()

while True:
    print("1. Add Book")
    print("2. Add Member")
    print("3. Display All Books")
    print("4. Display all Members")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Exit")

    choise = input("Enter choise: ")
 # Adding book
    if choise == "Add Book" or choise == "1" or choise == "add":
        title = input("Enter the title: ")
        author = input("Enter the Author: ")
        isbn = int(input("Enter book isbn: "))

        book = Book(title, author, isbn)
        Lib.add_book(book)

 # Adding member
    elif choise == "Add Member" or choise == "2":
        mem_id = int(input("Member Id: "))
        mem_name = input("Name: ")

        member = Member(mem_id, mem_name)
        Lib.add_member(member)

 # Displaying all books
    elif (choise == "Display All Books" or choise == "3"):
        Lib.display_all_books()

 # Displaying all members
    elif choise == "4" or choise == "Display All Members":
        Lib.display_all_members()

 # Issuing the book
    elif choise =="Issue book" or choise == "5":
        print("Add the Info to issue the book")
        b_isbn = int(input("Enter the Book isbn: "))
        b_m_id = int(input("Enter the member Id: "))
        try: 
            Lib.issue_book(b_isbn,b_m_id)
        except Exception as e: 
            print("Error",e)


 # Returing the book
    elif choise == "Return Book" or choise == "6":
        print("Add the info to return the book")
        i = int(input("Enter the Book isbn: "))
        mi = int(input("Enter the member Id: "))
        try: 
            Lib.return_book(i,mi)
        except Exception as e: 
            print("Error: ",e)

 # Exit

    elif choise == "Exit" or choise == "7":
        print("Goodbye!")
        break

    else: 
        print("Invalid choise.")
    




