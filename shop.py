class Stock:
    pass


class Employee:
    def __init__(self, name, section, position, salary):
        self.name = name
        self.section = section
        self.salary = salary
        self.position = position

    def __repr__(self):
        return f'{self.name} / {self.section} / {self.position}'

    def get_name(self):
        return self.name

    def get_section(self):
        return self.section

    def get_salary(self):
        return self.salary

    def get_position(self):
        return self.position

    def get_paid(self):
        print(f'{self} got ${self.salary}')
        return self.salary


class Room:
    def __init__(self):
        self.sections = []

    def get_sections(self):
        return self.sections

    def add_sections(self, section):
        self.sections.append(section)


class Section:
    def __init__(self, name):
        self.name = name
        self.staff = []
        self.salary_request = 0

    def __repr__(self):
        return f'{self.name} Section'

    def get_staff(self):
        return self.staff

    def get_salary_request(self):
        total_salary_request = sum([worker.get_salary() for worker in self.staff])
        return total_salary_request


class HumanResourcesDepartment:
    def __init__(self):
        self.salary_fund = 10000

    def __str__(self):
        return 'Human Resources Department'

    def get_salary_fund(self):
        return self.salary_fund

    def hire(self, worker: Employee, section: Section):
        section.get_staff().append(worker)
        worker_salary = worker.get_salary()

    def fire(self, worker: Employee, section: Section):
        section.get_staff().remove(worker)


class Accounting:
    def __init__(self):
        self.departments = []
        self.salary_fund = 10000  # Деньги приходят из Sales
        self.salary_requests = []

    def __repr__(self):
        return 'Accounting Department'

    def get_departments(self):
        return self.departments

    def add_department(self, department):
        self.departments.append(department)

    def get_salary_fund(self):
        return self.salary_fund

    def get_salary_requests(self):
        return self.salary_requests

    def pay_salary(self, section):
        for worker in section.get_staff():
            self.salary_fund -= worker.get_paid()


class Sales:
    pass

class Product:
    pass

class Contractor:
    pass


class Store:
    def __init__(self, shopping_room):
        self.sections = shopping_room.get_sections()

    def get_sections(self):
        return self.sections

    def add_sections(self, shopping_room: Room):
        self.sections.append(shopping_room)


if __name__ == '__main__':
    account = Accounting()
    hr = HumanResourcesDepartment()
    s1 = Section(name='Alcohol')
    s2 = Section(name='Meat')
    e1 = Employee(name='Bill Johns', section=s1, position='unknown', salary=2000)
    e2 = Employee(name='Tag Jones', section=s1, position='head', salary=4000)
    shopping_room = Room()
    shopping_room.add_sections(s1)
    shopping_room.add_sections(s2)
    shop = Store(shopping_room)
    hr.hire(worker=e1, section=s1)
    hr.hire(worker=e2, section=s1)
    print(s1.get_salary_request())
    print(account.get_sections())
    print(shop.get_sections())


