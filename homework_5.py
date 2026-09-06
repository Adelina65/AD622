def rectangle():
    a = float(input("Введите сторону A: "))
    b = float(input("Введите сторону B: "))
    print("Площадь:", a * b)

def triangle():
    c = float(input("Введите основание: "))
    d = float(input("Введите высоту: "))
    print("Площадь:", 0.5 * c * d)

def circle():
    r = float(input("Введите радиус: "))
    print("Площадь:", 3.14 * r * r)


vybor = input("Выберите фигуру: если 1 - значит прямоугольник, если 2 - значит треугольник, если 3 значит круг): ")

if vybor == "1":
    rectangle()
elif vybor == "2":
    triangle()
elif vybor == "3":
    circle()
else:
    print("Неверный ввод")