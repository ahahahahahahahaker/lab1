import csv
#вариант 6
kol_z = 0
pr = 150
with open('books.csv') as fp:
    reader = csv.reader(fp,delimiter=';')
    rowcount = 0
    search = input('введите ФИО автора:\n')
    for row in reader:
        rowcount += 1
        for i in range(13):
            if len(row [i]) > 30:
                kol_z += 1
        name = row [4]
        price = row [7]
        if row [4] == search:
            price = price.replace('.',',')
            if int(price[0:3]) > pr:
                print(f'название: {row[1]}', f'цена: {row[7]}')
    print(f'кол-во записей:{kol_z}')
    print(f'количество строк:{rowcount}')
