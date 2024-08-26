import pytest 

from openai3 import FancyMap
  
#defining a function with parameter x 
def func(x): 
    return x+5
  
#defining an another function   
def test_method(): 
#check whether 3+5 = 8 or not by passing 3 as an argument in function x 
    assert func(3) == 8

def test_put():
    fm = FancyMap()

    result = fm.put('AI', 'A')
    assert len(result) == 2
    assert result[0] == 2
    assert result[1] == 'A'


def test_get1():
    fm = FancyMap()

    result = fm.get('BOGUS')
    assert result is None


def test_get2():
    fm = FancyMap()

    fm.put('AI', 'A')
    fm.put('AI', 'B')
    fm.put('AI', 'C')

    result = fm.get('AI')
    assert result is not None
    assert result[0] == 6
    assert result[1] == 'C'

    result = fm.get('AI', 7)
    assert result is not None
    assert result[0] == 6
    assert result[1] == 'C'

    result = fm.get('AI', 6)
    assert result is not None
    assert result[0] == 6
    assert result[1] == 'C'

    result = fm.get('AI', 5)
    assert result is not None
    assert result[0] == 4
    assert result[1] == 'B'

    result = fm.get('AI', 4)
    assert result is not None
    assert result[0] == 4
    assert result[1] == 'B'

    result = fm.get('AI', 3)
    assert result is not None
    assert result[0] == 2
    assert result[1] == 'A'
