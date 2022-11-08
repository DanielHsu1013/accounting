items = []
while True:
    name = input('Please enter item name:')
    if name == 'q':
        break
    price = input('Please enter the price:')
    items.append([name, price])
print(items)