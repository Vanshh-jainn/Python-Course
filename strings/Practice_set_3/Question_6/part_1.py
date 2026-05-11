# Write a program that counts how many vowels are in a given string.

a = (input("Enter your sentance: "))

vowels = ["a", "e", "i", "o", "u"]
sum = 0
for char in a.lower():
    
    if(char in vowels):
        sum+=1

print(f"There are {sum} vowels in the string.")