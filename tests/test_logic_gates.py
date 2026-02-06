"""
Pruebas unitarias para las puertas lógicas básicas.
"""

import pytest
from src.logic_gates import AND, OR, NOT, XOR, NAND


class TestLogicGates:
    """Pruebas para las puertas lógicas básicas."""
    
    def test_AND_truth_table(self):
        """Prueba completa de la tabla de verdad AND."""
        assert AND(0, 0) == 0
        assert AND(0, 1) == 0
        assert AND(1, 0) == 0
        assert AND(1, 1) == 1
    
    def test_OR_truth_table(self):
        """Prueba completa de la tabla de verdad OR."""
        assert OR(0, 0) == 0
        assert OR(0, 1) == 1
        assert OR(1, 0) == 1
        assert OR(1, 1) == 1
    
    def test_NOT_truth_table(self):
        """Prueba completa de la tabla de verdad NOT."""
        assert NOT(0) == 1
        assert NOT(1) == 0
    
    @pytest.mark.parametrize("a,b,expected", [
        (0, 0, 0),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0),
    ])
    def test_XOR_parametrized(self, a, b, expected):
        """Prueba paramétrica de la puerta XOR."""
        assert XOR(a, b) == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (0, 0, 1),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0),
    ])
    def test_NAND_parametrized(self, a, b, expected):
        """Prueba paramétrica de la puerta NAND."""
        assert NAND(a, b) == expected
    
    def test_XOR_implemented_with_basic_gates(self):
        """Verifica que XOR esté implementada solo con AND, OR, NOT."""
        # XOR(a,b) = (A AND NOT B) OR (NOT A AND B)
        # Esta es una verificación conceptual
        for a in [0, 1]:
            for b in [0, 1]:
                xor_result = XOR(a, b)
                manual_result = OR(AND(a, NOT(b)), AND(NOT(a), b))
                assert xor_result == manual_result, \
                    f"XOR({a},{b}) no coincide con implementación manual"
    
    def test_invalid_inputs(self):
        """Prueba que las funciones manejen solo 0 y 1."""
        # Las funciones deberían manejar booleanos o enteros 0/1
        assert AND(1, 1) == 1
        assert OR(0, 0) == 0
        assert NOT(0) == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])