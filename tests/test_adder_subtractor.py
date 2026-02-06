"""
Pruebas unitarias para el sumador-restador completo.
"""

import pytest
from src.adder_subtractor import sumador_restador_4bits
from src.utils import bits_a_entero, mostrar_operacion


class TestAdderSubtractor:
    """Pruebas para el sumador-restador de 4 bits."""
    
    def test_addition_basic(self):
        """Prueba de suma básica: 5 + 3 = 8."""
        a = [0, 1, 0, 1]  # 5
        b = [0, 0, 1, 1]  # 3
        resultado, carry = sumador_restador_4bits(a, b, operacion=0)
        
        assert resultado == [1, 0, 0, 0]  # 8
        assert carry == 0
        assert bits_a_entero(resultado) == 8
    
    def test_subtraction_basic(self):
        """Prueba de resta básica: 7 - 2 = 5."""
        a = [0, 1, 1, 1]  # 7
        b = [0, 0, 1, 0]  # 2
        resultado, carry = sumador_restador_4bits(a, b, operacion=1)
        
        assert resultado == [0, 1, 0, 1]  # 5
        assert carry == 1  # En resta, carry=1 indica resultado positivo
        assert bits_a_entero(resultado, es_resta=True, cout=carry) == 5
    
    def test_subtraction_negative(self):
        """Prueba de resta con resultado negativo: 2 - 7 = -5."""
        a = [0, 0, 1, 0]  # 2
        b = [0, 1, 1, 1]  # 7
        resultado, carry = sumador_restador_4bits(a, b, operacion=1)
        
        assert resultado == [1, 0, 1, 1]  # -5 en complemento a 2
        assert carry == 0  # En resta, carry=0 indica resultado negativo
        assert bits_a_entero(resultado, es_resta=True, cout=carry) == -5
    
    def test_subtraction_zero(self):
        """Prueba de resta dando cero: 5 - 5 = 0."""
        a = [0, 1, 0, 1]  # 5
        b = [0, 1, 0, 1]  # 5
        resultado, carry = sumador_restador_4bits(a, b, operacion=1)
        
        assert resultado == [0, 0, 0, 0]  # 0
        assert carry == 1  # Resultado positivo (cero)
        assert bits_a_entero(resultado, es_resta=True, cout=carry) == 0
    
    def test_addition_overflow(self):
        """Prueba de overflow en suma: 8 + 8 = 16 (overflow)."""
        a = [1, 0, 0, 0]  # 8
        b = [1, 0, 0, 0]  # 8
        resultado, carry = sumador_restador_4bits(a, b, operacion=0)
        
        # En overflow, el resultado es incorrecto
        assert resultado == [0, 0, 0, 0]  # 0 (incorrecto)
        assert carry == 1  # Hay overflow
    
    def test_subtraction_overflow_positive(self):
        """Prueba de overflow positivo en resta: 7 - (-8) = 15."""
        a = [0, 1, 1, 1]  # 7
        b = [1, 0, 0, 0]  # -8 en complemento a 2
        resultado, carry = sumador_restador_4bits(a, b, operacion=1)
        
        # 7 - (-8) = 15
        assert resultado == [1, 1, 1, 1]  # 15
        assert carry == 1  # Resultado positivo
    
    @pytest.mark.parametrize("a,b,operacion,expected_result,expected_carry", [
        # Sumas
        ([0,0,0,0], [0,0,0,0], 0, [0,0,0,0], 0),  # 0 + 0
        ([0,0,0,1], [0,0,0,1], 0, [0,0,1,0], 0),  # 1 + 1
        ([0,1,0,1], [0,0,1,0], 0, [0,1,1,1], 0),  # 5 + 2
        ([1,1,1,1], [0,0,0,1], 0, [0,0,0,0], 1),  # 15 + 1 (overflow)
        
        # Restas
        ([0,0,0,0], [0,0,0,0], 1, [0,0,0,0], 1),  # 0 - 0
        ([0,0,0,1], [0,0,0,1], 1, [0,0,0,0], 1),  # 1 - 1
        ([0,1,0,1], [0,0,1,0], 1, [0,0,1,1], 1),  # 5 - 2
        ([0,0,1,0], [0,1,0,1], 1, [1,0,1,1], 0),  # 2 - 5 = -3
    ])
    def test_adder_subtractor_parametrized(self, a, b, operacion, 
                                           expected_result, expected_carry):
        """Prueba paramétrica del sumador-restador."""
        resultado, carry = sumador_restador_4bits(a, b, operacion)
        assert resultado == expected_result
        assert carry == expected_carry
    
    def test_invalid_operation(self):
        """Prueba que se valide la operación."""
        with pytest.raises(ValueError):
            sumador_restador_4bits([0,0,0,0], [0,0,0,0], 2)
    
    def test_invalid_input_length(self):
        """Prueba que se valide la longitud de entrada."""
        with pytest.raises(ValueError):
            sumador_restador_4bits([0,0,0], [0,0,0,0], 0)
    
    def test_bits_a_entero_function(self):
        """Prueba la función de conversión bits_a_entero."""
        # Números positivos
        assert bits_a_entero([0,0,0,0]) == 0
        assert bits_a_entero([0,1,0,1]) == 5
        assert bits_a_entero([1,1,1,1]) == 15
        
        # Números negativos (complemento a 2)
        assert bits_a_entero([1,1,1,1], es_resta=True, cout=0) == -1
        assert bits_a_entero([1,0,1,1], es_resta=True, cout=0) == -5
        assert bits_a_entero([1,0,0,0], es_resta=True, cout=0) == -8
        
        # Cero en resta
        assert bits_a_entero([0,0,0,0], es_resta=True, cout=1) == 0
    
    def test_mostrar_operacion_no_crash(self):
        """Prueba que mostrar_operacion no falle."""
        # Solo verificamos que no lance excepciones
        a = [0, 1, 0, 1]
        b = [0, 0, 1, 1]
        resultado = [1, 0, 0, 0]
        
        # No podemos verificar la salida, pero podemos verificar que no falle
        try:
            mostrar_operacion(a, b, resultado, 0, 0)
            assert True  # Si llegamos aquí, no falló
        except Exception:
            assert False, "mostrar_operacion lanzó una excepción"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])