# Class: Class is a blueprint or template, Eg. form and exam that contains name, age, electives, Father's name etc.

# Object:  Object are specific instance created from the template(Class), Eg, form which contains the data for John Doe

class Employee:
    company = "HP"

    def get_salary(self):
        return 34000

e = Employee() # An object of class Employee is created here.
print(e.get_salary())    