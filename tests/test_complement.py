"""
Pruebas unitarias para los circuitos de complemento.
"""

import pytest
from src.complement import complemento_a_1, complemento_a_2
from src.adder_4bit import adder_4bits


class TestComplementoA1:
    """Pruebas para el complemento a 1."""
    
    @pytest.mark.parametrize("bits,expected", [
        ([0,0,0,0], [1,1,1,1]),  # 0 -> 15
        ([0,0,0,1], [1,1,1,0]),  # 1 -> 14
        ([0,1,0,1], [1,0,1,0]),  # 5 -> 10
        ([1,0,0,0], [0,1,1,1]),  # 8 -> 7
        ([1,1,1,1], [0,0,0,0]),  # 15 -> 0
    ])
    def test_complemento_a_1_parametrized(self, bits, expected):
        """Prueba paramétrica del complemento a 1."""
        resultado = complemento_a_1(bits)
        assert resultado == expected
    
    def test_complemento_a_1_property(self):
        """Prueba la propiedad: complemento_a_1(complemento_a_1(x)) = x."""
        test_cases = [
            [0,0,0,0],
            [0,0,0,1],
            [0,1,0,1],
            [1,0,0,0],
            [1,1,1,1],
        ]
        
        for bits in test_cases:
            comp1 = complemento_a_1(bits)
            comp1_comp1 = complemento_a_1(comp1)
            assert comp1_comp1 == bits, \
                f"Complemento doble falló para {bits}"


class TestComplementoA2:
    """Pruebas para el complemento a 2."""
    
    @pytest.mark.parametrize("bits,expected", [
        ([0,0,0,0], [0,0,0,0]),  # 0 -> 0
        ([0,0,0,1], [1,1,1,1]),  # 1 -> -1
        ([0,1,0,1], [1,0,1,1]),  # 5 -> -5
        ([1,0,0,0], [1,0,0,0]),  # 8 -> -8
        ([1,1,1,1], [0,0,0,1]),  # 15 -> 1
    ])
    def test_complemento_a_2_parametrized(self, bits, expected):
        """Prueba paramétrica del complemento a 2."""
        resultado = complemento_a_2(bits)
        assert resultado == expected
    
    def test_complemento_a_2_negation_property(self):
        """
        Prueba la propiedad: x + complemento_a_2(x) = 0 (módulo 16).
        
        En complemento a 2, un número sumado con su complemento
        debería dar 0 (con carry ignorado).
        """
        test_cases = [
            [0,0,0,1],  # 1
            [0,1,0,1],  # 5
            [1,0,0,0],  # 8
            [1,0,1,0],  # 10
        ]
        
        for bits in test_cases:
            comp2 = complemento_a_2(bits)
            suma, cout = adder_4bits(bits, comp2, 0)
            
            # Debería dar 0 (ignorando el carry)
            assert suma == [0, 0, 0, 0], \
                f"{bits} + complemento_a_2({bits}) != 0"
    
    def test_complemento_a_2_double_negation(self):
        """Prueba que complemento_a_2(complemento_a_2(x)) = x."""
        test_cases = [
            [0,0,0,1],  # 1
            [0,1,0,1],  # 5
            [1,0,0,0],  # 8 (caso especial)
            [1,0,1,0],  # 10
        ]
        
        for bits in test_cases:
            comp2 = complemento_a_2(bits)
            comp2_comp2 = complemento_a_2(comp2)
            assert comp2_comp2 == bits, \
                f"Doble complemento falló para {bits}"
    
    def test_invalid_input(self):
        """Prueba que las funciones validen la entrada."""
        # Lista con longitud incorrecta
        with pytest.raises(ValueError):
            complemento_a_1([0, 0, 0])
        
        with pytest.raises(ValueError):
            complemento_a_2([0, 0, 0])


if __name__ == "__main__":
    pytest.main([__file__, "-v"])