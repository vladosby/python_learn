def my_func1(a, b):
    return sum((a, b)) * 0.05


print(my_func1(40, 60))


def my_func2(*args):
    return sum(args) * 0.05


print(my_func2(40, 60, 100, 100, 100))


def my_func3(**kwargs):
    print(kwargs)
    if "key1" in kwargs:
        print(f"key1 is present in the dict")


my_func3(key1="aaa", key2="bbb", name="mmm")


# {'key1': 'aaa', 'key2': 'bbb', 'name': 'mmm'}
# key1 is present in the dict

def my_func4(*args, **kwargs):
    print(args)
    print(kwargs)


my_func4(1, 2, 3, 4, key1="aaa", key2="bbb")


# (1, 2, 3, 4)
# {'key1': 'aaa', 'key2': 'bbb'}

def square(num):
    return num ** 2


test_array1 = [1, 2, 3, 4, 5]
result1 = map(square, test_array1)
print(result1)
# <map object at 0x7f84a802c9a0>
print(list(result1))


# [1, 4, 9, 16, 25]

def check_even(num):
    return num % 2 == 0


filter1 = filter(check_even, test_array1)
print(filter1)
# <filter object at 0x7fb5380c3610>
print(list(filter1))
# [2, 4]

print(list(map(lambda num: num ** 2, test_array1)))
# [1, 4, 9, 16, 25]


global_variable = 50


def override_global():
    global global_variable

    global_variable = "New Value"
    x = 10
    print(f"globals={globals()}")
    print(f"locals={locals()}")


# globals={'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7fddf8028c70>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/Users/vladislavki/Documents/projects/own/python_learn/src/functions_and_methods.py', '__cached__': None, 'my_func1': <function my_func1 at 0x7fdd88036280>, 'my_func2': <function my_func2 at 0x7fddd80fb550>, 'my_func3': <function my_func3 at 0x7fddd80fb4c0>, 'my_func4': <function my_func4 at 0x7fddd80fb430>, 'square': <function square at 0x7fddd80fb3a0>, 'test_array1': [1, 2, 3, 4, 5], 'result1': <map object at 0x7fdda804b6a0>, 'check_even': <function check_even at 0x7fddd80fb310>, 'filter1': <filter object at 0x7fdda804b430>, 'global_variable': 'New Value', 'override_global': <function override_global at 0x7fddd80fb1f0>}
# locals={'x': 10}

print(global_variable)
# 50
override_global()
print(global_variable)
# New Value
