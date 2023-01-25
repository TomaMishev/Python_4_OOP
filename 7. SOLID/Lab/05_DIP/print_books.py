# We want to print books, but before printing the book, we should format it. To accomplish this, we have a class
# Printer that can print books and a class Formatter which is used by the Printer. Refactor the provided code that
# breaks the DIP because both Printer and Formatter depend on concretions, not abstractions, by creating abstractions
# and injecting them wherever needed.


class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class Printer:
    @staticmethod
    def get_book(book: Book, formatter):
        formatted_book = formatter.format(book)
        return formatted_book


book = Book("Content")
formatter = Formatter()
printer = Printer()

print(printer.get_book(book, formatter))
