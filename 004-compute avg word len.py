def compute_average_word_length(instring,unique=False):
    '''
    The function compute the average length of the words in the input string (instring)
    if unique is True then remove the duplicates word

    :param instring: input str
    :type instring: str

    :param unique: input True/ False
    :type unique: boolean
    '''
    assert isinstance(instring, str)
    assert isinstance(unique, bool)
    words = instring.split()
    if unique is True:
        words = list(dict.fromkeys(words))
    avg = sum(len(word) for word in words) / len(words)
    return avg