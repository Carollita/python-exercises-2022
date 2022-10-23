authors = {'Victor Hugo', 'Lewis Carroll', 'Vladimir Nabokov'}

# Add
authors.add('Fyodor Dostoyevsky')
authors.add('Victor Hugo')
print(authors)
# {'Lewis Carroll', 'Victor Hugo', 'Fyodor Dostoyevsky', 'Vladimir Nabokov'}

# Copy
authors_list = authors.copy()
print(authors_list)
# {'Lewis Carroll', 'Vladimir Nabokov', 'Victor Hugo', 'Fyodor Dostoyevsky'}

# Discard
authors_list.discard('Vladimir Nabokov')
authors_list.discard('Charles Dickens')
print(authors_list)
# {'Lewis Carroll', 'Fyodor Dostoyevsky', 'Victor Hugo'}

# Remove
authors_list.remove('Lewis Carroll')
print(authors_list)
# {'Victor Hugo', 'Fyodor Dostoyevsky'}
# if the element does not exist, the remove command gives an error, the discard command does not

# Pop
authors_list.pop()
print(authors_list)
# remove first index element

# Clear
authors_list.clear()
print(authors_list)
# {}

# Len
print(len(authors))
# 4
print(len(authors_list))
# 0

# In
print('Charles Dickens' in authors) # False
print('Victor Hugo' in authors) # True