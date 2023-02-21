import csv
'''csv_file1=open("details.csv")
csv_reader=csv.reader(csv_file1)
for line in csv_file1:
    print(line)'''

persons=[('Lata',22,45),('Anil',21,56),('John',20,60)]
csvfile=open('persons.csv','w',newline="")
obj=csv.writer(csvfile)

for person in persons:
    obj.writerows(persons)
obj.close()