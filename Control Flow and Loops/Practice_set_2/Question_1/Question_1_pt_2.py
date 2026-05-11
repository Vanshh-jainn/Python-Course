# Create a program that checks if a person is eligible to vote (age >= 18).
age = int(input("Enter your age: "))

if (age<18 and age>=0):
    print("You are not eligible to vote.")
elif (age == 18):
    print("You just became eligible to vote!")
elif(age<0):
    print("Enter valid age")
else:
    print("You are eligible to vote.")