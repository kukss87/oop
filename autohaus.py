speciality_list = [
            'General',
            'Engine Specialist',
            'Transmission Technician',
            'Brake System Technician',
            'Electrical Systems Technician',
            'HVAC Technician',
            'Diagnostic Technician',
            'Tire and Wheel Technician',
            'Diesel Engine Technician',
            'Hybrid and Electric Vehicle Technician',
            'Body and Paint Technician'
]


class AutoHaus:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AutoHaus, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.masters_list = []
        self.for_cash = []
        self.total_cash = 0

    def register_master(self, master):
        self.for_cash.append(master)
        self.masters_list.append({master.name: master.speciality})
        print(f'{master.name}: {master.speciality} registered')

    def get_masters(self):
        print(f'{self.masters_list}')
        return self.for_cash

    def get_clients(self):
        for master in self.for_cash:
            if master.clients:
                print(f'Master {master.name}: {master.speciality} has such clients:')
                for client in master.clients:
                    if client:
                        print(f'{client.name}: {client.car} {client.model}')
            else:
                print(f'Master {master.name}: {master.speciality} has no clients today ')
        # print(f'{self.for_cash}')

    def get_total_cash(self):
        for master in self.for_cash:
            self.total_cash += master.day_calculate()
        print(f'{self.total_cash}')


class Master:
    def __init__(self, name: str, speciality: str):
        self.name = name
        self.speciality = speciality
        self.clients = []
        self.max_orders = 10
        self.day_income = 0

    def __str__(self):
        return f'Master: {self.name} ({self.speciality})'

    def make_appointment(self, client):
        self.clients.append(client)
        print(f'{self} now have an order from {client}')

    def cancel_appointment(self, client):
        self.clients.remove(client)
        print(f'{self} have no more the order from {client}')

    def check_appointment(self, client):
        if client in self.clients:
            return True
        return False

    def show_appointment(self):
        if self.clients:
            for client in self.clients:
                print(f'{self} has order from {client}')
        else:
            print(f'{self} has no orders today')

    def is_available(self):
        if len(self.clients) < self.max_orders:
            print(f'{self} is available now')
        else:
            print(f'{self} is not available now!')

    def get_paid(self, client, pay):
        self.day_income += pay
        print(f'{client} has paid {pay}')
        return self.day_income

    def day_calculate(self):
        print(f'{self} have ${self.day_income} today')
        return self.day_income


class Client:
    def __init__(self, name, car, model):
        self.name = name
        self.car = car
        self.model = model
        self.masters = []

    def __str__(self):
        return f'Client: {self.name} ({self.car} {self.model})'

    def __repr__(self):
        return f'Client: {self.name} ({self.car} {self.model})'

    def make_appointment(self, master):
        if master not in self.masters:
            self.masters.append(master)
            master.make_appointment(self)
            print(f'{self} now have new appointment with {master}')
        else:
            print(f'{self} already have old appointment with {master}')

    def cancel_appointment(self, master):
        if master in self.masters:
            self.masters.remove(master)
            master.cancel_appointment(self)
            print(f'{self} cancelled appointment with {master}')
        else:
            print(f'{self} yet has no appointment with {master}')

    def check_appointment(self, master):
        if master in self.masters:
            return True
        return False

    def show_appointment(self):
        if self.masters:
            for master in self.masters:
                print(f'{self} has appointment with {master}')
        else:
            print(f'{self} has no appointments!')

    def pay_bill(self, master, pay):
        master.get_paid(self, pay)
        print(f'{self} paid his bill [{pay}] for {master}')


if __name__ == '__main__':
    autohaus = AutoHaus()
    m = Master('John', 'Engine Specialist')
    m2 = Master('Joe', 'HVAC Technician')
    m3 = Master('Rod', 'Transmission Technician')
    c = Client('Tom', 'Skoda', 'Fabia')
    c2 = Client('Ben', 'bmw', 'x5')
    c3 = Client('Ann', 'audi', 'a8')
    c.make_appointment(m)
    c.make_appointment(m2)
    c2.make_appointment(m)
    c3.make_appointment(m)

    c.pay_bill(m, 250)
    c2.pay_bill(m2, 400)
    c3.pay_bill(m, 300)
    c3.pay_bill(m3, 550)
    m.day_calculate()
    m2.day_calculate()

    autohaus.register_master(m)
    autohaus.register_master(m2)
    autohaus.register_master(m3)
    autohaus.get_masters()
    autohaus.get_total_cash()
    autohaus.get_clients()
