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
