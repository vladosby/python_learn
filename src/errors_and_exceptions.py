def square(num):
    if num < 10:
        raise Exception("Number too big")
    else:
        return num ** 2


try:
    print(f"function result {square(11)}")
except Exception:
    print("Exception caught")
else:
    print("No exception caught")
finally:
    print("I am working always")
# function result 121
# No exception caught
# I am working always

try:
    print(f"function result {square(5)}")
except Exception:
    print("Exception caught")
else:
    print("No exception caught")
finally:
    print("I am working always")
# Exception caught
# I am working always


# Run Pylint analizer
# pylint src/errors_and_exceptions.py -r y
