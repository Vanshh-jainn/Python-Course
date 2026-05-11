a = 34
b= 3
#Arithmetic operators
print("a + b =", a+b)
print("a - b =", a-b)
print("a * b =", a*b)
print("a / b =", a/b)
print("a % b =", a%b)
print("a // b =", a//b) #its called float divide, ignores decimal value.
print()

#Conditional Operators
print(a>4)
print(a<4)
print(a>=4)
print(a<=34)
print(a==34)
print(a!=34)
print()

#Logical Operators
print(True and False)  # Output: False , and have priority False.
print(True or False)   # Output: True,  or have priority True.
print(not True)        # Output: False
print()

# Assignment Operators:
# =, +=, -=, *=, /=, %=, **=, //=.

a = 32
a+=3
print(a)

#Membership Operators:
# in, not in.

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # Output: True
print()

#Identity Operators:
# is, is not.
x = 10
y = 10
print(x is y)  # Output: True