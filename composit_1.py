#  Composition 1

class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def get_total(self):
        return self.pay * 12 + self.bonus


class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.salary = Salary(pay, bonus)

    def __str__(self):
        return f"Employee: {self.name}, {self.age}, {self.salary.get_total()}"


e1 = Employee("John", 30, 5000, 1000)
print(e1)
