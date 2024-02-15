import random
import itertools


class Cat:
    def __init__(self, breed, age, gender):
        self.breed = breed
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.breed} {self.age} {self.gender}"

    def __repr__(self):
        return self.__str__()

    def get_age(self):
        return self.age

    def __lt__(self, other):
        return self.age < other.age

    def __add__(self, other):
        if self.gender != other.gender:
            gender = random.choice(["male", "female"])
            breed = self.breed if self.breed == other.breed else random.choice([self.breed, other.breed])
            return Cat(breed=breed, age=0, gender=gender)
        return None


if __name__ == "__main__":
    cats = [
        Cat(breed='maine-coon', age=2, gender='female'),
        Cat(breed='sphynx', age=1, gender='male'),
        Cat(breed='british', age=5, gender='female'),
        Cat(breed='maine-coon', age=4, gender='male'),
        Cat(breed='sphynx', age=3, gender='female'),
    ]

    print(sorted(cats, reverse=True))
    print(cats[1] + cats[4])
    print(cats[0] + cats[1])
