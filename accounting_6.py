items = []
while True:
    name = input('Please enter item name:')
    if name == 'q':
        break
    price = input('Please enter the price:')
    items.append([name, price])

for p in items:
    print('the price of', p[0], 'is', p[1], 'dollers' )

with open ('product.csv', 'w', encoding='utf-8') as f:
    f.write('品項,價格\n' )
    for p in items:
        f. write (p[0] + ',' + p[1] + '\n')