import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from classes.dateclass import DateClass

import random
import time
import datetime
timeFormat = '%d/%m/%Y'
minDate = "01/01/1901"
maxDate = "31/12/2999"


def getRandomDate():
    stime = time.mktime(time.strptime(minDate, timeFormat))
    etime = time.mktime(time.strptime(maxDate, timeFormat))
    ptime = stime + random.random() * (etime - stime )
    return ptime


def daysBetweenByPython(d1, d2):
    d1=datetime.datetime.strptime(time.strftime(timeFormat, time.localtime(d1)),timeFormat)
    d2=datetime.datetime.strptime(time.strftime(timeFormat, time.localtime(d2)),timeFormat)
    return max(abs(d2 - d1).days-1,0)

def daysBetweenByMe(d1, d2):
    d1=time.strftime(timeFormat, time.localtime(d1))
    d2=time.strftime(timeFormat, time.localtime(d2))
    return DateClass(d1).dayDifferece(DateClass(d2))


def test_stree():
    N = 1000
    for _ in range(N):
        d1 = getRandomDate()
        d2 = getRandomDate()
        d1String = time.strftime(timeFormat, time.localtime(d1))
        d2String = time.strftime(timeFormat, time.localtime(d2))
        print(f"Testing difference between dates {d1String} and {d2String} yield the same results")
        assert daysBetweenByPython(d1, d2)==daysBetweenByMe(d1, d2)
