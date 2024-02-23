
class School:
    """Интерфейс для работы со школьной системой"""

    # Создать класс School, который будет хранить информацию о школе.
    pass


class Course:
    """Класс для работы с курсами"""

    # Создать класс Course, который будет хранить информацию о курсах.
    # Класс должен иметь методы:
    # - назначение преподавателя курсу +
    # - добавление студента в курс +
    # - удаление студента из курса
    # - расчет средней оценки по курсу
    # - расчет средней оценки по всем курсам
    # - расчет средней оценки по всем студентам
    # - расчет средней оценки по всем студентам по курсу
    # - расчет количества студентов в курсе
    # - расчет посещаемости курса
    # - расчет количества оценок студента по курсу
    # - список студентов курса
    # - список курсов студента
    # - список студентов курса без оценок

    uid = 0

    def __init__(self, title):
        self.title = title
        self.teacher = None
        self.students = []
        self.grades = {}
        Course.uid += 1
        self.course_id = Course.uid

    def __repr__(self):
        return f"Course {self.title}"

    def get_students(self):
        """Список студентов курса"""
        return self.students

    def assign_teacher(self, teacher):
        """Назначение преподавателя курсу"""
        self.teacher = teacher
        teacher.attach_course(self)
        # teacher.courses_attached.append(self)

    def add_student(self, student):
        """Добавление студента на курс"""
        self.students.append(student)
        student.enroll_in_course(self)
        # student.courses.append(self)


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
        Teacher.uid += 1
        self.teacher_id = Teacher.uid

    def __repr__(self):
        return f'{self.name}'

    def attach_course(self, course):
        """Добавление курса в список курсов преподавателя"""
        self.courses_attached.append(course)


class Student:
    """Класс для работы со студентами"""

    # Создать класс Student, который будет хранить информацию о студентах.
    # Класс должен иметь методы:
    # - добавление курса в один из двух списков (finished_courses или courses_in_progress)
    # - добавление оценки студента по курсу
    # - расчет средней оценки по курсу
    # - расчет средней оценки по всем курсам

    uid = 0

    def __init__(self, name, gender=None):
        self.name = name
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.uid += 1
        self.student_id = Student.uid

    def __repr__(self):
        return f'{self.name}'

    def enroll_in_course(self, course):
        """Запись на курс"""
        self.courses_in_progress.append(course)

    def get_current_courses(self):
        """Список курсов, которые студент записан на"""
        return self.courses_in_progress


class Lesson:
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
    math = Course('Math')
    english = Course('English')
    history = Course('History')
    physics = Course('Physics')

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
    english.add_student(student4)
    english.add_student(student5)

    print(english.get_students())
    print(english.teacher)
    print(student1.get_current_courses())
