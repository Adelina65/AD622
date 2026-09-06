# # print(5+3)
# # print(5 -3)
# # age = 20.2
# # print(age, type(age), id(age))
# #
# # import keyword
# # print(keyword.kwlist)
# # a = 1
# # b = 2
# # c = a
# # a=b
# # b=c
# # print(a, b)
# #
# # num = 987654
# # one = num % 10 *1000000
# # num = num // 10
# # print(one)
#
# # prince = 99
# # print(prince)
#
# phone_price = 50000 # цена телефона
# case_price = 1500 # цена чехла
# phone_count = 2 # количество покупаемых телефонов
# case_count = 3 # количество покупаемых чехлов
# user_balance = 105000 # баланс денег на карте клиента
# # Посчитайте общую стоимость телефонов.
# # Посчитайте общую стоимость чехлов.
# # Посчитайте итоговую сумму заказа (сумму всех телефонов и чехлов).
# # Примените скидку: магазин дарит скидку 10% на всю покупку,
# #  если общая сумма заказа превышает 80000. Посчитайте финальную стоимость с учетом возможной скидки.
#
# # print('И как что делать и почему \nпроверяю')
# # print("Привет,\t мир\t!")
# # сумма = 1 + 2 + 3 + 4 + 5 + \
# #         6 + 7 + 8 + 9 + 10
# # print(сумма)
#
# # print('Привет  роо нщт', "b xnj", sep = "!")
# # print('Привет  роо нщт', "b xnj", end = "   ")
#
# # secret = 8
# # guess = 8
# # if guess < secret:
# #   print("too low")
# # elif guess > 7:
# #   print("too high")
# # elif guess == secret:
# #   print("too right")
# # else:
# #    print("Вот так")
#
# # small = True
# # green = False
# # if small == "вишня" or small== "горошек":
# #   print("Вишня и горошек", True)
# # else:
# #   print("тыква", False)
#
# # name = "Аделя"
# # name = name.replace("А", "Л")  # Перезаписываем переменную новой копией
# # print(name)
#
# # I = 5
# # while I <= 8:
# #    print(I)
# #    I += 1
# #    if I == 8:
# #        break
#
#
# # print(lambda )
# #
# #
# # map func *iterable
# # filter
#
# # n= 'Adelinastashkevich'
# # a = n[4]
# # print(a)
#
#
# # text = "ID_94827_2026"
# # date = text[-4:]     # '2026' (последние 4 символа)
# # product_id = text[3:8] # '94827'
#
#
# stm = 3570
# chv = 3570 // 10
# print('Общая сумма = ', (stm + chv) / 4)

time = 5000
min= int(time // 60)
print= int((time - min) % 60)
print(min)

time = 5000

# 1. Находим полные минуты с помощью целочисленного деления
minutes = time // 60

# 2. Находим оставшиеся секунды с помощью остатка от деления
seconds = time % 60

# 3. Выводим результат на экран
print(minutes, "мин.", seconds, "сек.")