def compute_sum_to_n(n):
    '''
    This function computes the sum of all non-negative 
    integers up to and including a specified value, n.

    :param n: input number
    :type n: int
    '''
    assert isinstance(n, int)
    assert n >= 0
    result = 0
    for i in range(0, n+1):
        result = result + i
        i += 1
    return result