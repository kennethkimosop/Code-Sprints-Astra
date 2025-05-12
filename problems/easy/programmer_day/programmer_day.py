def dayOfProgrammer(year):
    # Transition year (Julian to Gregorian)
    if year == 1918:
        return "26.09.1918"
    
    # Julian calendar
    if year < 1918:
        if year % 4 == 0:
            return "12.09." + str(year)
        else:
            return "13.09." + str(year)
    
    # Gregorian calendar
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return "12.09." + str(year)
    else:
        return "13.09." + str(year)

print(dayOfProgrammer(2017))   # Output: 13.09.2017 (non-leap year - Gregorian)
print(dayOfProgrammer(1800))   # Output: 12.09.1800 (leap year - Julian)
print(dayOfProgrammer(1900))   # Output: 12.09.1900 (leap year - Julian)

