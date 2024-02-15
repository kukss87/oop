"""
in_progress
completed
overdue
"""
from datetime import datetime as date


class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        if date.now() <= self.deadline:
            return f'Description: {self.description}. Deadline: {self.deadline}. Completed: {self.completed}'
        return f'Description: {self.description}. Deadline: {self.deadline} is overdue!'


class TaskManager:
    @staticmethod
    def create_task(description, deadline, priority='general'):
        if priority == 'urgent':
            return UrgentTask(description, deadline)
        elif priority == 'important':
            return ImportantTask(description, deadline)
        else:
            return Task(description, deadline)


class UrgentTask(Task):
    def __init__(self, description, deadline):
        super().__init__(description, deadline)
        self.priority = 'urgent'

    def __str__(self):
        return f'Description: {self.description}. Deadline: {self.deadline}. Completed: {self.completed}.' \
               f' Priority ({self.priority})'


class ImportantTask(Task):
    def __init__(self, description, deadline):
        super().__init__(description, deadline)
        self.priority = 'important'

    def __str__(self):
        return f'Description: {self.description}. Deadline: {self.deadline}. Completed: {self.completed}.' \
               f' Priority ({self.priority})'


task1 = TaskManager.create_task('Task1', date(2024, 2, 6))
task2 = TaskManager.create_task('Task2', date(2024, 2, 16), priority='urgent')
task3 = TaskManager.create_task('Task3', date(2024, 2, 11), priority='important')

print(task1)
print(task2)
print(task3)
