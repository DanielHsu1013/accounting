items = []
while True:
    name = input('Please enter item name:')
    if name == 'q':
        break
    price = input('Please enter the price:')
    items.append([name, price])

for p in items:
    print('the price of', p[0], 'is', p[1], 'dollers' )
