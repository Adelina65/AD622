# 1-ый способ
number_of_crows = int(input("Введите количество ворон в диапазоне от 0 до 9: "))
if number_of_crows == 1:
    print("На ветке", number_of_crows, "ворона")
elif number_of_crows < 0 or number_of_crows > 9:
    print("Ошибка: введено неверное число!")
elif number_of_crows == 2 or number_of_crows == 3 or number_of_crows == 4:
    print("На ветке", number_of_crows, "вороны")
else:
    print("На ветке", number_of_crows, "ворон")

# 2-ой способ
number_of_crows = int(input("Введите количество ворон в диапазоне от 0 до 9: "))
if number_of_crows == 1:
    print("На ветке", number_of_crows, "ворона")
elif 2 <= number_of_crows <= 4:
    print("На ветке", number_of_crows, "вороны")
elif number_of_crows < 0 or number_of_crows > 9:
    print("Ошибка: введено неверное число!")
else:
    print("На ветке", number_of_crows, "ворон")