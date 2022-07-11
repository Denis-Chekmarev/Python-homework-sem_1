def getNumber():
    while True:
        day = input('input the day of a week --> ')
        if day.isdigit():
            day = int(day)
            if day > 0 and day < 8:
                return day


day = getNumber()


if day == 6 or day == 7:
    print('It\'s a weekend')
else: 
    print('It\'s weekdays')