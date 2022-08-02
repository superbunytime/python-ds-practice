def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    x = [i for i in range(num)]
    x.pop(x[0])
    y = []
    for i in x:
        if num % i == 0:
            y.append(i)
    y.append(num)
    return y

#comprehensions are scary