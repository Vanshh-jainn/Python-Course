# Create a list containing a table of 5
# Normal method
table = []
for i in range(1,11):
    table.append(5*i)
print(table)

# List comprehension
Table = [(5*i) for i in range(1,11)]
print(Table)

squared = [x**2 for x in range(5)]
print(squared)  # Output: [0, 1, 4, 9, 16]