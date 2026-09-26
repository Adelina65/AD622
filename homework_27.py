# Задание 1. Сравнение двух температурных рядов
# Условие:
# Имеются данные о температуре за 5 дней недели (понедельник — пятница):
# •	Город А: [20, 22, 19, 23, 25]
# •	Город Б: [15, 17, 18, 16, 21]
# Постройте на одной координатной плоскости два линейных графика: для Города А
#  (красная сплошная линия с маркерами в виде точек) и Города Б
#  (зеленая штрихпунктирная линия с маркерами-квадратами).
# Обязательно добавьте легенду.

from matplotlib import pyplot as plt

days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт']
temperature_city_a = [20, 22, 19, 23, 25]
temperature_city_b = [15, 17, 18, 16, 21]
fig, ax = plt.subplots()
ax.plot(days, temperature_city_a, color='red', linestyle='-', marker='o', label='Город А')
ax.plot(days, temperature_city_b, color='green', linestyle='-.', marker='s', label='Город Б')
ax.set_xlabel('День недели', fontweight='bold')
ax.set_ylabel('Температура', fontweight='bold')
ax.set_title('Динамика температуры за неделю', fontweight='bold')
ax.legend()
plt.show()



# Задание 2. Отображение прибыли компании и выделение лучшего месяца
# Условие:
# Даны показатели прибыли компании (в тыс. рублей) за первое полугодие: [120, 150, 90, 210, 180, 250].
# Постройте линейный график. Окрасьте линию в фиолетовый цвет, увеличьте её толщину до 3. Отдельно выделите точку с
# максимальной прибылью крупным красным маркером.


profit = [120, 150, 90, 210, 180, 250]
month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь']
fig, ax = plt.subplots()
ax.plot(month, profit, color='violet', linestyle='-', linewidth=3)
max_month = 'Июнь'
max_profit = 250
ax.plot(max_month, max_profit, color='red', marker='o', markersize=11, label='Максимальная прибыль')
ax.set_xlabel('Первое полугодие', fontweight='bold')
ax.set_ylabel('Прибыль компании (тыс.руб.)', fontweight='bold')
ax.legend()
plt.show()

# или

profit = [120, 150, 90, 210, 180, 250]
month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь']
fig, ax = plt.subplots()
ax.plot(month, profit, color='violet', linestyle='-', linewidth=3)
max_profit = max(profit)
max_month = month[profit.index(max_profit)]
ax.plot(max_month, max_profit, color='red', marker='o', markersize=11, label='Максимальная прибыль')
ax.set_xlabel('Первое полугодие', fontweight='bold')
ax.set_ylabel('Прибыль компании (тыс.руб.)', fontweight='bold')
ax.legend()
plt.show()