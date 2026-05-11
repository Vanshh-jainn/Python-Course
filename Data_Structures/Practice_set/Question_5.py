student = {"name": "John", "age": 20, "grade": "A"}
print(student["name"])
student["grade"] = "A+"
print(student)
student["city"] = "Delhi"
print(student)

my_dict = {"Treater": 2346547890,
           "Vansh": 4563458762,
           "Pringles":3456542876}
print(my_dict.keys())
print(my_dict.values())
for key, value in my_dict.items():
    print(key,value)
