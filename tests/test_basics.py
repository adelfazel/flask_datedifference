import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from classes.dateclass import DateClass

def test_static1():
    d0 = DateClass("02/06/1983")
    d1 = DateClass("22/06/1983")
    assert d0.dayDifferece(d1)==19

def test_static2():
    d0 = DateClass("04/07/1984")
    d1 = DateClass("25/12/1984")
    assert d0.dayDifferece(d1)==173

def test_static3():
    d0 = DateClass("03/01/1989")
    d1 = DateClass("03/08/1983")
    assert d0.dayDifferece(d1)==1979
