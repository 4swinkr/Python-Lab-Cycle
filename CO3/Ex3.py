a=int(input("Enter a:"))
b=int(input("Enter b: "))
try:
    if b==0:
        raise Exception
    c=a/b
    print(c)
except:
    print("Exception raised")