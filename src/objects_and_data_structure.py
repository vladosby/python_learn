# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp
string = "hello world"

# slicing [start:stop:step]

print(string[-2])
# l
print(string[0:-2])
# hello wor
print(string[0:len(string):2])
# hlowrd
print(string[4:])
# o world
print(string[:4])
# hell
print(string[::2])
# hlowrd
print(string[::-1])
# dlrow olleh

print("This is {}, that is {}".format("string format", "formatted"))
# This is string format, that is formatted

print("This is {1}, that is {0}".format("string format", "formatted"))
# This is formatted, that is string format

print("This is {first}, that is {any}".format(first="string format", any="formatted"))
# This is string format, that is formatted

# float formatting {value:width.precision f}
float_value = 100 / 13
print("Not formatted double {}".format(float_value))
# Not formatted double 7.6923076923076925
print("Formatted double {r:1.2f}".format(r=float_value))
# Formatted double 7.69
print("Formatted double {r:10.2f}".format(r=float_value))
# Formatted double       7.69
print('This is my ten-character, two-decimal number:{0:10.2f}'.format(float_value))
# This is my ten-character, two-decimal number:      7.69
print("I'm going to inject %s here." % 'something')
# I'm going to inject something here.
print("I'm going to inject %s text here, and %s text here." % ('some', 'more'))
# I'm going to inject some text here, and more text here.
print('{0:<8} | {1:^8} | {2:>8}'.format('Left', 'Center', 'Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11, 22, 33))
# Left     |  Center  |    Right
# 11       |    22    |       33

print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left', 'Center', 'Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11, 22, 33))
# Left==== | -Center- | ...Right
# 11====== | ---22--- | ......33

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.keys())
# dict_keys(['a', 'b', 'c'])
print(my_dict.values())
# dict_values([1, 2, 3])
print(my_dict.items())
# dict_items([('a', 1), ('b', 2), ('c', 3)])
print(list(my_dict.values())[0])
#  1

my_tuple = (1, 2, 3, 1, 2, 1)
print(my_tuple.count(1))
# 3
print(my_tuple.index(2))
# 1
print(my_tuple[4])
# 2

my_set = {1, 1, 1, 2, 2, 2}
print(my_set)
# {1, 2}
my_set.add(5)
print(my_set)
# {1, 2, 5}
my_set.add(1)
print(my_set)
# {1, 2, 5}

my_set2 = set()
my_set2.add(1)
my_set2.add(1)
my_set2.add(3)
print(my_set2)
# {1, 3}
