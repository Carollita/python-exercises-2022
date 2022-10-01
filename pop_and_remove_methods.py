programming_languages = ['python', 'java', 'javaScript', 'c++', 'C#']

print(programming_languages.pop()) # C#
print(programming_languages.pop()) # c++
print(programming_languages.pop(0)) # python
print(programming_languages) # ['java', 'javaScript']

programming_languages.remove('javaScript')
print(programming_languages) # ['java']