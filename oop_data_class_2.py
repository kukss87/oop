from dataclasses import dataclass, field


class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x ** 2 + y ** 2 + z ** 2) ** 0.5

    def __repr__(self):
        return f'Vector3D({self.x}, {self.y}, {self.z})'


@dataclass
class V3D:
    x: float
    y: float
    z: float
    length: float = field(init=False)

    def __post_init__(self):
        self.length = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5


v1 = Vector3D(1, 2, 3)
v2 = V3D(1, 2, 3)

print(v1.length)
print(v2.length)

print(v1)
print(v2)
