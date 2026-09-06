count = int(input("Укажите количество символов: "))
char_type = input("Укажите тип символа: ")
orientation = int(input("Ориентация линии (0 - горизонтальная, 1 - вертикальная): "))

i = 0
while i < count:
    if orientation == 0:
        print(char_type, end="")
    else:
        print(char_type)
    i += 1


if orientation == 0:
    print()

