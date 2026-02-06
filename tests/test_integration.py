"""
Pruebas de integración para el sistema completo.
"""

import pytest
from src.logic_gates import AND, OR, NOT, XOR
from src.half_adder import half_adder
from src.full_adder import full_adder
from src.adder_4bit import adder_4bits
from src.complement import complemento_a_2
from src.adder_subtractor import sumador_restador_4bits
from src.utils import bits_a_entero, mostrar_operacion


class TestIntegration:
    """Pruebas de integración del sistema completo."""
    
    def test_complete_flow_addition(self):
        """
        Prueba el flujo completo para una suma.
        Verifica que todas las capas funcionen correctamente juntas.
        """
        # Datos de prueba: 5 + 3 = 8
        a = [0, 1, 0, 1]  # 5
        b = [0, 0, 1, 1]  # 3
        
        # 1. Usar el sumador-restador
        resultado, cout = sumador_restador_4bits(a, b, operacion=0)
        
        # 2. Verificar resultado
        assert resultado == [1, 0, 0, 0]  # 8
        assert cout == 0
        
        # 3. Convertir a entero
        valor = bits_a_entero(resultado)
        assert valor == 8
        
        # 4. Verificar que se pueda mostrar
        try:
            mostrar_operacion(a, b, resultado, cout, 0)
            assert True
        except Exception:
            pytest.fail("mostrar_operacion falló en prueba de integración")
    
    def test_complete_flow_subtraction(self):
        """
        Prueba el flujo completo para una resta.
        """
        # Datos de prueba: 7 - 2 = 5
        a = [0, 1, 1, 1]  # 7
        b = [0, 0, 1, 0]  # 2
        
        # 1. Usar el sumador-restador
        resultado, cout = sumador_restador_4bits(a, b, operacion=1)
        
        # 2. Verificar resultado
        assert resultado == [0, 1, 0, 1]  # 5
        assert cout == 1
        
        # 3. Convertir a entero (considerando que es resta)
        valor = bits_a_entero(resultado, es_resta=True, cout=cout)
        assert valor == 5
    
    def test_negative_result_flow(self):
        """
        Prueba el flujo completo para una resta con resultado negativo.
        """
        # Datos de prueba: 2 - 7 = -5
        a = [0, 0, 1, 0]  # 2
        b = [0, 1, 1, 1]  # 7
        
        # 1. Usar el sumador-restador
        resultado, cout = sumador_restador_4bits(a, b, operacion=1)
        
        # 2. Verificar resultado en complemento a 2
        assert resultado == [1, 0, 1, 1]  # -5 en complemento a 2
        assert cout == 0
        
        # 3. Convertir a entero
        valor = bits_a_entero(resultado, es_resta=True, cout=cout)
        assert valor == -5
    
    def test_all_components_connected(self):
        """
        Verifica que todos los componentes estén conectados correctamente.
        """
        # Verificar que las puertas básicas funcionan
        assert AND(1, 1) == 1
        assert OR(0, 1) == 1
        assert NOT(0) == 1
        assert XOR(0, 1) == 1
        
        # Verificar half adder
        suma, carry = half_adder(1, 1)
        assert suma == 0 and carry == 1
        
        # Verificar full adder
        suma, cout = full_adder(1, 1, 1)
        assert suma == 1 and cout == 1
        
        # Verificar complemento a 2
        comp2 = complemento_a_2([0, 0, 0, 1])  # 1
        assert comp2 == [1, 1, 1, 1]  # -1
        
        # Verificar adder de 4 bits
        resultado, cout = adder_4bits([0,1,0,1], [0,0,1,1])
        assert resultado == [1,0,0,0] and cout == 0
    
    def test_truth_table_consistency(self):
        """
        Verifica que las tablas de verdad sean consistentes
        a través de todas las capas.
        """
        # Para cada combinación de 2 bits, verificar que XOR funcione
        for a in [0, 1]:
            for b in [0, 1]:
                xor_directo = XOR(a, b)
                
                # XOR usando half adder (suma sin carry)
                suma_half, _ = half_adder(a, b)
                assert xor_directo == suma_half, \
                    f"XOR inconsistente para a={a}, b={b}"
    
    def test_adder_subtractor_equivalence(self):
        """
        Verifica que A - B = A + (-B) usando complemento a 2.
        """
        test_cases = [
            ([0,1,0,1], [0,0,1,1]),  # 5, 3
            ([0,1,1,1], [0,0,1,0]),  # 7, 2
            ([0,0,1,0], [0,1,1,1]),  # 2, 7
            ([1,0,0,0], [0,0,0,1]),  # 8, 1
        ]
        
        for a, b in test_cases:
            # Resta usando el sumador-restador
            resultado_resta, cout_resta = sumador_restador_4bits(a, b, operacion=1)
            
            # Suma manual: A + complemento_a_2(B)
            b_negativo = complemento_a_2(b)
            resultado_suma, cout_suma = adder_4bits(a, b_negativo, 0)
            
            # Deberían ser equivalentes
            assert resultado_resta == resultado_suma, \
                f"Resta y suma con complemento no coinciden para {a} - {b}"
            assert cout_resta == cout_suma, \
                f"Carry no coincide para {a} - {b}"
    
    def test_edge_cases(self):
        """
        Prueba casos extremos del sistema.
        """
        # Caso 1: Mínimo valor (0)
        resultado, cout = sumador_restador_4bits([0,0,0,0], [0,0,0,0], 0)
        assert resultado == [0,0,0,0] and cout == 0
        
        # Caso 2: Máximo valor positivo (7) en resta con signo
        resultado, cout = sumador_restador_4bits([0,1,1,1], [0,0,0,0], 1)
        assert resultado == [0,1,1,1] and cout == 1
        
        # Caso 3: Mínimo valor negativo (-8) en resta con signo
        resultado, cout = sumador_restador_4bits([1,0,0,0], [0,0,0,0], 1)
        assert resultado == [1,0,0,0] and cout == 1
        
        # Caso 4: Overflow máximo
        resultado, cout = sumador_restador_4bits([1,1,1,1], [0,0,0,1], 0)
        assert cout == 1  # Debe haber overflow
    
    def test_error_handling_integration(self):
        """
        Verifica que el manejo de errores funcione en todo el sistema.
        """
        # Entrada inválida en el sumador-restador
        with pytest.raises(ValueError):
            sumador_restador_4bits([0,0,0], [0,0,0,0], 0)
        
        with pytest.raises(ValueError):
            sumador_restador_4bits([0,0,0,0], [0,0,0,0], 2)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])