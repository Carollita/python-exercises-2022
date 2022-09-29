option = 0

while option != 3:
    option = int(input('[1] Banana \n[2] Apple \n[3] Exit \n\nI would like to buy: '))

    if option == 1:
        print('You chose buy bananas!\n')
    elif option == 2:
        print('You chose buy apple!\n')
    elif option == 3:
        print('You finished your shopping at supermarket!\n')