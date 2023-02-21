class Rectangle:
    def __init__(self):
        self.l = int(input("Enter the length: "))
        self.b = int(input("Enter the breadth: "))
        
    def get_perimeter(self):
        return 2 * (self.l + self.b)
    
    def get_area(self):
        return self.l * self.b
    
    def compare(self,obj2):
        if obj1.get_area() == obj2.get_area():
            print("Area of both rectangles are the same")
        elif obj1.get_area() > obj2.get_area():
            print("Area of Rectangle 1 is greater")
        else:
            print("Area of Rectangle 2 is greater")

obj1=Rectangle()
obj2=Rectangle()
print("Area of rectangle: ", (obj1.get_area()))
print("Perimeter of rectangle: ", (obj1.get_perimeter()))
print("Area of rectangle: ", (obj2.get_area()))
print("Perimeter of rectangle: ", (obj2.get_perimeter()))
print("Perimeter of rectangle: ", (obj2.get_perimeter()))
obj1.compare(obj2)

