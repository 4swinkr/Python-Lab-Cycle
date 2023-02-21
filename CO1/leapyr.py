print ("Print leap year between two given years")
print ("start year :2022")
startyear = 2022
endyear = int(input("Enter last year \n"))
while startyear <= endyear:
    print ("List of leap years:")
    for year in range(startyear, endyear):
        if (0 == year % 4) and (0 != year % 100) or (0 == year % 400):
           print (year)
    break        