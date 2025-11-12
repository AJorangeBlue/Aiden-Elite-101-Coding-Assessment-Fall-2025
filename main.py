from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author

# '''
# (Citation: GitHub's copilot) I asked for help on
# how to call the books that were available or  if the availability is True 

def viewBooks():
    avail_Books = []
    for books in library_books:
        if books["available"] == True:
            avail_Books.append(
                {
                    "id": books["id"],
                    "title": books["title"],
                    "author": books["author"]
                })
    return avail_Books

# print(viewBooks())


# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

"""
Citation: W3school's python string .strip() to remove unnecessary spaces.
Mimo.org for the 'in' operator
GitHub's Copliot for why my function didn't return anything
"""

def search_Anything(search_bar):
    search_results = []
    #search_bar = input("Search up an author or a genre: ").strip().lower()
    for item in library_books:
        if (search_bar in item["author"].lower() or search_bar in item['genre'].lower()):
            search_results.append(item)
            #print() - delete this line later
            

    return search_results
    
search_bar = input("Search up an author or a genre: ").strip().lower()
print(search_Anything(search_bar))




#print(searchAny()) # Remove this line before showing


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    pass
