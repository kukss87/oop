import random

class School:
    """Интерфейс для работы со школьной системой"""
    # Экземпляр класса School может быть только один

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.courses = []

    def __str__(self):
        return 'School object'

    def add_course(self, course):
        if isinstance(course, Course):
            self.courses.append(course)
        else:
            print(f'{course} is not a Course_object!!!')

    def get_courses(self):
        if not self.courses:
            return 'Ни один курс еще не создан'
        return self.courses

    def join_lists(self):  # helper method
        full_list = []
        for course in self.courses:
            students = course.get_students()
            if students:
                full_list.extend(students)
        full_list = list(set(full_list))
        return full_list

    @staticmethod
    def sort_method(item):  # helper method
        return item[1]

    def sort_all_students(self):
        full_list = self.join_lists()
        lst = [(student, student.get_total_average_grade()) for student in full_list]
        lst.sort(reverse=True, key=self.sort_method)
        return lst


class Course:
    """Класс для работы с курсами"""
    # - Средние баллы всех студентов

    uid = 0

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.covered_lessons = 0
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

    def get_duration(self):
        return self.duration

    def get_students(self):
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
            self.grades[student] = []
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

    def has_grades(self, student):
        if not self.grades[student]:
            return False
        return True

    def average_grade(self):
        length = len([student for student in self.students if student.has_grades(self)])
        if length <= 0:
            return
        summa = sum([student.get_course_average_grade(self) for student in self.students if student.has_grades(self)])
        avg = summa/length
        return round(avg, 2)

    @staticmethod
    def sort_method(item):  # helper method
        return item[1]

    def sorted_students(self):
        lst = [(student, float(student.get_course_average_grade(self))) for student in self.grades if student in self.students]
        lst.sort(key=self.sort_method, reverse=True)
        return lst

    def students_without_grades(self):
        lst = [student for student in self.grades if not self.has_grades(student)]
        return lst

    def start_course(self):
        print(f'Курс {self.title} начат')
        for les in range(self.duration):
            for stu in range(2):
                print(f'Урок {self.covered_lessons + 1}')
                student = random.choice(self.students)
                while True:
                    grade = int(input(f'{student}:  '))
                    if 1 <= grade <= 12:
                        break
                student.new_grade(self, grade)
            self.covered_lessons += 1
            print(f'Урок {self.covered_lessons} завершен')
        print(f'Курс {self.title} завершен')
        print(f'Рейтинг: {self.sorted_students()}')

        while self.students:
            for s in self.students:
                s.complete_course(self)


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

    uid = 0

    def __init__(self, name, gender=None):
        self.name = name
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grade = self.get_total_average_grade()  # ?
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
        if course in self.courses_in_progress:
            if self.has_grades(course):
                return round(sum(self.grades[course])/len(self.grades[course]), 2)
            else:
                return 0
        return 0

    def courses_without_grades(self):
        return [course for course in self.grades if not self.has_grades(course)]

    def get_total_average_grade(self):
        length = len([item for item in self.grades if self.has_grades(item)])
        if length <= 0:
            return 0
        else:
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

    def complete_course(self, course):
        course.expel_student(self)
        self.finished_courses.append(course)


class Lesson:
    """Класс для работы с занятиями"""
    # - оценивание студентов происходит только во время уроков
    # - добавление занятия в расписание
    # - удаление занятия из расписания
    # - расчет количества занятий в расписании
    def __init__(self, course):
        self.course = course

    def starts_lesson(self):
        print(f'Lesson {self.course} starts')



class Schedule:
    """Класс для работы с расписанием занятий"""
    # - добавление занятия в расписание
    #  - удаление занятия из расписания
    # - расчет количества занятий в расписании
    # - составление расписания
    # - изменение расписания
    pass


class Grades:
    """Класс для работы с оценками студентов"""
    pass


if __name__ == '__main__':
    school = School()
    math = Course('Math', 10)
    english = Course('English', 5)
    history = Course('History', 10)
    physics = Course('Physics', 10)

    school.add_course(math)
    school.add_course(english)
    school.add_course(history)
    school.add_course(physics)

    teacher1 = Teacher('Tracy Solomon')
    teacher2 = Teacher('Kathy Haas')
    teacher3 = Teacher('John Perez')

    school.add_course(teacher2)

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
    physics.add_student(student2)
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
    student3.new_grade(english, 8)
    teacher2.rate(english, student4, 1)
    teacher2.rate(english, student4, 2)
    teacher2.rate(english, student4, 9)
    teacher2.rate(english, student5, 2)
    teacher2.rate(math, student2, 1)

    print(student2.get_all_grades())
    print(student2.get_grade(english))
    print(student2.get_course_average_grade(english))
    print(student2.get_course_average_grade(history))
    print(student2.get_total_average_grade())
    print(english.average_grade())
    print(math.average_grade())
    print(student2.courses_without_grades())
    print(physics.students_without_grades())
    print(history.students_without_grades())
    print(student2.get_current_courses())
    student2.complete_course(math)
    print(student2.get_finished_courses())
    print(student2.get_current_courses())
    print(english.sorted_students())
    print(student1.get_course_average_grade(english))
    print(student2.get_course_average_grade(english))
    print(student3.get_course_average_grade(english))
    print(student4.get_course_average_grade(english))
    print(student5.get_course_average_grade(english))
    print(school.get_courses())
    print('*****************')
    print(school.sort_all_students())
    english.start_course()
    print(english.average_grade())
    print(student1.get_course_average_grade(english))
    print(student2.get_course_average_grade(english))
    print(student3.get_course_average_grade(english))
    print(student4.get_course_average_grade(english))
    print(student5.get_course_average_grade(english))
    print(english.sorted_students())
    print(english.get_students())

