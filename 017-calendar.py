import calendar
def number_of_days(year, month):
    '''
    Function that returns the number of calendar days in a given year and month

    :param year: input int
    :type year: int

    :param month: input int
    :type month: int
    '''
    assert isinstance(year, int)
    assert isinstance(month, int)
    assert year >= 0
    assert 0 < month < 13
    return calendar.monthrange(year, month)[1]

# print(number_of_days(1997,12))

def number_of_leap_years(year1,year2):
    '''
    function to find the number of leap-years 
    between (including both endpoints) two given years

    :param year1: input int
    :type year1: int

    :param year2: input int
    :type year2: int
    '''
    assert isinstance(year1, int)
    assert isinstance(year2, int)
    assert year2 >= year1 >= 0
    assert year2 >= 0
    c = 0
    years = list(range(year1, year2 + 1))
    for year in years:
        if calendar.isleap(year) is True:
            c += 1
    return c

# print(number_of_leap_years(-1, 2020))

def get_day_of_week(year, month, day):
    '''
    function to find the string name (e.g., Monday, Tuesday) 
    of the day of the week on a given month,day, and year

    :param year: input int
    :type year: int

    :param month: input int
    :type month: int

    :param day: input int
    :type day: int
    '''
    assert isinstance(year, int)
    assert isinstance(month, int)
    assert isinstance(day, int)
    assert 0 < month < 13
    assert year >= 0
    assert 0 < day < number_of_days(year, month)
    c = calendar.weekday(year, month, day)
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return weekdays[c]

print(get_day_of_week(0, 2, 29))