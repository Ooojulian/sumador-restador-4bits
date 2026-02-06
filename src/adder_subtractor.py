"""
Implementación del sumador-restador de 4 bits.

Combina un sumador de 4 bits con circuitos de complemento
para realizar tanto sumas como restas.
"""

from .adder_4bit import adder_4bits
from .complement import complemento_a_2


def sumador_restador_4bits(a_bits: list, b_bits: list, operacion: int):
    """
    Implementa un sumador-restador de 4 bits.
    
    Args:
        a_bits: Lista de 4 bits representando el primer número
        b_bits: Lista de 4 bits representando el segundo número
        operacion: 0 para suma, 1 para resta
        
    Returns:
        Tupla (resultado_bits, cout) donde:
        - resultado_bits: Lista de 4 bits con el resultado
        - cout: Acarreo/overflow de salida
        
    Raises:
        ValueError: Si operacion no es 0 o 1
        
    Examples:
        >>> sumador_restador_4bits([0,1,0,1], [0,0,1,1], 0)
        ([1,0,0,0], 0)  # 5 + 3 = 8
        >>> sumador_restador_4bits([0,1,1,1], [0,0,1,0], 1)
        ([0,1,0,1], 1)  # 7 - 2 = 5
    """
    if operacion not in [0, 1]:
        raise ValueError("La operación debe ser 0 (suma) o 1 (resta)")
    
    # Validar entrada
    if len(a_bits) != 4 or len(b_bits) != 4:
        raise ValueError("Las listas deben tener exactamente 4 bits")
    
    # Para resta: A - B = A + complemento_a_2(B)
    if operacion == 1:  # Resta
        b_operand = complemento_a_2(b_bits)
    else:  # Suma (operacion == 0)
        b_operand = b_bits
    
    # Realizar la suma
    resultado, cout = adder_4bits(a_bits, b_operand, 0)
    
    return resultado, cout


def prueba_sumador_restador():
    """
    Prueba el sumador-restador con varios casos de prueba.
    """
    print("Prueba del Sumador-Restador de 4 bits:")
    print("=" * 70)
    
    casos_prueba = [
        # (a, b, op, resultado_esp, cout_esp, descripcion)
        ([0,1,0,1], [0,0,1,1], 0, [1,0,0,0], 0, "5 + 3 = 8"),
        ([0,1,1,1], [0,0,1,0], 1, [0,1,0,1], 1, "7 - 2 = 5"),
        ([0,0,1,0], [0,1,1,1], 1, [1,0,1,1], 0, "2 - 7 = -5"),
        ([1,0,0,0], [1,0,0,0], 0, [0,0,0,0], 1, "8 + 8 = 16 (overflow)"),
        ([1,1,1,1], [0,0,0,1], 0, [0,0,0,0], 1, "15 + 1 = 16 (overflow)"),
        ([0,0,0,0], [0,0,0,0], 0, [0,0,0,0], 0, "0 + 0 = 0"),
        ([0,1,0,1], [0,1,0,1], 1, [0,0,0,0], 1, "5 - 5 = 0"),
    ]
    
    resultados_correctos = 0
    total_casos = len(casos_prueba)
    
    for a, b, op, resultado_esp, cout_esp, desc in casos_prueba:
        resultado, cout = sumador_restador_4bits(a, b, op)
        correcto = resultado == resultado_esp and cout == cout_esp
        estado = "✓" if correcto else "✗"
        
        if correcto:
            resultados_correctos += 1
        
        op_str = "+" if op == 0 else "-"
        print(f"\n{desc}:")
        print(f"  {a} {op_str} {b} = {resultado} (cout={cout})")
        print(f"  Esperado: {resultado_esp} (cout={cout_esp}) {estado}")
    
    print(f"\nResumen: {resultados_correctos}/{total_casos} pruebas pasadas")
    
    return resultados_correctos == total_casos


if __name__ == "__main__":
    prueba_sumador_restador()