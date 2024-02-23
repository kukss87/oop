class School:
    """Интерфейс для работы со школьной системой"""

    # Создать класс School, который будет хранить информацию о школе.

    pass


class Course:
    """Класс для работы с курсами"""

    # Создать класс Course, который будет хранить информацию о курсах.
    # Класс должен иметь методы:
    # - назначение преподавателя курсу
    # - добавление студента в курс
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

    def __init__(self, name, teacher='unknown'):
        self.name = name
        self.teacher = teacher
        self.students = []
        self.grades = {}
        Course.uid += 1
        self.course_id = Course.uid

    def __str__(self):
        return f"Course {self.name} (teacher: {self.teacher.name} {self.teacher.surname})"


class Teacher:
    """Класс для работы с преподавателями"""

    # Создать класс Teacher, который будет хранить информацию о преподавателях.
    # Класс должен иметь методы:
    # - добавление курса в список курсов преподавателя(courses_attached)
    # - выставление оценки студенту по курсу
    # - расчет средней оценки по курсу
    # - расчет количества студентов у преподавателя
    # - расчет количества часов  работы преподавателя
    # - список студентов у преподавателя

    uid = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        Teacher.uid += 1
        self.teacher_id = Teacher.uid


class Student:
    """Класс для работы со студентами"""

    # Создать класс Student, который будет хранить информацию о студентах.
    # Класс должен иметь методы:
    # - добавление курса в один из двух списков (finished_courses или courses_in_progress)
    # - добавление оценки студента по курсу
    # - расчет средней оценки по курсу
    # - расчет средней оценки по всем курсам

    uid = 0

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.uid += 1
        self.student_id = Student.uid


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
    teacher1 = Teacher('John', 'Smith')
    student1 = Student('John', 'Smith', 'male')
    student2 = Student('Jane', 'Smith', 'female')
