# In Python, variables have scope (where they can be accessed) and lifetime (how long they exist). Variables are created when a function is called and destroyed when it returns. Understanding scope helps avoid unintended errors and improves code organization.

# Types of Scope in Python
# 1. Local Scope (inside a function) – Variables declared inside a function are accessible only within that function.
# 2. Global Scope (accessible everywhere) – Variables declared outside any function can be used throughout the program.

def sum(a,b):
    c = a + b # here c a and b are local variables
    z  = 2 
    print(z) # here we can access z as it is a global variable but changing its value will create a local variable of it which is destroyed after the function returns
    return c
print(sum(4,5))

# print(c) c wont get print because c is a local variable and not a global variable
z  =1 # here z is a global variable
