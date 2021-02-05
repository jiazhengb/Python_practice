def fibonacci(n):
    '''
    This function will return the list of Fibonacci numbers

    :param n: input int
    :type n: int
    '''
    assert n > 0
    assert isinstance(n, int)
    a , b, c = 1 , 1, 0
    while c < n:
        y = yield a
        x = a + b
        a = b
        b = x
        c += 1
    return y

print(list(fibonacci(3)))