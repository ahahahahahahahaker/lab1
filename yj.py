import csv
#вариант 6
kol_z = 0
pr = 150
with open('books.csv') as fp:
    reader = csv.reader(fp,delimiter=';')
    rowcount = 0
    search = input('введите ФИО автора:\n')
    next(reader)
    for row in reader:
        rowcount += 1
        for i in range(13):
            if len(row [i]) > 30:
                kol_z += 1
        name = row [4]
        price = row [7]
        if search == name and float(price) > pr:
                print(f'название: {row[1]}\nцена: {price}')
    print(f'кол-во записей:{kol_z}')
    print(f'количество строк:{rowcount}')
