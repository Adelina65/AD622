mathematics = {'Matvei', 'Evgeniya', 'Michail', 'Maxim', 'Natalia'}
physics = {'Matvei','Maxim', 'Alexander'}

all = mathematics | physics
print(all)

both = mathematics & physics
print(both)

mathematics = both
del physics
print(mathematics)