# 1-ый способ
num = 97531
print('Исходное число:', num)
res = num % 10 * 10000
num = num // 10
res += num % 10 * 1000
num = num // 10
res += num % 10 * 100
num = num // 10
res += num % 10 * 10
num = num // 10
res += num % 10
print('Обратное число:', res)

# 2-ой способ
num = 97531
print('Исходное число:', num)
one = num % 10
num = num // 10
two = num % 10
num = num // 10
three = num % 10
num = num // 10
four = num % 10
num = num // 10
five = num % 10
num = num // 10
res = one *10000 + two *1000 + three *100 + four *10 + five
print("Обратное число:", res)

# произведение цифр числа 97531

num = 97531
one = num % 10
num = num // 10
two = num % 10
num = num // 10
three = num % 10
num = num // 10
four = num % 10
num = num // 10
five = num % 10
num = num // 10
res = one * two * three * four * five
print("Произведение цифр числа 97531:", res)

# среднее арифметическое числа 97531

num = 97531
one = num % 10
num = num // 10
two = num % 10
num = num // 10
three = num % 10
num = num // 10
four = num % 10
num = num // 10
five = num % 10
num = num // 10
print(one,two,three, four, five)
res = (one + two + three + four + five) / 5
print("Среднее арифметическое числа 97531:", res)


