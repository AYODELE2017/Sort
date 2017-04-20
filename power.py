def power(a, b):
    if isinstance(a, int or float) and isinstance(b, int or float):
        if b == 1:
            return a

        if b == 0:
            return 1

        if a == 0:
            return 0

        if b != 1:
            return a * power(a, b - 1)
    else:
        raise TypeError("Argument must be integer or float")
print(power(2, 3))
print(power(2, 1))
print(power(2, 0))
print(power(0, 3))