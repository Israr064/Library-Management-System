# Book class:

# Attributes: title, author, isbn (unique id), is_issued (default False)
# Method display_info() jo book ki details print kare

class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_issued = False

    def display_info(self):
        print(f"Title = {self.title}")
        print(f"Author = {self.author}")
        print(f"Isbn = {self.isbn}")
        


B1 = Book("Python","Israr",1043)
B1.display_info()
