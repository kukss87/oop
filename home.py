class Device:
    def __init__(self):
        self.state = 'off'
        self.device_type = None

    def get_state(self):
        return self.state

    def get_type(self):
        return self.device_type

    def __str__(self):
        return f'{self.device_type}'

    def on(self):
        self.state = 'on'
        print(f'{self} is on')

    def off(self):
        self.state = 'off'
        print(f'{self} is off')


class Thermostat(Device):
    def __init__(self):
        super().__init__()
        self.device_type = 'thermostat'


class Light(Device):
    def __init__(self):
        super().__init__()
        self.device_type = 'light'


class Security(Device):
    def __init__(self):
        super().__init__()
        self.device_type = 'security'


class SmartHome:
    def __init__(self):
        self.thermostats = []
        self.lamps = []
        self.security = []

    def add_delegate(self, delegate):
        if isinstance(delegate, Thermostat):
            self.thermostats.append(delegate)
        elif isinstance(delegate, Light):
            self.lamps.append(delegate)
        else:
            self.security.append(delegate)

    @staticmethod
    def delegate(delegate):
        if delegate.get_state() == 'on':
            delegate.off()
        else:
            delegate.on()


home = SmartHome()
t1 = Thermostat()
t2 = Thermostat()
l1 = Light()
l2 = Light()
s1 = Security()
s2 = Security()
home.add_delegate(t1)
home.add_delegate(t2)
home.add_delegate(l1)
home.add_delegate(l2)
home.add_delegate(s1)
home.add_delegate(s2)
home.delegate(t1)
home.delegate(t1)
home.delegate(t1)
home.delegate(t2)
home.delegate(t2)
home.delegate(l1)
home.delegate(l1)
home.delegate(l2)
home.delegate(s1)
home.delegate(s2)
home.delegate(s1)
home.delegate(s1)
home.delegate(s2)
