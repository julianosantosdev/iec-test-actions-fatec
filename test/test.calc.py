import pytest
from src.calc import add, divide

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0
    
def test_dividir():
    assert dividir(10, 2) == 5
    with pytest.raises(ValueError):
        dividir(10, 0)