def sum(a,b):
    print("Vansh jain is the best")
    c = a+b
    global z #please modify global z
    z = 3
    print(z)
    return c
z  = 1
print(z)
print(sum(3,5))