# Member class:

# Attributes: member_id, name, borrowed_books (empty list se start ho, jitni books issue karega unme add hongi)
# Method display_info() jo member ki details print kare

class Member:
    def __init__(self,member_id,name):
        self.member_id = member_id
        self.name = name 
        self.borrowed_books = []

    def display_info(self):
        book_titles = [book.title for book in self.borrowed_books]
        print(f"ID: {self.member_id} | Name: {self.name} | Borrowed Books: {book_titles}")
