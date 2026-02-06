"""
Pruebas unitarias para los sumadores.
"""

import pytest
from src.half_adder import half_adder
from src.full_adder import full_adder
from src.adder_4bit import adder_4bits, bits_a_decimal


class TestHalfAdder:
    """Pruebas para el medio sumador."""
    
    def test_half_adder_truth_table(self):
        """Prueba la tabla de verdad del half adder."""
        # Caso 0,0
        suma, carry = half_adder(0, 0)
        assert suma == 0 and carry == 0
        
        # Caso 0,1
        suma, carry = half_adder(0, 1)
        assert suma == 1 and carry == 0
        
        # Caso 1,0
        suma, carry = half_adder(1, 0)
        assert suma == 1 and carry == 0
        
        # Caso 1,1
        suma, carry = half_adder(1, 1)
        assert suma == 0 and carry == 1
    
    @pytest.mark.parametrize("a,b,expected_sum,expected_carry", [
        (0, 0, 0, 0),
        (0, 1, 1, 0),
        (1, 0, 1, 0),
        (1, 1, 0, 1),
    ])
    def test_half_adder_parametrized(self, a, b, expected_sum, expected_carry):
        """Prueba paramétrica del half adder."""
        suma, carry = half_adder(a, b)
        assert suma == expected_sum
        assert carry == expected_carry


class TestFullAdder:
    """Pruebas para el sumador completo."""
    
    @pytest.mark.parametrize("a,b,cin,expected_sum,expected_cout", [
        (0, 0, 0, 0, 0),
        (0, 0, 1, 1, 0),
        (0, 1, 0, 1, 0),
        (0, 1, 1, 0, 1),
        (1, 0, 0, 1, 0),
        (1, 0, 1, 0, 1),
        (1, 1, 0, 0, 1),
        (1, 1, 1, 1, 1),
    ])
    def test_full_adder_parametrized(self, a, b, cin, expected_sum, expected_cout):
        """Prueba paramétrica del full adder."""
        suma, cout = full_adder(a, b, cin)
        assert suma == expected_sum
        assert cout == expected_cout


class Test4BitAdder:
    """Pruebas para el sumador de 4 bits."""
    
    def test_adder_4bits_basic(self):
        """Prueba básica del sumador de 4 bits."""
        # 5 + 3 = 8
        a = [0, 1, 0, 1]  # 5
        b = [0, 0, 1, 1]  # 3
        resultado, cout = adder_4bits(a, b)
        
        assert resultado == [1, 0, 0, 0]  # 8
        assert cout == 0
    
    def test_adder_4bits_with_carry(self):
        """Prueba del sumador de 4 bits con acarreo de entrada."""
        # 5 + 3 + 1 = 9
        a = [0, 1, 0, 1]  # 5
        b = [0, 0, 1, 1]  # 3
        resultado, cout = adder_4bits(a, b, cin=1)
        
        assert resultado == [1, 0, 0, 1]  # 9
        assert cout == 0
    
    def test_adder_4bits_overflow(self):
        """Prueba de overflow en el sumador de 4 bits."""
        # 8 + 8 = 16 (overflow)
        a = [1, 0, 0, 0]  # 8
        b = [1, 0, 0, 0]  # 8
        resultado, cout = adder_4bits(a, b)
        
        # En overflow, el resultado es incorrecto pero hay carry
        assert resultado == [0, 0, 0, 0]  # 0 (incorrecto debido a overflow)
        assert cout == 1  # Hay carry
    
    @pytest.mark.parametrize("a,b,cin,expected_result,expected_cout", [
        ([0,0,0,0], [0,0,0,0], 0, [0,0,0,0], 0),  # 0 + 0
        ([0,0,0,1], [0,0,0,1], 0, [0,0,1,0], 0),  # 1 + 1
        ([1,0,0,0], [1,0,0,0], 0, [0,0,0,0], 1),  # 8 + 8 (overflow)
        ([1,1,1,1], [0,0,0,1], 0, [0,0,0,0], 1),  # 15 + 1 (overflow)
    ])
    def test_adder_4bits_parametrized(self, a, b, cin, expected_result, expected_cout):
        """Prueba paramétrica del sumador de 4 bits."""
        resultado, cout = adder_4bits(a, b, cin)
        assert resultado == expected_result
        assert cout == expected_cout
    
    def test_adder_4bits_invalid_input(self):
        """Prueba que el sumador valide la entrada."""
        # Lista con longitud incorrecta
        with pytest.raises(ValueError):
            adder_4bits([0, 0, 0], [0, 0, 0, 0])
        
        # Lista con bits inválidos
        with pytest.raises(ValueError):
            adder_4bits([0, 2, 0, 0], [0, 0, 0, 0])
    
    def test_bits_a_decimal(self):
        """Prueba la conversión de bits a decimal."""
        assert bits_a_decimal([0, 0, 0, 0]) == 0
        assert bits_a_decimal([0, 0, 0, 1]) == 1
        assert bits_a_decimal([0, 1, 0, 1]) == 5
        assert bits_a_decimal([1, 0, 0, 0]) == 8
        assert bits_a_decimal([1, 1, 1, 1]) == 15


if __name__ == "__main__":
    pytest.main([__file__, "-v"])