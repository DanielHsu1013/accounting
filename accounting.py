items = []
while True:
    name = input('Please enter item name:')
    if name == 'q':
        break
    price = input('Please enter the price:')
    p = []
    p.append(name)
    p.append(price)
    items.append(p)
print(items)