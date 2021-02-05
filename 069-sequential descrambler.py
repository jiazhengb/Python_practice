import itertools as it
from itertools import combinations
from itertools import permutations
from collections import defaultdict
from collections import Counter
def descrambler(w,k):
    '''
    You are given a sequence of n lower-case letters and a k-tuple of 
    integers that indicate partition-lengthsof the sequence. 
    Also, you have a dictionary of commonly used words.
    '''
    assert isinstance(w, str)
    assert w.isalpha() # check a-z
    assert isinstance(k, tuple)
    for t in k:
        assert t > 0
        assert isinstance(t, int) # check if int
    assert len(w) == sum(k)
    with open("/tmp/google-10000-english-no-swears.txt", "r") as file:
        allText = file.read()
        dict_words = list(map(str, allText.split())) # all words in dict
    d = defaultdict(list)
    for i in dict_words:
        d[tuple(sorted(tuple(i)))].append(i)
    z = sorted(w)
    w = tuple(sorted(w))
    p = []
    for i in k:
        for j in list(combinations(w, i)):
            j = tuple(sorted(j))
            if d[j] != [] and d[j] not in p:
                p.append(d[j])
    alltext = [item for sublist in p for item in sublist]
    n = 0
    for i in k:
        c = Counter(list(k))
        if c[i] > 1:
            n += 1
    if n == 0:
        pos = list(combinations(alltext, len(k)))
    else:
        pos = list(permutations(alltext, len(k)))
    for i in pos:
        if sorted(''.join(i)) == z:
            i = ' '.join(i)
            yield i
print(list(descrambler('choeounokeoitg',(4,4,6))))