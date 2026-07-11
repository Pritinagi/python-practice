from main_02 import add,div
import pytest

def test_add():
    
    assert add(2,3)==5

def test_add_double():
    
    assert add(10,20)==30

def test_add_negative():
    
     assert add(-5,5)==0

def test_div_zeroes():
    
    with pytest.raises(ZeroDivisionError):
        div(10,0)

test_div_zeroes()



# assert or the condition ==0 is never read it only evaluaes the value div(10,0) and stops right there but if the error doesnt raise then it reacehes to the assert and condition to
# if a function need to raise an excption dont use assert 