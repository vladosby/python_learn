def cubes_generator(n: int):
    for x in range(1, n):
        yield x ** 3


print(cubes_generator(5))
# <generator object cubes_generator at 0x7f9e88304f90>

for v in cubes_generator(5):
    print(v)
# 1
# 8
# 27
# 64

print(list(cubes_generator(5)))


# [1, 8, 27, 64]

def fib(n):
    a = 1
    b = 1

    for i in range(n):
        yield a
        a, b = b, a + b  # Next execution resumes
        # from this point


for f in fib(5):
    print(f)

# 1
# 1
# 2
# 3
# 5
