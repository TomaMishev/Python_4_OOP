# Refactor the provided code, so there is a separate class called Library, which contains books and has a method
# called find_book(title) that returns the book with the given title. Remove the unnecessary code from the Book class.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books = []

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book

    def add_book(self, book: Book):
        self.books.append(book)
