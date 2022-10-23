books = {'Buddenbrooks', 'The Grapes of Wrath', 'Crime and Punishment', 'Dracula', 'Les Miserables'}

favorite_books = {'Crime and Punishment', 'Les Miserables', 'The Little Prince', 'The Catcher in the Rye'}

union_books = books.union(favorite_books)
print(union_books)
# {'The Grapes of Wrath', 'Crime and Punishment', 'Buddenbrooks', 'Les Miserables', 'Dracula', 'The Little Prince', 'The Catcher in the Rye'}

intersection_books = books.intersection(favorite_books)
print(intersection_books)
# {'Les Miserables', 'Crime and Punishment'}

difference_books = books.difference(favorite_books)
print(difference_books)
# {'The Grapes of Wrath', 'Dracula', 'Buddenbrooks'}

difference_books = favorite_books.difference(books)
print(difference_books)
# {'The Catcher in the Rye', 'The Little Prince'} 

symmetric_difference_books = books.symmetric_difference(favorite_books)
print(symmetric_difference_books)
# {'The Catcher in the Rye', 'Dracula', 'The Little Prince', 'Buddenbrooks', 'The Grapes of Wrath'}


books = {'Crime and Punishment', 'Les Miserables', 'The Catcher in the Rye'}

favorite_books = {'Crime and Punishment', 'Les Miserables', 'The Little Prince', 'The Catcher in the Rye', 'Buddenbrooks', 'Dracula'}

issubset_books = books.issubset(favorite_books)
print(issubset_books)
# True

issubset_books = favorite_books.issubset(books)
print(issubset_books)
# False

issuperset_books = books.issuperset(favorite_books)
print(issuperset_books)
# False 

issuperset_books = favorite_books.issuperset(books)
print(issuperset_books)
# True

books = {'Crime and Punishment', 'Les Miserables', 'The Catcher in the Rye'}

favorite_books = {'The Little Prince', 'Buddenbrooks', 'Dracula'}

books_to_read = {'Dracula'}

isdisjoint_books = books.isdisjoint(favorite_books)
print(isdisjoint_books)
# True

isdisjoint_books = favorite_books.isdisjoint(books_to_read)
print(isdisjoint_books)
# False