# Positional Arguments
def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8

# Default Arguments
def addition(a,b,plus=0):
    return(a+b+plus)

c = addition(3,4) #here plus is default parameter we dont need to pass an argument for it.
print(c)
d = addition(6,6,2) #here we overwrote the default argument.
print (d)


# Keyword argument

e = add(b = 4,a = 5) # here we can pass the arguments in specific order.
print(e)