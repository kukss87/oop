class ToDoList:
    def __init__(self):
        self.name = input('List_name >>> ')
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Задание {task.get_task_name()} добавлено')

    def get_tasks(self):
        for task in self.tasks:
            print(task)

    def task_done(self, task):
        self.tasks.remove(task)
        print(f'Задание {task} выполнено')


class Task:
    def __init__(self):
        self.task = input('Task_name >>> ')

    def __str__(self):
        return f'{self.task}'

    def add_to_list(self, todolist):
        todolist.add_task(self)

    def done(self, todolist):
        todolist.task_done(self)

    def get_task_name(self):
        return self.task


if __name__ == '__main__':
    tlist = ToDoList()
    task1 = Task()
    task2 = Task()
    task3 = Task()
    task1.add_to_list(tlist)
    task2.add_to_list(tlist)
    task3.add_to_list(tlist)
    tlist.get_tasks()
    tlist.task_done(task2)
    tlist.get_tasks()

