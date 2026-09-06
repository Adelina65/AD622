sales_data = {
    "John":  {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
    "Tom":   {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
    "Anne":  {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
    "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}
}

name = input("Введите имя: ")
region = input("Введите регион: ")

current_value = sales_data[name][region]
print(current_value)

new_value = int(input("Введите новое значение: "))
sales_data[name][region] = new_value
print(sales_data[name])
