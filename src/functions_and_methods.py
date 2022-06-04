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

my_func4(1,2,3,4, key1="aaa", key2="bbb")
# (1, 2, 3, 4)
# {'key1': 'aaa', 'key2': 'bbb'}
