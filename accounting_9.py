import os #operate system

#read file
def read_file(filename):
    items = []
    with open (filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '品項,價格' in line:
                continue
            name, price = line.strip().split(',')            
            items.append([name, price])
    return items

#user input
def user_input(items):
    items = []
    while True:
        name = input('Please enter item name:')
        if name == 'q':
            break
        price = input('Please enter the price:')
        #price = int(price)
        items.append([name, price])
    print(items)
    return items

#print accounting record
def print_product(items):
    for p in items:
        print('the price of', p[0], 'is', p[1], 'dollers' )

#write the accounting record into csv file
def write_file(filename, items):
    with open (filename, 'w', encoding='utf-8') as f:
        f.write('品項,價格\n' )
        for p in items:
            f. write (p[0] + ',' + p[1] + '\n')

#main functiuon
def main():
    filename = 'product.csv'
    if os.path.isfile(filename):
        print('the file is exist')
        items = read_file(filename)
    else:
        print('the file is not found')

    #items = read_file('product.csv')
    items = user_input(items)
    print_product(items)
    write_file('product.csv', items)


main()