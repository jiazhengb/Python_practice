def is_string_integer(i):
    '''
    This function takes a single string character as input and returns True or False 
    if that character represents a valid integer in base 10.

    :param i: input char
    :type i: str
    '''
    assert isinstance(i, str)
    assert len(i) == 1
    return i.isdigit()