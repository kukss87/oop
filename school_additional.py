from faker import Faker

fake = Faker()


def get_names(number):
    students = []
    for i in range(number):
        students.append(fake.name())
    return students


def get_subjects(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    clean_data = [line.strip() for line in lines if line.strip() != '']
    return clean_data


subjects = get_subjects('gpt.txt')
print(subjects)

students = get_names(100)
print(students)

teachers = get_names(len(subjects))
print(teachers)
