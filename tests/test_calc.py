import pytest
from src.calc import add, divide

def test_somar():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    
def test_dividir():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)