Basic_Salary = float(input("Enter Basic Salary :"))
if Basic_Salary<=10000:
    DA = (Basic_Salary * 80) / 100
    HRA = (Basic_Salary * 20) / 100
    Gross_Salary = Basic_Salary + DA + HRA
elif Basic_Salary<=20000:
    DA = (Basic_Salary * 90) / 100
    HRA = (Basic_Salary * 25) / 100
    Gross_Salary = Basic_Salary + DA + HRA
elif Basic_Salary>20000:
    DA = (Basic_Salary * 95) / 100
    HRA = (Basic_Salary * 30) / 100
    Gross_Salary = Basic_Salary + DA + HRA
print("DA is" , DA)
print("HRA is" , HRA)
print( "Gross Salary :" , Gross_Salary)