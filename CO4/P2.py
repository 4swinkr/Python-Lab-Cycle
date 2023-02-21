class Bank:
    def __init__(self):
        self.accnumber=int(input("enter the account number:"))
        self.name=input("enter name:")
        self.typeacc=input("enter the type of account:")
        self.balance=0
    def deposit(self):
        amount=int(input("enter the amount"))
        self.balance=self.balance+amount
        print("deposited and balance is",self.balance)
    def withdraw(self):
        amount=int(input("enter the amount"))
        if self.balance> amount:
            self.balance -=amount
            print("withdraw and balance is",self.balance)
        else:
            print("withdraw not posiable")
ac1=Bank()
print("acountnumber is:",ac1.accnumber)
print("name is:",ac1.name)
print(" balance is:",ac1.balance)
while(True):
    print("\n1.deposit money\n2.withdraw money\n3.exit")
    ch=int(input("enter the your choice:"))
    if(ch==1):
        ac1.deposit()
    elif(ch==2):
        ac1.withdraw()
    else:
        exit(0)