def power(a, b):
    if isinstance(a, (int or float)) and isinstance(b, (int or float)):
        def add(a, b):
            num = a
            for i in range(b):
                num += 1
            return num

        def multiply(a, b):
            num = 0
            for i in range(b):
                num = add(num, a)
            return num

        def power(a, b):
            num = 1
            for i in range(b):
                num = multiply(num, a)
            return num
        return power(a, b)
    else:
        raise TypeError("Argument must be integer or float")
print(power(2, 2))
print(power(2, 3))
print(power(2, 0))
print(power(0, 5))
#print(power("a", 5))

