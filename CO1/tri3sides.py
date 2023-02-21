import math
print("Enter three sides")
a=int(input())
b=int(input())
c=int(input())
print(a,b,c)
s=a+b+c/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle",area)
