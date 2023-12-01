def bookworm(books):
    for book in books:
        if book[0]=='A':
            print(book)

#Test your function with this input
books = ["Harry Potter", "The Hitchhiker's Guide to the Galaxy", "A Brief History of Time", "The Great Gatsby", "Atlas Shrugged"]
bookworm(books)