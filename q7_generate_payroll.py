name = input("Enter name: ")
working_hours = float(input("Enter number of hours worked weekly: "))
pay_rate = float(input("Enter hourly pay rate: "))
cpf = float(input("Enter CPF contribution rate(%): "))

gross_pay = pay_rate * working_hours
cpf_contribution = cpf * gross_pay / 100
net_pay = gross_pay - cpf_contribution


print("Payroll statement for",name)
print("Number of hours worked in week: ",working_hours)
print("Hourly pay rate: $",pay_rate)
print("Gross pay = $",gross_pay)
print("CPF contribution at",cpf,"% = $",cpf_contribution)
print("Net pay = $",net_pay)
