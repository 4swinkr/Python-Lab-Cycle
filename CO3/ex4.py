marks=int(input("Enter marks"))
try:
    if marks<0 or marks>100:
        raise Exception("Marks should be in between 1 and 100")
    print("Marks=",marks)
except Exception as e:
    print(e)
    