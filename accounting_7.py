#read file
items = []
with open ('product.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if '品項,價格' in line:
            continue
        name, price = line.strip().split(',')
        items.append([name, price])  
print (items)

#user input
items = []
while True:
    name = input('Please enter item name:')
    if name == 'q':
        break
    price = input('Please enter the price:')
    items.append([name, price])
print(items)

#print accounting record
for p in items:
    print('the price of', p[0], 'is', p[1], 'dollers' )

#write the accounting record into csv file
with open ('product.csv', 'w', encoding='utf-8') as f:
    f.write('品項,價格\n' )
    for p in items:
        f. write (p[0] + ',' + p[1] + '\n')