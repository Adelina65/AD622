
# Задача 1: Диаграмма рассеяния (Взаимосвязь чисел)
# Условие: Покажите взаимосвязь между общим счетом
#  (total_bill) и оставленными чаевыми (tip).
# Подсветите точки разными цветами в зависимости от пола (sex) клиента.
#  На основе датасета tips.

import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
plt.figure(figsize=(10,6))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex", palette="Set1")
plt.title('Взаимосвязь чисел')
plt.xlabel('Общий счет', fontsize=11)
plt.ylabel('Оставленные чаевые', fontsize=11)
plt.show()



# Задача 2: Ящик с усами (Распределение по категориям)
# Условие: Постройте график "ящик с усами" (boxplot),
# чтобы сравнить распределение общего счета (total_bill)
# между курящими (smoker) и некурящими клиентами. На основе датасета tips.


tips = sns.load_dataset("tips")
plt.figure(figsize=(10,6))
sns.boxplot(data=tips, x="smoker", y="total_bill", palette="Set2")
plt.title('Распределение по категориям между курящими и некурящими клиентами')
plt.xlabel('Курящий клиент (smoker)', fontsize=11)
plt.ylabel('Общий счет (total_bill)', fontsize=11)
plt.show()



# Задача 3 Задача 3: Матрица корреляции и Тепловая карта (heatmap)
# Условие: Найдите корреляцию между всеми числовыми признаками
#  в датасете iris и визуализируйте её в виде тепловой карты.
# Выведите коэффициенты корреляции внутри ячеек и
# используйте контрастную цветовую палитру (например, coolwarm).

iris = sns.load_dataset('iris')
print(iris.head())
corr_matrix = iris.corr(numeric_only=True)
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Матрица корреляции и Тепловая карта')
plt.show()