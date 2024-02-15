#  Composition 2

class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def get_total(self):
        return self.pay * 12 + self.bonus


class Employee:
    def __init__(self, name: str, age: int, salary: Salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Employee: {self.name}, {self.age}, {self.salary.get_total()}"


s1 = Salary(5000, 1000)
e1 = Employee("John", 30, s1)
print(e1)
