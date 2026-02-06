"""
Implementación de complemento a 1 y complemento a 2.

Usado para representar números negativos en operaciones de resta.
"""

from .logic_gates import NOT
from .adder_4bit import adder_4bits


def complemento_a_1(bits: list) -> list:
    """
    Calcula el complemento a 1 de un número binario.
    
    El complemento a 1 se obtiene invirtiendo cada bit.
    
    Args:
        bits: Lista de bits (debe tener 4 elementos)
        
    Returns:
        Lista de bits representando el complemento a 1
        
    Examples:
        >>> complemento_a_1([0,1,0,1])
        [1,0,1,0]
    """
    if len(bits) != 4:
        raise ValueError("La lista debe tener 4 bits")
    
    # Complemento a 1 = NOT de cada bit
    return [NOT(bit) for bit in bits]


def complemento_a_2(bits: list) -> list:
    """
    Calcula el complemento a 2 de un número binario.
    
    El complemento a 2 = complemento a 1 + 1.
    
    Args:
        bits: Lista de 4 bits
        
    Returns:
        Lista de 4 bits representando el complemento a 2
        
    Examples:
        >>> complemento_a_2([0,0,0,1])  # 1
        [1,1,1,1]  # -1 en complemento a 2
    """
    # Paso 1: Calcular complemento a 1
    comp1 = complemento_a_1(bits)
    
    # Paso 2: Sumar 1 (0001 en binario)
    uno = [0, 0, 0, 1]
    resultado, _ = adder_4bits(comp1, uno, 0)
    
    return resultado


def prueba_complementos():
    """
    Prueba las funciones de complemento.
    """
    print("Prueba de Complementos:")
    print("=" * 60)
    
    casos_prueba = [
        ([0,0,0,0], "0"),
        ([0,0,0,1], "1"),
        ([0,1,0,1], "5"),
        ([1,0,0,0], "8"),
        ([1,1,1,1], "15"),
    ]
    
    print("\nComplemento a 1:")
    print("Número | Binario | Comp. a 1")
    print("-" * 40)
    
    for bits, desc in casos_prueba:
        comp1 = complemento_a_1(bits)
        print(f"   {desc:2}  |   {bits}   |   {comp1}")
    
    print("\nComplemento a 2:")
    print("Número | Binario | Comp. a 2")
    print("-" * 40)
    
    for bits, desc in casos_prueba:
        comp2 = complemento_a_2(bits)
        print(f"   {desc:2}  |   {bits}   |   {comp2}")
    
    # Verificación de propiedad: A + (-A) = 0 en complemento a 2
    print("\nVerificación: A + complemento_a_2(A) = 0")
    print("-" * 40)
    
    for bits, desc in casos_prueba:
        if desc != "0":  # Evitar el caso 0 + (-0)
            comp2 = complemento_a_2(bits)
            suma, cout = adder_4bits(bits, comp2, 0)
            
            # En complemento a 2, A + (-A) debería dar 0 con cout=1 (ignorado)
            es_cero = suma == [0, 0, 0, 0]
            estado = "✓" if es_cero else "✗"
            
            print(f"  {desc} + (-{desc}) = {suma} {estado}")
    
    return True


if __name__ == "__main__":
    prueba_complementos()