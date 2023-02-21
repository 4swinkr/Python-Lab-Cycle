from Graphics.rectangle import*
from Graphics.circle import*
from Graphis.ThreeDgraphics.cuboid import*
from Graphis.ThreeDgraphics.sphere import*

l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
print("Area of rectangle= ",RectArea(l,b))
print("Perimeter of rectangle= ", RectPeimeter(l,b))

r=int(input("Enter the radius of circle: "))
print("Area of the circle= ", CircleArea(r))
print("Perimeter of circle= ",CirclePerimeter(r))
print()

r=