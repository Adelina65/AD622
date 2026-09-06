import random


def generate_random_tuple(min_val, max_val):
    return tuple(random.randint(min_val, max_val) for _ in range(10))


tuple1 = generate_random_tuple(0, 5)
tuple2 = generate_random_tuple(-5, 0)
tuple3 = tuple1 + tuple2
zero_count = tuple3.count(0)


print("Третий кортеж:", tuple3)
print("Количество нулей в нем:", zero_count)