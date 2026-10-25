# Задача:
# Тестирование гипотез о поведении клиентов (с использованием формулы Бернулли)
# Контекст: Компания тестирует новую функцию в своем сервисе. Предполагается, что вероятность использования новой
# функции пользователем равна 40% (p = 0.40).
# Вопрос: если мы случайным образом выберем 10 пользователей, какова вероятность того, что ровно 5 из них
# воспользуются новой функцией?

import math
import matplotlib.pyplot as plt


n = 10
p = 0.40
q = 1 - p


k_values = list(range(0, n + 1))
probabilities = []


for k in k_values:
    c_n_k = math.comb(n, k)
    prob = c_n_k * (p ** k) * (q ** (n - k))
    probabilities.append(prob)

print(f"Вероятность того, что ровно 5 пользователей воспользуются  новой функцией: {probabilities[5]:.4f}")



plt.figure(figsize=(10, 6))
bars = plt.bar(k_values, probabilities, color='skyblue', edgecolor='black', alpha=0.8)


target_k = 5
bars[target_k].set_color('forestgreen')
bars[target_k].set_edgecolor('black')


for bar in bars:
    height = bar.get_height()
    if height > 0.001:
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.005,
            f'{height:.4f}',
            ha='center',
            va='bottom',
            fontsize=9,
        )

plt.title('Распределение Бернулли (n = 10, p = 0.40)', fontsize=16, pad=15)
plt.xlabel('Количество пользователей, воспользовавшихся новой функцией', fontsize=11)
plt.ylabel('Вероятность P(k)', fontsize=11)

plt.xticks(k_values)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.ylim(0, max(probabilities) + 0.04)

plt.show()
