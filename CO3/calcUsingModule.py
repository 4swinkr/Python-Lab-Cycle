import calModule

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
x=int(input("Enter your choice: 1.Sum  2.Difference  3.Multiplication  4.Division  5.Exit : "))

if x==1:
    print("Sum is:", calModule.sum(a,b))
elif x==2:
    print("Difference is:", calModule.diff(a,b))
elif x==3:
    print("Multiplication is:", calModule.mul(a,b))
elif x==4:
    print("Division is:", calModule.div(a,b))
elif x==5:
    exit
    
