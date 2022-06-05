def hello():
    return "Hello World"


def other(some_func):
    print("Other code running")
    print(some_func())


other(hello)


# Other code running
# Hello World

def new_decorator(original_func):
    def wrap_func():
        print("Extra code before original function")
        original_func()
        print("Extra code after original function")

    return wrap_func


def func_need_decorator():
    print("I am function without decorator")


decorated_func = new_decorator(func_need_decorator)
decorated_func()


# Extra code before original function
# I am function without decorator
# Extra code after original function

@new_decorator
def second_func_need_decorator():
    print("I am SECOND function without decorator")


second_func_need_decorator()
# Extra code before original function
# I am SECOND function without decorator
# Extra code after original function
