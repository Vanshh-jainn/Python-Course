class Point:
    def __init__(self, x, y):  
        self.x = x
        self.y = y

    def sum(self, p):
        return Point((self.x+p.x), (self.y+p.y))
    def print_point(self):
        return f"X is {self.x} and Y is {self.y}"
    def __add__(self, p):
        return Point((self.x+p.x), (self.y+p.y))
    
        
p1 = Point(2,3)
p2 = Point(4,5)

#p = p1.sum(p2) #Returns a new point which is the sum of p1 and p2
p = p1 + p2  # We overloaded the + operator by writing __add__ function.
print(p.print_point())
