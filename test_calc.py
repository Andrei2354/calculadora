import pytest
from calc import Calculadora

# Fixture sirve para crear una instancia de la calculadora para cada prueba
@pytest.fixture
def calculadora():
    return Calculadora(10, 5)

# Pruebas unitarias para la clase Calculadora
def test_suma(calculadora):
    assert calculadora.suma() == 15

def test_resta(calculadora):
    assert calculadora.resta() == 5

def test_multiplicacion(calculadora):
    assert calculadora.multiplicacion() == 50

def test_division(calculadora):
    assert calculadora.division() == 2

def test_division_por_cero():
    calculadora = Calculadora(10, 0)
    assert calculadora.division() == "Error: No se puede dividir por cero. "

def test_suma_negativa():
    calculadora = Calculadora(-5, 10)
    assert calculadora.suma() == 5

def test_division_decimal():
    calculadora = Calculadora(5, 2)
    assert calculadora.division() == 2.5