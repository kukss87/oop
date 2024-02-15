# models
class Dish:
    def __init__(self, name, price, number):
        self.name = name
        self.price = price
        self.number = number

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_number(self):
        return self.number

    def change_number(self, ordered_number):
        if self.number >= ordered_number:
            self.number -= ordered_number
        else:
            raise Exception('ordered_number is too big')

    def __bool__(self):
        return self.number > 0


class Kitchen:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def get_info_dishes_for_order(self):
        actual_dishes = [dish for dish in self.dishes if dish.get_number() > 0]
        names = [dish.get_name() for dish in actual_dishes]
        prices = [dish.get_price() for dish in actual_dishes]
        numbers = [dish.get_number() for dish in actual_dishes]
        return names, prices, numbers

    def eat_dish(self, name, ordered_number):
        dish = [dish for dish in self.dishes if dish.get_name() == name][0]
        dish.change_number(ordered_number=ordered_number)

    def is_not_empty(self):
        return any(dish for dish in self.dishes)


# view
class Waiter:
    def __init__(self, name):
        self.name = name

    def open(self):
        print('Welcome to our cafe!')

    def close(self):
        print('Our cafe is closed!')

    def take_order(self, names, prices, numbers):
        print(f'Hello, I am a {self.name}')
        print('we have got ', ', '.join(names))
        order_idx = None
        while True:
            name_str = input('>>> ')
            for name in names:
                if name.lower().startswith(name_str.lower()):
                    order_idx = names.index(name)
                    break
            if order_idx is not None:
                break
            print('once again, please!')
        while True:
            print('how many?')
            try:
                ordered_number = int(input('>>> '))
            except ValueError:
                print('once again, please!')
            else:
                if 0 < ordered_number <= numbers[order_idx]:
                    print('Ok')
                    return names[order_idx], ordered_number, prices[order_idx]
                else:
                    print('I can\'t do this')


# controller
class Cafe:
    def __init__(self, waiter: Waiter, kitchen: Kitchen):
        self.waiter = waiter
        self.kitchen = kitchen

    def start(self):
        self.waiter.open()
        while self.kitchen.is_not_empty():
            names, prices, numbers = self.kitchen.get_info_dishes_for_order()
            name, ordered_number, price = self.waiter.take_order(names=names, prices=prices, numbers=numbers)
            self.kitchen.eat_dish(name=name, ordered_number=ordered_number)

        self.waiter.close()


if __name__ == '__main__':
    waiter = Waiter(name='Diego')
    kitchen = Kitchen()
    kitchen.add_dish(dish=Dish(name='pizza', price=11.99, number=2))
    kitchen.add_dish(dish=Dish(name='spaghetti', price=7.99, number=3))
    kitchen.add_dish(dish=Dish(name='mozzarella', price=3.99, number=1))
    cafe = Cafe(waiter=waiter, kitchen=kitchen)
    cafe.start()
