def centuryFromYear(year):
    if year % 100 == 0:
        return year/100
    else:
        return int(year/100 + 1)

'''Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

Example
For year = 1905, the output should be
centuryFromYear(year) = 20;
For year = 1700, the output should be
centuryFromYear(year) = 17.'''