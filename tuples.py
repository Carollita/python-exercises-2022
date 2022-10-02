pokemon_evolution = ('Gastly', 'Haunter', 'Gengar',) 
# ('Gastly', 'Haunter', 'Gengar')

fruit = tuple('grape')
# ('g', 'r', 'a', 'p', 'e')     

cooking_ingredients = tuple(['Olive oil', 'Egg', 'Tomato',])
# ('Olive oil', 'egg', 'tomato')

print(f'''
{pokemon_evolution}
{fruit}
{cooking_ingredients}
''')

# Access Tuple Items

print(cooking_ingredients[0])
# Olive oil

print(cooking_ingredients[-1])
# return last item (Tomato)