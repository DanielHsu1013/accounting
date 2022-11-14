items = []
while True:
    name = input('Please enter item name:')
    if name == 'q':
        break
    price = input('Please enter the price:')
    items.append([name, price])

for p in items:
    print('the price of', p[0], 'is', p[1], 'dollers' )

with open ('product.csv', 'w') as f:
    f.write('Item,Price\n' )
    for p in items:
        f. write (p[0] + ',' + p[1] + '\n')