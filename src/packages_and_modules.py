import math

# We can look for which functions are implemented in each module by using the dir function:
print(dir(math))
# ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh',
# 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp',
# 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite',
# 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow',
# 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']


# When we find the function in the module we want to use, we can read about it more using the help function
print(help(math.ceil))
# Help on built-in function ceil in module math:
#
# ceil(x, /)
#     Return the ceiling of x as an Integral.
#
#     This is the smallest integer >= x.
#
# None


# The __init__.py file can also decide which modules the package exports as the API, while keeping other modules
# internal, by overriding the __all__ variable, like so:
#
# __init__.py:
#
# __all__ = ["bar"]
