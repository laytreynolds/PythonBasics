# QA Homework

def find_author(book):
    books = {"Margaret Atwood":["The Handmaid's Tale", "The Blind Assassin"], "J.R.R. Tolkien":["The Hobbit", "The Lord Of The Rings", "The Silmarillion"], "Roald Dahl":["Charlie And The Chocolate Factory", "Matilda"]}
    booktitle = ' '.join([word.capitalize() for word in book.split()])
    for author in books:
        if booktitle in books[author]:
            return f"{author} wrote {booktitle}"
        else:
            continue
    return "Book not found"
title = input("Enter a book title: ")
print(find_author(title))