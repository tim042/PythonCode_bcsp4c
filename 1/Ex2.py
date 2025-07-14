Id = str(input("ID="))
FName = str(input("Name="))
LName = str(input("Last Name="))
Bs = int(input("BaseSalary="))
Bo = int(input("Sala="))
Bt = int(input("Salary t="))

BA = Bs + Bo +Bt

print(Id)
print(FName,LName)
print("All Salary=",BA)

if BA>1500000:
    HB = BA*5/100
    JB = BA - HB
    print(JB)
elif BA>1000000:
    MB = BA*3/100
    KB = BA - MB
    print(KB)
else:
    print(BA)

