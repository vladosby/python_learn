# the id() function can return the memory address of the variable punk as an integer.
variable = 10
print(id(variable))
# 4508817744
print(id(variable))
# 4508817744

# PyObj_FromPtr() function, which is provided by the built-in _ctypes module,
# to get the value of an object by its memory address.
import _ctypes

print(_ctypes.PyObj_FromPtr(id(variable)))


# 10


class Dog:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"My name is {self.name}")


dog = Dog("Bobby")
print(dog)
address_in_memory = id(dog)
# 140194443540368
print(address_in_memory)

_ctypes.PyObj_FromPtr(address_in_memory).print_name()
# My name is Bobby
