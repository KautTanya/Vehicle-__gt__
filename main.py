"""Vehicle-__gt__"""


class Vehicle:
    """Представлення транспортного засобу"""
    def __init__(self, name, speed, cost):
        self.name = name
        self.speed = speed
        self.cost = cost

    def __gt__(self, other):
        if isinstance(other, Vehicle):
            return self.speed > other.speed
        raise TypeError("Error type")


v1 = Vehicle("Name1", 100, 10000)
v2 = Vehicle("Name2", 110, 9000)

result = sorted([v1, v2])
print(result)
print(v1 > v2)
