from collections import OrderedDict
def gather_values(x):
    '''
    Write a function gather_values that can produce the following output from x:
    {'10': [1, 1, 1, 1, 1],
    '11': [1, 1, 1, 1, 1, 1],        
    '01': [1, 1, 1],                 
    '00': [0, 0, 0, 0, 0, 0]}

    :param x: input list
    :type x: list
    '''
    assert isinstance(x, list)
    for l in x:
        assert isinstance(l, str)
        for i in range(len(l)):
            assert l[i] == '0' or '1'
    assert len(x) > 0
    h = 0
    c = 0
    d = {}
    y = list(dict.fromkeys(x))
    a = []
    ans = []
    for l in x:
        for i in range(len(l)):
            if l[i] == '0':
                h += 1
            else:
                h -= 1
        if h > 0:
            ans.append(0)
        else:
            ans.append(1)
        h = 0

    for i in range(len(y)):
        for z in x:
            if z == y[c]:
                a.append(ans[x.index(z)])
        d[y[c]] = a
        a = []
        c += 1
    return d

def map_bitstring(x):
    '''
    This function takes a list of bitstrings (i.e., 0101) and maps each bitstring 
    to 0 if the number of 0s in the bitstring strictly exceeds the number of 1s.

    :param x: input list
    :type x: list
    '''
    assert isinstance(x, list)
    assert len(x) > 0
    for l in x:
        assert isinstance(l, str)
        for i in range(len(l)):
            assert l[i] == '0' or '1'
    n, h = 0, 0
    ans = []
    co = {}
    x = list(dict.fromkeys(x))
    for l in x:
        for i in range(len(l)):
            if l[i] == '0':
                h += 1
            else:
                h -= 1
        if h > 0:
            ans.append(0)
        else:
            ans.append(1)
        h = 0
    while n < len(x):
        co[str(x[n])] = int(ans[n])
        n+=1
    return co

def threshold_values(seq, threshold=1):
    '''
    Note that 01 corresponding value was set to 0 because it did not have the
    top two most frequent values of 1. If there is a tie, 
    then use the smallest value the tied bitstrings to pick the winner.
    '''
    assert isinstance(seq, list)
    assert isinstance(threshold, int)
    assert len(seq) >= threshold > 0
    i, j, k = [], [], 0
    m = 1
    u = 0
    n = -1
    for s in seq:
        assert '0' or '1' in s
        assert len(s) > 0
    a = gather_values(seq)
    a = dict(OrderedDict(sorted(a.items()))) # order
    keys = list(a.keys())
    values = list(a.values())
    for key in keys:
        a[key] = len(values[k]) 
        k += 1
    b = dict(sorted(a.items(), key=lambda item: item[1])) # order by values
    keys = list(b.keys())
    one = {}
    ma = map_bitstring(seq)
    
    ma = [ma[k] for k in sorted(b, key=b.get)] # mapped list for 0 and 1

    while u < len(ma):
        b[keys[u]] = ma[u]
        u += 1
    u = 1
    while u < threshold+1:
        if list(b.values())[-u] == 1:
            one[list(b.keys())[-u]] = 1
        else:
            continue
        u += 1
    u = 0
    while u < len(ma)-threshold:
        one[list(b.keys())[u]] = 0
        u += 1
    one = dict(OrderedDict(sorted(one.items())))
    return one