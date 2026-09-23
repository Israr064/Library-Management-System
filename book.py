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
        status = "Issued" if self.is_issued else "Avaliable"
        print(f"Title: {self.title} | Author: {self.author} | Isbn: {self.isbn} | Status: {status}")

    def to_dict(self):
        return {"title": self.title, "author": self.author, "isbn": self.isbn, "is_issued": self.is_issued}

        


