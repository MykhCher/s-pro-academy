from django.shortcuts import render
from django.http import HttpRequest, HttpResponseNotFound

books = [
    {'id': 1,
    'title': 'Fluent Python',
    'released_year': 2015, 
    'description': 'Python’s simplicity lets you become productive quickly, but this often means you aren’t using everything it has to offer. With this hands-on guide, you’ll learn how to write effective, idiomatic Python code by leveraging its best—and possibly most neglected—features. Author Luciano Ramalho takes you through Python’s core language features and libraries, and shows you how to make your code shorter, faster, and more readable at the same time.',
    'author_id': 1
    },

    {'id' : 2,
    'title' : 'The Hobbit: or There and Back Again',
    'released_year' : 1937,
    'description': 'The bedtime story for his children famously begun on the blank page of an exam script that tells the tale of Bilbo Baggins and the dwarves in their quest to take back the Lonely Mountain from Smaug the dragon.',
    'author_id': 2
    },

    {'id' : 3,
    'title' : 'The Fellowship of the Ring',
    'released_year' : 1954,
    'description' : 'One of the world’s most famous books that continues the tale of the ring Bilbo found in The Hobbit and what comes next for it, him, and his nephew Frodo.',
    'author_id' : 2
    },

    {'id' : 4,
    'title' : 'The Two Towers',
    'released_year' : 1954,
    'description' : 'The continuation of the story begun in The Fellowship of the Ring as Frodo and his companions continue their various journeys.',
    'author_id' : 2
    },

    {'id' : 5,
    'title' : 'The Return of the King',
    'released_year' : 1955,
    'description' : 'The conclusion to the story that we began in The Fellowship of the Ring and the perils faced by Frodo et al.',
    'author_id' : 2
    },

    {'id' : 6,
    'title' : 'A Tragedy of Hamlet, Prince of Denmark',
    'released_year' : 1603,
    'description' : 'Hamlet is considered among the most powerful and influential works of world literature, with a story capable of "seemingly endless retelling and adaptation by others".[1] It was one of Shakespeare’s most popular works during his lifetime',
    'author_id' : 3
    },

    {'id' : 7,
    'title' : 'Romeo and Juliet',
    'released_year' : 1595,
    'description' : 'A tragedy written by William Shakespeare early in his career about two young Italian star-crossed lovers whose deaths ultimately reconcile their feuding families. It was among Shakespeare’s most popular plays during his lifetime and, along with Hamlet, is one of his most frequently performed plays.',
    'author_id' : 3
    }
 ]

authors = [
    {'id' : 1,
    'first_name' : 'Luciano',
    'last_name' : 'Ramalho',
    'age' : 51
    },

    {'id' : 2,
    'first_name' : 'John',
    'last_name' : 'Tolkien',
    'age' : 82},

    {'id' : 3,
    'first_name': 'William',
    'last_name' : 'Shakespeare',
    'age' : 52}
]

def book_list(request):
    return render(request, 'book_list.html', context={'books' : books})

def book_detail(request, book_id):
    try:
        book = books[int(book_id)-1]
        return render(request, "book_details.html", context = book)
    except:
        return HttpResponseNotFound(f"not found {book_id = }")


def author_detail(request, auth_id):
    try:
        auth = authors[int(auth_id)-1]
        return render(request, "auth_details.html", context = auth)
    except:
        return HttpResponseNotFound(f"not found {auth_id = }")

def book_authlist(request, auth_id):
    bookByAuth = list()
    for book in books:
        if book['author_id'] == int(auth_id):
            bookByAuth.append(book)
    return render(request, 'books_authlist.html', context={'books' : bookByAuth})
    