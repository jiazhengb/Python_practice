import csv
def write_columns(data, fname):
    '''
    This function can write the following formula to 
    three columns to a comma-separated file: 
    data_value, data_value**2, (data_value+data_value**2)/3

    :param data: input list of int ot float 
    :type data: list

    :param fname: input string
    :type fname: str
    '''
    assert isinstance(data, list)
    assert isinstance(fname, str)
    for d in data:
        assert isinstance(d, int) or isinstance(d, float)
    holder = []
    n = 3
    for i in data:
        holder.insert(0, i)
        holder.insert(0, i**2)
        holder.insert(0, (i+i**2)/3.0)
    holder.reverse()
    fholder = [holder[i:i + n] for i in range(0, len(holder), n)]
    for x in fholder:
        for t in x:
            if isinstance(t, float):
                x[x.index(t)] = format(t, '.2f')
    with open(fname, 'w', newline = '') as f:
        a = csv.writer(f, delimiter = ',')
        a.writerows(fholder)

write_columns([1,2.2,3.5,5.7], 'a')