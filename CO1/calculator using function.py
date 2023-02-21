def sum(a,b):
    "Adding two numbers a and b"
    sum=a+b
    return sum
def diff(a,b):
    "Difference of two numbers a and b"
    diff=a-b
    return diff
def mul(a,b):
    "Multiplication of two numbers a and b"
    mul=a*b
    return mul
def div(a,b):
    "Division of two numbers a and b"
    div=a/b
    return div

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
x=int(input("Enter your choice: 1.Sum  2.Difference  3.Multiplication  4.Division  5.Exit : "))

if x==1:
    print("Sum is:", sum(a,b))
elif x==2:
    print("Difference is:", diff(a,b))
elif x==3:
    print("Multiplication is:", mul(a,b))
elif x==4:
    print("Division is:", div(a,b))
elif x==5:
    exit