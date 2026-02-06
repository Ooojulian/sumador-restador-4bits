"""
Implementación de un medio sumador (Half Adder).

Un medio sumador suma dos bits sin considerar el acarreo de entrada.
"""

from .logic_gates import AND, XOR


def half_adder(a: int, b: int):
    """
    Implementa un medio sumador (Half Adder).
    
    Un half adder suma dos bits y produce:
    - Suma: XOR de los bits de entrada
    - Carry: AND de los bits de entrada
    
    Args:
        a: Primer bit de entrada (0 o 1)
        b: Segundo bit de entrada (0 o 1)
        
    Returns:
        Tupla (suma, carry) donde:
        - suma: Resultado de la suma (0 o 1)
        - carry: Acarreo de salida (0 o 1)
        
    Examples:
        >>> half_adder(0, 1)
        (1, 0)
        >>> half_adder(1, 1)
        (0, 1)
    """
    suma = XOR(a, b)
    carry = AND(a, b)
    
    return suma, carry


def prueba_half_adder():
    """
    Prueba el medio sumador con todas las combinaciones posibles.
    """
    print("Prueba del Medio Sumador (Half Adder):")
    print("=" * 40)
    print("A B | Suma | Carry")
    print("-" * 40)
    
    for a in [0, 1]:
        for b in [0, 1]:
            suma, carry = half_adder(a, b)
            print(f"{a} {b} |   {suma}   |   {carry}")
    
    return True


if __name__ == "__main__":
    prueba_half_adder()