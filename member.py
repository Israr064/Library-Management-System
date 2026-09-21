# Member class:

# Attributes: member_id, name, borrowed_books (empty list se start ho, jitni books issue karega unme add hongi)
# Method display_info() jo member ki details print kare

class Member:
    def __init__(self,member_id,name):
        self.member_id = member_id
        self.name = name 
        self.borrowed_books = []

    def display_info(self):
        print(f"Member_ID = {self.member_id}")
        print(f"Name = {self.name}")
        print(f"Borrowed books = {self.borrowed_books}")


m1 = Member(123,"Ibrar")
m1.display_info()