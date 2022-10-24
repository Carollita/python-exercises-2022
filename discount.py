product_price = float(input('Product Price: '))
discount = float(input('Product Discount: '))

discount_value = (product_price / 100) * discount
discount_product = product_price - discount_value

print(f'''
Product Price = {product_price}
Product Discount = {discount}
Discount Value = {discount_value}
Total Product Value With Discount = {discount_product}
''')