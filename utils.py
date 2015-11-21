class Int(object):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value == other.value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        return self.value / other.value

    def __mod__(self, other):
        return self.value % other.value

    def __and__(self, other):
        return self.value & other.value

    def __or__(self, other):
        return self.value | other.value

    def __xor__(self, other):
        return self.value ^ other.value

    def __rshift__(self, other):
        return self.value >> other.value

    def __lshift__(self, other):
        return self.value << other.value

    def __invert__(self):
        return ~self.value

    def __int__(self):
        return self.value