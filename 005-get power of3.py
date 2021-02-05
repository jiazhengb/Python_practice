def get_power_of3(i):
    '''
    Given a set of weights {1,3,9,27}, and this 
    function can construct any number between 1 and 40.

    :param i: input int
    :type i: int
    '''
    assert isinstance(i, int)
    assert 0 < i < 41
    given = [1, 3, 9, 27]
    ns = [-1, 0, 1]
    arr = [0, 0, 0, 0]
    for n0 in ns:
        for n1 in ns:
            for n2 in ns:
                for n3 in ns:
                    arr[0] = n0
                    arr[1] = n1
                    arr[2] = n2
                    arr[3] = n3
                    ans = sum([a*b for a, b in zip(arr, given)])
                    if i == ans:
                        return arr