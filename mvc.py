# Модель (Model)
class UserModel:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return f'User: {self.username}, Email: {self.email}'


# Представление (View)
class UserView:
    def show_user_details(self, user):
        print("User Details:")
        print(f"Username: {user.username}")
        print(f"Email: {user.email}")


# Контроллер (Controller)
class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_user_details(self):
        return self.model

    def show_user_details(self):
        user = self.get_user_details()
        self.view.show_user_details(user)


# Использование паттерна MVC
if __name__ == "__main__":
    # Создаем объекты модели, представления и контроллера
    user_model = UserModel("JohnDoe", "johndoe@example.com")
    user_view = UserView()
    user_controller = UserController(user_model, user_view)

    # Отображаем детали пользователя через контроллер
    user_controller.show_user_details()
