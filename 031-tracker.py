from collections.abc import Iterable
from time import sleep
import random
from datetime import datetime
import itertools as it
def producer():
    'produce timestamps'
    starttime = datetime.now()
    while True:
        sleep(random.uniform(0,0.2))
        yield datetime.now()-starttime

def tracker(p, limt=1):
    ''' 
    A generator that tracks the output of this producer and ultimately 
    returns the number of odd numbered seconds that have been iterated over.

    :param p: input generator
    :type p: generator

    :param day: input int
    :type day: int
    '''
    assert limt > 0
    assert isinstance(limt, int)
    assert isinstance(p, Iterable)
    c = 0
    h = limt
    limt = yield limt
    if limt == None:
        limt = h
    while c < limt:
        t = next(p).seconds
        if t % 2 != 0:
            c += 1
            yield c