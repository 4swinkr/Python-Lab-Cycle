fn1=open("P01-txtFile.txt",'r')
f=fn1.readlines()
for x in range(0,len(f)):
    print(f[x])
fn1.close()