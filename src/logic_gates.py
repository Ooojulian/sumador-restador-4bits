"""
Implementación de puertas lógicas básicas.

Este módulo define las puertas lógicas fundamentales AND, OR y NOT,
y construye puertas derivadas usando solo estas tres.
"""

def AND(a: int, b: int) -> int:
    """
    Implementa la puerta lógica AND.
    
    Args:
        a: Primer bit de entrada (0 o 1)
        b: Segundo bit de entrada (0 o 1)
        
    Returns:
        Resultado de la operación AND (0 o 1)
        
    Examples:
        >>> AND(0, 0)
        0
        >>> AND(1, 1)
        1
    """
    return 1 if (a and b) else 0


def OR(a: int, b: int) -> int:
    """
    Implementa la puerta lógica OR.
    
    Args:
        a: Primer bit de entrada (0 o 1)
        b: Segundo bit de entrada (0 o 1)
        
    Returns:
        Resultado de la operación OR (0 o 1)
        
    Examples:
        >>> OR(0, 0)
        0
        >>> OR(1, 0)
        1
    """
    return 1 if (a or b) else 0


def NOT(a: int) -> int:
    """
    Implementa la puerta lógica NOT.
    
    Args:
        a: Bit de entrada (0 o 1)
        
    Returns:
        Resultado de la operación NOT (0 o 1)
        
    Examples:
        >>> NOT(0)
        1
        >>> NOT(1)
        0
    """
    return 1 if not a else 0


def XOR(a: int, b: int) -> int:
    """
    Implementa la puerta lógica XOR usando solo AND, OR y NOT.
    
    XOR(a,b) = (A AND NOT B) OR (NOT A AND B)
    
    Args:
        a: Primer bit de entrada (0 o 1)
        b: Segundo bit de entrada (0 o 1)
        
    Returns:
        Resultado de la operación XOR (0 o 1)
        
    Examples:
        >>> XOR(0, 1)
        1
        >>> XOR(1, 1)
        0
    """
    # XOR = (A AND NOT B) OR (NOT A AND B)
    return OR(AND(a, NOT(b)), AND(NOT(a), b))


def NAND(a: int, b: int) -> int:
    """
    Implementa la puerta lógica NAND usando solo AND y NOT.
    
    NAND(a,b) = NOT(AND(a,b))
    
    Args:
        a: Primer bit de entrada (0 o 1)
        b: Segundo bit de entrada (0 o 1)
        
    Returns:
        Resultado de la operación NAND (0 o 1)
    """
    return NOT(AND(a, b))


def prueba_tablas_verdad():
    """
    Muestra las tablas de verdad de todas las puertas lógicas.
    """
    print("Tabla de verdad AND:")
    print("A B | AND")
    print("0 0 |", AND(0, 0))
    print("0 1 |", AND(0, 1))
    print("1 0 |", AND(1, 0))
    print("1 1 |", AND(1, 1))
    
    print("\nTabla de verdad OR:")
    print("A B | OR")
    print("0 0 |", OR(0, 0))
    print("0 1 |", OR(0, 1))
    print("1 0 |", OR(1, 0))
    print("1 1 |", OR(1, 1))
    
    print("\nTabla de verdad NOT:")
    print("A | NOT")
    print("0 |", NOT(0))
    print("1 |", NOT(1))
    
    print("\nTabla de verdad XOR (implementada con AND, OR, NOT):")
    print("A B | XOR")
    print("0 0 |", XOR(0, 0))
    print("0 1 |", XOR(0, 1))
    print("1 0 |", XOR(1, 0))
    print("1 1 |", XOR(1, 1))
    
    return True


if __name__ == "__main__":
    prueba_tablas_verdad()