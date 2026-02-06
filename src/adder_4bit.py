"""
Implementación de un sumador de 4 bits.

Conecta 4 sumadores completos en cascada para sumar números de 4 bits.
"""

from .full_adder import full_adder


def adder_4bits(a_bits: list, b_bits: list, cin: int = 0):
    """
    Implementa un sumador de 4 bits con acarreo de entrada.
    
    Args:
        a_bits: Lista de 4 bits representando el primer número
        b_bits: Lista de 4 bits representando el segundo número
        cin: Acarreo de entrada (default: 0)
        
    Returns:
        Tupla (resultado_bits, cout) donde:
        - resultado_bits: Lista de 4 bits con el resultado
        - cout: Acarreo de salida (0 o 1)
        
    Raises:
        ValueError: Si las listas no tienen exactamente 4 bits
        
    Examples:
        >>> adder_4bits([0,1,0,1], [0,0,1,1])
        ([1,0,0,0], 0)  # 5 + 3 = 8
    """
    # Validar entrada
    if len(a_bits) != 4 or len(b_bits) != 4:
        raise ValueError("Las listas deben tener exactamente 4 bits")
    
    # Validar que todos los bits sean 0 o 1
    for bit in a_bits + b_bits:
        if bit not in [0, 1]:
            raise ValueError("Los bits deben ser 0 o 1")
    
    # Inicializar resultado y acarreo
    resultado = [0, 0, 0, 0]
    carry = cin
    
    # Sumar bit por bit, empezando por el LSB (bit menos significativo, índice 3)
    for i in range(3, -1, -1):  # Iterar de 3 a 0
        suma, carry = full_adder(a_bits[i], b_bits[i], carry)
        resultado[i] = suma
    
    return resultado, carry


def prueba_adder_4bits():
    """
    Prueba el sumador de 4 bits con varios casos de prueba.
    """
    print("Prueba del Sumador de 4 bits:")
    print("=" * 60)
    
    casos_prueba = [
        # (a, b, resultado_esperado, cout_esperado, descripcion)
        ([0,0,0,0], [0,0,0,0], [0,0,0,0], 0, "0 + 0 = 0"),
        ([0,1,0,1], [0,0,1,1], [1,0,0,0], 0, "5 + 3 = 8"),
        ([1,0,0,0], [1,0,0,0], [0,0,0,0], 1, "8 + 8 = 16 (overflow)"),
        ([1,1,1,1], [0,0,0,1], [0,0,0,0], 1, "15 + 1 = 16 (overflow)"),
        ([0,0,0,1], [0,0,0,1], [0,0,1,0], 0, "1 + 1 = 2"),
    ]
    
    for a, b, resultado_esp, cout_esp, desc in casos_prueba:
        resultado, cout = adder_4bits(a, b)
        correcto = resultado == resultado_esp and cout == cout_esp
        estado = "✓" if correcto else "✗"
        
        print(f"\n{desc}:")
        print(f"  {a} + {b} = {resultado} (cout={cout})")
        print(f"  Esperado: {resultado_esp} (cout={cout_esp}) {estado}")
    
    return True


def bits_a_decimal(bits: list) -> int:
    """
    Convierte una lista de 4 bits a su valor decimal.
    
    Args:
        bits: Lista de 4 bits (0 o 1)
        
    Returns:
        Valor decimal del número binario
    """
    valor = 0
    for i in range(4):
        valor += bits[3-i] * (2**i)
    return valor


if __name__ == "__main__":
    prueba_adder_4bits()