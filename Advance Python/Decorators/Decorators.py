# Decorator is a function that takes a function, than it creates a new function inside its body (wrapper). Than it returns that new function.

def decorator(func):
    def wrapper():
        print("About to print hello..")
        func()
        print("I have printed this function..")
    return wrapper



@decorator
def Say_hello():
    print("Hello")

Say_hello()
# decorator(Say_hello)()




