for _ in [1, 2, 3]:
    print("hello")
# hello
# hello
# hello

for (a, b) in [(1, "a"), (2, "b"), (3, "c")]:
    print(f"a={a}, b={b}")
# a=1, b=a
# a=2, b=b
# a=3, b=c

for a, b in [(1, "a"), (2, "b"), (3, "c")]:
    print(f"a={a}, b={b}")
# a=1, b=a
# a=2, b=b
# a=3, b=c

for key, value in {"a": 1, "b": 2, "c": 3}.items():
    print(f"key={key}, value={value}")
# key=a, value=1
# key=b, value=2
# key=c, value=3

x = 0
while x < 5:
    print(f"Increase x={x}")
    x += 1
else:
    print("x is bigger than 5")
# Increase x=0
# Increase x=1
# Increase x=2
# Increase x=3
# Increase x=4
# x is bigger than 5


for num in range(0, 10, 4):
    print(num)
# 0
# 4
# 8

print(list(range(0, 10, 4)))
# [0, 4, 8]


test_string = "abc"
for letter in enumerate(test_string):
    print(letter)
# (0, 'a')
# (1, 'b')
# (2, 'c')

for index, letter in enumerate(test_string):
    print(f"index = {index}, letter = {letter}")
# index = 0, letter = a
# index = 1, letter = b
# index = 2, letter = c

list_test1 = [1, 2, 3]
list_test2 = ["a", "b", "c"]

zipped = zip(list_test1, list_test2)
print(zipped)
# <zip object at 0x7fd0e016bc00>
for item in zipped:
    print(item)
# (1, 'a')
# (2, 'b')
# (3, 'c')

print("x" in list_test1)
# False
print(2 in list_test1)
# True
print("key1" in {"key1": 1})
# True

from random import shuffle, randint

list_test3 = [1, 2, 3, 4, 5, 6]
shuffle(list_test3)
print(list_test3)
# [5, 6, 1, 2, 4, 3]
print(randint(1, 10))
# 5

# input_value = input("what is you name?") todo uncomment
# print(input_value) todo uncomment
# Vlad
