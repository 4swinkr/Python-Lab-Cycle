import csv
with open('studentdetails.csv','r')as csv_file1:
    csv_reader=csv.DictReader(csv_file1)
    with open('newstudentdetails6.csv','w')as csv_file2:
        feildnames1=['Roll No','Student Name','Grade','CO1','CO2','CO3','CO4','CO5']
        csv_writer=csv.DictWriter(csv_file2,fieldnames=feildnames1)
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)