from functools import reduce

accptableYearRange = range(1901,3000)
accptableMonthRange =  range(1,13)
daysInNormalYear, daysInLeapYear = 365, 366

def ilen(iterable): # geeky way of finding length of iterable class
    return reduce(lambda sum, element: sum + 1, iterable, 0)

def isLeapYear(year):
    if (year % 4)!=0:
        return False
    elif (year % 100) != 0:
        return True
    elif (year % 400) != 0:
        return False
    else:
        return True

def numDaysInMonth(year,month):
    maxDays = [31,0 ,31,30,31,30,
               31,31,30,31,30,31]
    allowedDays =  {}
    for m in accptableMonthRange:
        allowedDays[m] = range(1,maxDays[m-1]+1)
    if isLeapYear(year):
        allowedDays[2]=range(1,30)
    else:
        allowedDays[2]=range(1,29)
    return allowedDays

class DateClass():
    def __init__(self,dateString):
        self.day,self.month,self.year = self.validateAndParseInput(dateString)

    def numYearsSinceBegining(self):
        years = int(self.year)

        numLeapYears= ilen(filter(isLeapYear,range(min(accptableYearRange),years)))
        years -= numLeapYears
        return years, numLeapYears

    def numDaysHaveElapsedThisYear(self):
        maxDays = numDaysInMonth(self.year,self.month)
        daysSoFar = int(self.day)
        for m in range(1,self.month):
            daysSoFar+=len(maxDays[m])
        return daysSoFar

    def daysSince1901(self):
        normalYears, leapYears = self.numYearsSinceBegining()
        return self.numDaysHaveElapsedThisYear() \
            +leapYears*daysInLeapYear \
            +normalYears*daysInNormalYear

    def validateAndParseInput(self,dateString):
        try:
            day,month,year = dateString.split("/")
            if not (day.isdigit() and month.isdigit() and month.isdigit()) :
                raise ValueError("invalid content; ensure content are digits")
            day,month,year = int(day),int(month),int(year)
            if year not in accptableYearRange:
                raise ValueError("invalid year range")
            if month not in accptableMonthRange:
                raise ValueError("invalid month range")
            daysAllowed = numDaysInMonth(year,month)
            if day not in daysAllowed[month]:
                raise ValueError("invalid day entered")
            return day,month,year
        except ValueError as e:
            print(f"Unable to parse {dateString}; stackTrace: {e};")

    def dayDifferece(self, otherDate):
        d1,d2  = self.daysSince1901(), otherDate.daysSince1901()
        return max(abs(d2-d1)-1,0)

if __name__ == "__main__":
    pass
