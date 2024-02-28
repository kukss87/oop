class School:
    """Интерфейс для работы со школьной системой"""
    # Экземпляр класса School может быть только один

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __str__(self):
        return 'School object'


class Course:
    """Класс для работы с курсами"""

    # Создать класс Course, который будет хранить информацию о курсах.
    # Класс должен иметь методы:
    # - расчет средней оценки по курсу
    # - расчет средней оценки по всем студентам
    # - расчет средней оценки по всем студентам по курсу
    # - расчет посещаемости курса
    # - расчет количества оценок студента по курсу
    # - список студентов курса без оценок

    uid = 0

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.teacher = None
        self.students = []
        self.grades = {}
        self.course_id = self.autoincrement()

    @classmethod
    def autoincrement(cls):
        cls.uid += 1
        instance_id = cls.uid
        return instance_id

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def get_title(self):
        return self.title

    def get_uid(self):
        return self.course_id

    def get_students(self):
        """Список студентов курса"""
        if not self.students:
            return f'На курса {self} пока нет ни одного студента'
        return self.students

    def get_number_of_students(self):
        return len(self.students)

    def get_teacher(self):
        """Имя преподавателя курса"""
        if not self.teacher:
            return f'На курс {self} учитель еще не назначен'
        return self.teacher

    def assign_teacher(self, teacher):
        """Назначение преподавателя курсу"""
        if isinstance(teacher, Teacher):
            self.teacher = teacher
            teacher.attach_course(self)
        else:
            raise TypeError(f'{teacher} должен быть экземпляром класса Teacher')

    def add_student(self, student):
        """Добавление студента на курс"""
        if isinstance(student, Student):
            self.students.append(student)
            student.enroll_in_course(self)
        else:
            raise TypeError(f'{student} должен быть экземпляром класса Student')

    def expel_student(self, student):
        """Удаление студента из курса"""
        if student in self.students:
            self.students.remove(student)
            student.leave_course(self)
        else:
            raise TypeError(f'{student} еще не зачислен на курс')

    def average_grade(self):
        length = len([student for student in self.students if student.has_grades(self)])
        summa = sum([student.get_course_average_grade(self) for student in self.students if student.has_grades(self)])
        avg = summa/length
        return avg


class Teacher:
    """Класс для работы с преподавателями"""

    # Создать класс Teacher, который будет хранить информацию о преподавателях.
    # Класс должен иметь методы:
    # - добавление курса в список курсов преподавателя(courses_attached)
    # - выставление оценки студенту по курсу
    # - расчет количества студентов у преподавателя
    # - расчет количества часов  работы преподавателя
    # - список студентов у преподавателя

    uid = 0

    def __init__(self, name):
        self.name = name
        self.courses_attached = []
        self.courses_available = []
        self.teacher_id = self.autoincrement()

    @classmethod
    def autoincrement(cls):
        cls.uid += 1
        instance_uid = cls.uid
        return instance_uid

    def __repr__(self):
        return self.name

    def attach_course(self, course):
        """Добавление курса в список курсов преподавателя"""
        self.courses_attached.append(course)

    @staticmethod
    def rate(course, student, grade):
        student.new_grade(course, grade)


class Student:
    """Класс для работы со студентами"""

    # Создать класс Student, который будет хранить информацию о студентах.
    # Класс должен иметь методы:
    # - добавление курса в один из двух списков (finished_courses или courses_in_progress)
    # - когда заканчивается курс из списка courses_in_progress, он автоматически добавляется в
    #  - список finished_courses

    uid = 0

    def __init__(self, name, gender=None):
        self.name = name
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.student_id = self.autoincrement()

    @classmethod
    def autoincrement(cls):
        cls.uid += 1
        instance_uid = cls.uid
        return instance_uid

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_current_courses(self):
        """Список курсов, на которые студент записан"""
        return self.courses_in_progress

    def get_number_of_current_courses(self):
        return len(self.courses_in_progress)

    def get_finished_courses(self):
        """Список курсов, завершенных студентом"""
        return self.finished_courses

    def get_all_grades(self):
        return self.grades

    def get_grade(self, course):
        return self.grades[course]

    def has_grades(self, course):
        if not self.grades[course]:
            return False
        return True

    def get_course_average_grade(self, course):
        if self.has_grades(course):
            return round(sum(self.grades[course])/len(self.grades[course]), 2)
        return 'No marks'

    def get_total_average_grade(self):
        length = len([item for item in self.grades if self.has_grades(item)])
        avg = sum([self.get_course_average_grade(subj) for subj in self.grades if self.has_grades(subj)])/length
        return round(avg, 2)

    def new_grade(self, course, grade):
        self.grades[course].append(grade)

    def enroll_in_course(self, course):
        """Запись на курс"""
        self.courses_in_progress.append(course)
        self.grades[course] = []

    def leave_course(self, course):
        self.courses_in_progress.remove(course)


class Lesson:
    """Класс для работы с занятиями"""
    # - добавление занятия в расписание
    # - удаление занятия из расписания
    # - расчет количества занятий в расписании
    pass


class Grades:
    """Класс для работы с оценками студентов"""
    pass


class Schedule:
    """Класс для работы с расписанием занятий"""
    # - добавление занятия в расписание
    #  - удаление занятия из расписания
    # - расчет количества занятий в расписании
    # - составление расписания
    # - изменение расписания
    # - статистика занятий в расписании (по курсам, по преподавателямб по студентам)
    pass


if __name__ == '__main__':
    school = School()
    math = Course('Math', 10)
    english = Course('English', 10)
    history = Course('History', 10)
    physics = Course('Physics', 10)

    teacher1 = Teacher('Tracy Solomon')
    teacher2 = Teacher('Kathy Haas')
    teacher3 = Teacher('John Perez')

    student1 = Student('Michele Mann DDS')
    student2 = Student('Gregory Shepherd')
    student3 = Student('Jennifer Cunningham')
    student4 = Student('Seth Meyers')
    student5 = Student('Joseph Diaz')

    english.assign_teacher(teacher1)
    history.assign_teacher(teacher2)
    math.assign_teacher(teacher3)

    english.add_student(student1)
    english.add_student(student2)
    history.add_student(student2)
    math.add_student(student2)
    english.add_student(student4)
    english.add_student(student5)
    english.add_student(student3)
    english.expel_student(student1)

    print(english.get_students())
    print(english.get_number_of_students())
    print(history.get_students())
    print(physics.get_teacher())
    print(english.get_teacher())
    print(student2.get_current_courses())
    print(student2.get_number_of_current_courses())
    print(physics.get_uid())

    student2.new_grade(english, 12)
    student2.new_grade(english, 12)
    student3.new_grade(english, 10)
    student3.new_grade(english, 10)
    teacher2.rate(math, student2, 1)

    print(student2.get_all_grades())
    print(student2.get_grade(english))
    print(student2.get_course_average_grade(english))
    print(student2.get_course_average_grade(history))
    print(student2.get_total_average_grade())
    print(english.average_grade())
    print(math.average_grade())

