# Задача 1: продажи отделов магазина (Настройка цветов и сетки)
# Условие: Магазин продает три категории товаров: Электроника, Одежда и Книги. Данные разбиты по кварталам.
# Постройте график, задайте категории вручную с помощью списка цветов (colors) и включите фоновую сетку
# для удобства чтения.
# Исходные данные:
# •	quarters = ['Q1', 'Q2', 'Q3', 'Q4']
# •	electronics = [40, 55, 48, 70]
# •	clothing = [30, 45, 40, 65]
# •	books = [15, 20, 18, 25]


import matplotlib.pyplot as plt

quarters = ['Q1', 'Q2', 'Q3', 'Q4']
electronics = [40, 55, 48, 70]
clothing = [30, 45, 40, 65]
books = [15, 20, 18, 25]
plt.figure(figsize=(8, 5))
plt.plot(quarters, electronics, color='#34495e', label='Электроника', marker='o')
plt.plot(quarters, clothing, color='#f1948a', label='Одежда', marker='o')
plt.plot(quarters, books, color='#85c1e9', label='Книги', marker='o')
plt.title('Продажи отделов магазина', fontsize=14, fontweight='bold')
plt.xlabel('Кварталы', fontsize=12)
plt.ylabel('Продажи', fontsize=12)
plt.grid(axis='y', linestyle='-', alpha=0.5)
plt.legend()
plt.show()




# Задание 2. круговая диаграмма (Доли рынка смартфонов)
# Условие: У вас есть данные о долях рынка четырех популярных брендов смартфонов: Apple, Samsung, Xiaomi и Другие.
# Постройте простую круговую диаграмму, добавьте подписи к каждому сектору и выведите проценты внутри графика
# с округлением до одного знака после запятой.
#
# Данные: названия и их доли в процентах:
# •	brands = ['Apple', 'Samsung', 'Xiaomi', 'Другие']
# •	market_share = [30, 25, 20, 25]



brands = ['Apple', 'Samsung', 'Xiaomi', 'Другие']
market_share = [30, 25, 20, 25]
plt.pie(
    market_share,
    labels=brands,
    autopct='%1.1f%%',
    colors=['red', 'green', 'blue', 'yellow']
)
plt.title('Доли рынка смартфонов')
plt.show()