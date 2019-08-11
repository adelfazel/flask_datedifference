import sys
from classes.dateclass import DateClass

if __name__ == "__main__":
    dates = []
    print("Enter dates in dd/mm/yyyy format")

    print("Enter the first date:")
    dates.append(sys.stdin.readline().strip())
    print("Enter the second date:")

    dates.append(sys.stdin.readline().strip())

    try:
        Date1 = DateClass(dates[0])
        Date2 = DateClass(dates[1])
        print(Date1.dayDifferece(Date2))
    except TypeError as e:
        print("Nothing to display")
