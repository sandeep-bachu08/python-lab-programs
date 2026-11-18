import csv
with open("payroll.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Basic Salary", "Bonus", "Total"])
    n = int(input("Enter number of employees: "))
    for i in range(n):
        name = input("Enter employee name: ")
        salary = float(input("Enter basic salary: "))
        bonus = float(input("Enter bonus: "))
        total = salary + bonus
        writer.writerow([name, salary, bonus, total])
with open("payroll.csv", "r") as file:
    reader = csv.reader(file)
    print("\nPayroll Details:")
    for row in reader:
        print(row)
