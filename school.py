class Pupil:
    def __init__(self, name, class_titel=None):
        self.name: str = name
        self.class_titel: str = class_titel
        self.marks: dict = {'art': None,
                            'chemistry': None,
                            'english': None,
                            'geography': None,
                            'history': None,
                            'math': None,
                            'music': None,
                            'physical_Education': None,
                            'science': None,
                            'spanish': None}

    def __str__(self):
        return self.name

    def update_mark(self, subject: str, mark: int):
        if subject in self.marks:
            self.marks.update({subject: mark})
        else:
            print(f'No such subject exists. Use method obj.add_subject()')

    def show_marks(self):
        print(f'Pupil {self} has following grades: ')
        for key, value in self.marks.items():
            print(f'{key}: {value}')

    def add_subject(self, subject: str):
        self.marks.update({subject: None})

    def enroll_in_class(self, class_titel):
        self.class_titel = class_titel

    def expel_from_class(self):
        self.class_titel = None

    def get_class(self):
        return self.class_titel

    def expelling(self):
        self.class_titel = 'expelled'


class School:

    def __init__(self, number):
        self.number = number
        self.classes_list = []
        self.expelled_pupils = []

    def __str__(self):
        return f'{self.number}'

    def register_class(self, class_titel):
        self.classes_list.append(class_titel)

    @staticmethod
    def enroll_pupil(pupil, class_titel):
        class_titel.enroll_pupil(pupil)
        print(f'{pupil} enrolled in {class_titel}')

    def show_classes(self):
        print(f'School {self} has following classes: ')
        for class_item in self.classes_list:
            print(f'{class_item}')

    def transfer(self, pupil, old_class, new_class):
        new_class.enroll_pupil(pupil)
        old_class.transfer_out(pupil)
        pupil.enroll_in_class(new_class)
        print(f'Pupil {pupil} expelled from {self}')


class Class:
    def __init__(self, title, school: School):
        self.title = title
        self.pupil_list = []
        self.expelled_pupils = []
        self.new_class = school
        self.new_class.register_class(title)

    def __str__(self):
        return self.title

    def enroll_pupil(self, pupil):
        self.pupil_list.append(pupil)
        pupil.enroll_in_class(self)

    def transfer_out(self, pupil):
        self.pupil_list.remove(pupil)

    def expel(self, pupil):
        self.pupil_list.remove(pupil)
        self.expelled_pupils.append(pupil)
        pupil.expelling()
        print(f'Pupil {pupil} expelled from {self}')

    def show_expelled(self):
        print(f'From class {self} has expelled following pupils: ')
        for pupil in self.expelled_pupils:
            print(f'{pupil}')

    def show_pupils(self):
        print(f'Class {self} has following pupils: ')
        for pupil in self.pupil_list:
            print(f'{pupil}')


if __name__ == '__main__':
    SCHOOL = School(42)
    pupil_1 = Pupil('Li', '4b')
    pupil_2 = Pupil('Johansen')
    c = Class('7b', SCHOOL)
    c1 = Class('7a', SCHOOL)
    pupil_1.update_mark('math', 10)
    SCHOOL.enroll_pupil(pupil_1, c)
    SCHOOL.enroll_pupil(pupil_2, c)

    c.show_pupils()
    SCHOOL.show_classes()
    c.show_pupils()
    SCHOOL.transfer(pupil_1, c, c1)

    print('----')
    c.show_pupils()
    c1.show_pupils()

