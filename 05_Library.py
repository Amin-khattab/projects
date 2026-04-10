class book:

    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def show_details(self):
        return f"{self.title} by {self.author}"
    
class library:

    def __init__(self):
        self.list_of_books = []
    
    def add_book(self,book):
        self.list_of_books.append(book)
        
    def show_books(self):
        print("the books we have are : \n\n")
        for book in self.list_of_books:
            if not book.is_borrowed:
                print(f"{book.show_details()}\n")

    def borrow_book(self,title):
        for book in self.list_of_books:
            print(book.title , book.is_borrowed)
            if book.title == title:
                print(book.title , book.is_borrowed)

                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"you have sessusfully borrowed {title}")
                    break
                else:
                    print("we dont have this book curuntily ")
                    break
        else:
            print("we dont have this book")
    
    def return_book(self,title):
        for book in self.list_of_books:
            if book.title == title:
                if book.is_borrowed == True:
                    book.is_borrowed = False
                    print(f"you have secsussfully returned {title}")
                    break
                else:
                    print("we have this book you cant return a book you havent taken")
                    break
        else:
            print("we never had this book ")


lib = library()

num_books = int(input("how many books do you have"))

for i in range(num_books):

    title = input("\nTitle: \n")
    author = input("Author: \n")

    book_i = book(title,author)

    lib.add_book(book_i)

lib.show_books()

borrow_book = input("which book do you want to borrow ? ")

lib.borrow_book(borrow_book)

return_book = input("which book do you want to return ? ")

lib.return_book(return_book)

