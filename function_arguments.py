def save_car(brand, model, year, plate):
    print(f'Car successfully inserted! {brand}/{model}/{year}{plate}')

save_car('Fiat', 'Palio', 1999, 'ABC-1234')

save_car(brand='Fiat', model='Palio', year=1999, plate='ABC-1234')

save_car(**{'brand':'Fiat', 'model':'Palio', 'year':1999, 'plate':'ABC-1234'})

