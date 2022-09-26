from books import books

#  number_of_authors(book) (function name) 
#  recieves a book dictionary (argument)
#  returns the number of authors that the book has (all the authors)
def number_of_authors(book):
    len(book["authors"]) # to check each element in an array
    return len(book["authors"]) # to save the value 
print(number_of_authors(books[0]))

#  get_book_by_id(book_id, books)
#  # receives a book id
#  # recieves a list of book dictionaries
#  # returns the book dictionary with the same id as the book_id provided

def get_book_by_id(book_id, books):
    for book in books: # to search for the id of the books
        if book_id == book["id"]: #
            return book 
print(get_book_by_id(38, books))


# add_summary_to_book(summary, book)
# receives a book dictionary
# recieves a summary string
# adds the summary to the book dictionary
# return the book dictionary
def add_summary_to_book(summary, book):
    summary_book = []
    for summary in book:
        summary_book.append(book) # to add a summary of the books in each element in the list 
    return summary_book


print(add_summary_to_book("this is a good book about", books[0]))


# CHALLENGE 1
# get_book_property(property, book)
# receives a book dictionary
# recieves a property (string)
# return the book property


def get_book_property(property, book):
    ...


print(get_book_property("color", books[0]))
print(get_book_property("title", books[0]))


# CHALLENGE 2
# calculate_available_books(books)
# receives a list of books
# return a new list of unavailable books


def calculate_not_available_books(books):
    ...


print(calculate_not_available_books(books))

# CHALLENGE 3
# get_book_by_author_name(author_name, books)
# receives a author name (string)
# recieves a list of book dictionaries
# returns the book dictionary that contains an author with the author name provided
def get_book_by_author_name(author_name, books):
    ...


print(get_book_by_author_name("Neil Gaiman", books))
