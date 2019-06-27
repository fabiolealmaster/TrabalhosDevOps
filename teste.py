import pytest
import principal 

def test_somar():
    assert principal.somar(2,3)==5
   
def test_subtrair():
    assert principal.subtrair(5,2)==3