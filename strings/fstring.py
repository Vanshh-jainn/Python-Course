#before f string
template = "Hey {} take this {} bag"
a = "vansh"
b = "$100"
t = template.format(a,b)
print(t)

# after f string update
print(f"Hey {a} take this {b} bag.")