from random import choices
def get_sample(nbits=3,prob=None,n=1):
    '''
    Given a number of bits, write the get_sample function to return a 
    list n of random samples from a finite probability mass function 
    defined by a dictionary with keys defined by a specified number of bits.

    :param nbits: input int
    :type nbits: int

    :param prob: input dict
    :type prob: dict

    :param n: input int
    :type n: int
    '''
    assert isinstance(nbits, int)
    assert isinstance(prob, dict)
    assert isinstance(n, int)
    assert 0 < n
    assert 0 < nbits
    for i in list(prob.keys()):
        assert len(i) == nbits
    assert sum(list(prob.values())) == 1
    assert len(list(prob.keys())) == 2**nbits
    ans, a = [], []
    value = list(prob.values())
    key = list(prob.keys())
    for k in key:
        i = int(k)
        a.append(i)
    for i in range(n):
        c = str(choices(a, value)[0])
        c = c.zfill(nbits)
        ans.append(c)
    return ans

