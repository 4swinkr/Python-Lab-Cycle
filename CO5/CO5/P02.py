f=open("P02-txtFile.txt",'r')
f1=open("P02-txtCpyodd.txt",'w')
lines=f.readlines()
for i in range(0,len(lines)):
    if i%2==0:
        l=f1.write(lines[i])
f.close()
fn=open("P02-txtCpyodd.txt",'r')
cont=f1.read()
print(cont)
f1.close()