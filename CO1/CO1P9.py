a=input("Enter the string")
start=a[0]
end=a[-1]
swapped_string = end+a[1:-1]+start
print("Swapped string is:",swapped_string)