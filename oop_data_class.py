from dataclasses import dataclass, field


@dataclass
class ThingData:
    id: int
    name: str = 'unknown'
    model: str = 'unknown'
    price: int = -1
    owners: list = field(default_factory=list)

    def __eq__(self, other):
        return self.price == other.price


td_1 = ThingData(model='x5', price=30000, id=1, owners=['Ivan', 'Petr'])
td_2 = ThingData(name='audi', price=35000, id=2,  owners=['Ben', 'John'])
td_3 = ThingData(name='audi', model='a6', id=3, owners=['Alex', 'Joseph'])
td_4 = ThingData(id=4)

td_3.owners.append('Ivan')

print(td_1.__dict__)
print(td_2.__dict__)
print(td_3.__dict__)
print(td_4.__dict__)
