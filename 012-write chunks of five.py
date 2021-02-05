import csv
def write_chunks_of_five(words,fname):
    '''
    This function can use corpus of 10,000 common English words
    create a new file that consists of each consecutive non-overlapping 
    sequence of five lines merged into one line.

    :param words: input list of string
    :type words: list

    :param fname: input string
    :type fname: str
    '''
    assert isinstance(words, list)
    for w in words:
        assert isinstance(w, str)
    assert isinstance(fname, str)
    n = 5
    w = [words[i:i + n] for i in range(0, len(words), n)]
    with open(fname, 'w', newline = '') as f:
        a = csv.writer(f, delimiter = ' ')
        a.writerows(w)
