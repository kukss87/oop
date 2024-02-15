
"""Класс для управления банковским счетом:
Создайте класс "BankAccount", который имеет атрибуты
для отслеживания баланса счета и методы для пополнения счета,
снятия денег и получения текущего баланса.
Обеспечьте возможность установки начального баланса при создании счета."""


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Недостаточно средств на счету')

    def show_balance(self):
        print(f'{self.balance}')


if __name__ == '__main__':
    account = BankAccount('Peter Geller', 1000)
    account.deposit(500)
    account.deposit(350)
    account.withdraw(2000)
    account.show_balance()

