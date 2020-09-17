type = str(input("Введите фигуру: "))
if type == "треугольник":
        a = int(input("Введите сторону a = "))
        b = int(input("Введите сторону В = "))
        p = ((a *b)/2)
elif type == "Квадрат":
        a = int(input("Введите сторону а = "))
        p = (a ** 2)
print(p)