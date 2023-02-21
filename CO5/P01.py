'''fl=open("P01-txtFile.txt","r")
s=fl.readlines()
t=s.strip("\n")
print(s,t)'''

print([line.strip() for line in open('P01-txtFile.txt','r')])