import pandas as pd

print(' employees data')
emp = pd.read_csv(r"D:\summ_program\emp.csv")
print(emp)

print(' attendance data')

att = pd.read_csv(r"D:\summ_program\attendance.csv")
print(att)

print(' Merge employees and attendance')
merged = pd.merge(emp, att, on="EmpID")
print(merged)

print(' employee salary > 50000')
print(emp[emp["Salary"] > 50000])
 
print('employees from delhi')
print(emp[emp["City"] == "Delhi"])

print('employees from mohali / experience more than 2 years') 
print(emp[(emp["City"] == "Mohali") & (emp["Experience"] > 2)])

print('employees sort on the basis of experience')
print(emp.sort_values(by="Experience"))

print("according to their salary(descending order)")
print(emp.sort_values(by="Salary", ascending=False))

print('total employees count')
print("Total employees:", len(emp))

print("number of employees according to city")
print(emp["City"].value_counts())

print(' maximum and minimum salary')
print("Max salary:", emp["Salary"].max())
print("Min salary:", emp["Salary"].min())

print('missing vaalues check and replace')
print(emp.isnull().sum())   
print(emp.fillna('unknown'))

print(' present employees')
print(merged[merged["Attendance"] == "Present"])

