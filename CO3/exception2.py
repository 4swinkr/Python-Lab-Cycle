a=int(input("Enter a:"))
b=int(input("Enter b: "))
l=[10,20,30,40,50]

try:
    c=a/b
    print(c)
    print(l[4])
except:
    print("Exception raised and using default value for denominator")
    b=1
    c=a/b
    print(c)