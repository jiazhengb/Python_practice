from itertools import islice
def slide_window(x, width, increment):
    '''
    This function will turn input string into smaller strings 
    with length of input width and each string have increment.
    Then return a big string with little strings.

    :param x: input list
    :type x: list

    :param n: input int
    :type n: int

    :param n: input int
    :type n: int
    '''
    assert increment > 0
    assert len(x) >= width > 0 
    assert isinstance(x, list)
    assert isinstance(increment, int)
    assert isinstance(width, int)

    i, a, b = 0, 0, width
    r = []
    while i < len(x):
        r.append(x[a:b])
        i += 1
        if len(x[a:b]) < width:
            break
        a += increment
        b += increment
    r.pop()
    return r

x = [1,2,3,4,5,6,7,8,9,10]
print(slide_window(x, 3, 1))