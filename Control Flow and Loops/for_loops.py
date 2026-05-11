# What are For Loops?
# For loops are used to iterate over a sequence (e.g., list, string, range).
# They execute a block of code repeatedly for each item in the sequence.

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit) # this prints the values in list one by one
print(fruits) #this prints whole list in a single line


for i in range(1,6): #range works like [1-6) not[1-5]
    print(i)

print()
print("This is the table of 5")
for i in range(1,11):
    print("5 *",i,"=",5*i)