circle_shape = lambda r: 3.14159 * r**2
rect_shape = lambda w, h: w * h
trap_shape = lambda a, b, h: 0.5 * (a + b) * h

s_circle = circle_shape(2)
s_rect = rect_shape(10, 13)
s_trap = trap_shape(7, 5, 3)

print("Площадь окружности (r=2):", s_circle)
print("Площадь прямоугольника (10x13):", s_rect)
print("Площадь трапеции (a=7, b=5, h=3):", s_trap)