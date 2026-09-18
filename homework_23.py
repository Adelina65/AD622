# Создать одномерный массив из 5-ти нулей
import numpy as np
zeros = np.zeros(5) # float
print(zeros)

zeros = np.zeros(5, dtype = 'int32') # int
print(zeros)

# Создать массив из 3х4 единиц
ones = np.ones((3, 4))
print(ones)

ones = np.ones((3, 4), dtype = 'int32')
print(ones)