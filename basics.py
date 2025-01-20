# Python OOPS

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return f'{self.first} {self.last}'

emp_1 = Employee("Faiz", "A", "4800000")
emp_2 = Employee("Erick", "Owens", "2500000")

print(emp_2.email)
print(emp_2.fullname())

print(Employee.fullname(emp_2))