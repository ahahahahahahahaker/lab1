import csv
#вариант 6
k=0
with open('books.csv') as fp:
    reader = csv.reader(fp,delimiter=';')
    rowcount  = 0
    print('введите ФИО автора:')
    a=input()
    for row in reader:
        rowcount+= 1
        n=0
        for i in range(13):
            if len(row[i])>30:
                k+=1
        if row[4]==a:
            row[7]=row[7].replace('.',',')
            if int(row[7][0:3])>150:
                print('название:',row[1], 'цена:',row[7])
    print('кол-во записей:', k)
    print("количество строк:", rowcount)
