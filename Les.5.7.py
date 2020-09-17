import datetime
d=int(input("День"))
m=int(input("Месяц"))
y=int(input("Год"))
try:
    data=datetime.date(y,m,d)
    print(data)
    print("Дата существующая")
except:
    print("Такой даты нет")