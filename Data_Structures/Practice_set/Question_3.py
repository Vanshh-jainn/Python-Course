coordinates = (10, 20)
print(coordinates[0])
print(coordinates[1])

list_1 = list(coordinates)
list_1[0] = 50
coordinates = tuple(list_1)
print(coordinates)
