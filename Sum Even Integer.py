def sum_even_int(x):
    x = str(x)
    total = 0
    for i in x:
        i = int(i)
        if i % 2 == 0:
            total += i
    return total
print(sum_even_int(234578))

