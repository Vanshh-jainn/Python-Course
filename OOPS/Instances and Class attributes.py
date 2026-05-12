class Employee:
    company = "HP" #this is class attribute because it is shared by all the objects of the class Employee. It is not specific to any object. It is shared by all the objects of the class Employee. 

    def __init__(self, salary, name, bond, company):
        self.salary = salary #create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self): # self is important here because self is the way to reference the object of the class which is being created.
        return self.salary
    def get_info(self):
        return f"Name: {self.name}, Salary: {self.salary}, Bond: {self.bond} years" 
    
e1 = Employee(34000, "john doe", 3, "HP")
print(e1.company)

e2 = Employee(34000, "john doe", 4, "Tesla")
print(e2.company) #will always play instance attribute first if it is present in the object. If it is not present in the object then it will play class attribute. This is called as method resolution order. It will first look for the instance attribute and if it is not present then it will look for the class attribute.


#----Object Introspection-----#
print(dir(e1)) #dir() is a built-in function that returns a list of all the attributes and methods of an object. It is used for object introspection.  

