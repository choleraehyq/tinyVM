'''
Python do not support reference passing of int variables, 
so I must wrap int variables in Int objects to implement registers.
The 'other' parameters below are int variables not Int.
'''

class Int(object):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

    def __repr__(self):
        return repr(self.value)

    def __lt__(self, other):
        return self.value < other

    def __le__(self, other):
        return self.value <= other

    def __gt__(self, other):
        return self.value > other

    def __ge__(self, other):
        return self.value >= other

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return self.value == other

    def __iadd__(self, other):
        self.value += other
        return self

    def __isub__(self, other):
        self.value -= other
        return self

    def __imul__(self, other):
        self.value *= other
        return self

    def __itruediv__(self, other):
        self.value /= other
        return self

    def __mod__(self, other):
        return self.value % other

    def __iand__(self, other):
        self.value &= other
        return self

    def __ior__(self, other):
        self.value |= other
        return self

    def __ixor__(self, other):
        self.value ^= other
        return self

    def __irshift__(self, other):
        self.value >>= other
        return self

    def __ilshift__(self, other):
        self.value <<= other
        return self

    def __invert__(self):
        return ~self.value

    def __int__(self):
        return self.value

    def set(self, v):
        self.value = v
