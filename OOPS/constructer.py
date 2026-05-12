# Class: Class is a blueprint or template, Eg. form and exam that contains name, age, electives, Father's name etc.

# Object:  Object are specific instance created from the template(Class), Eg, form which contains the data for John Doe

class Employee:
    def __init__(self, salary, name, bond):
        self.salary = salary #create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond

    def get_salary(self): # self is important here because self is the way to reference the object of the class which is being created.
        return self.salary
    def get_info(self):
        return f"Name: {self.name}, Salary: {self.salary}, Bond: {self.bond} years" 


  

e1 = Employee(34000, "john doe", 4)
print(e1.get_salary())

e1 = Employee(34000, "john doe", 4)
print(e1.get_info())
