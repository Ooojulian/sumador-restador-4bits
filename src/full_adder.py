"""
Implementación de un sumador completo (Full Adder).

Un sumador completo suma tres bits (dos bits de entrada y un acarreo de entrada).
"""

from .logic_gates import OR
from .half_adder import half_adder


def full_adder(a: int, b: int, cin: int):
    """
    Implementa un sumador completo (Full Adder).
    
    Un full adder suma tres bits (a, b, cin) y produce:
    - Suma: Resultado de la suma
    - Cout: Acarreo de salida
    
    Se implementa usando dos half adders y una puerta OR.
    
    Args:
        a: Primer bit de entrada (0 o 1)
        b: Segundo bit de entrada (0 o 1)
        cin: Acarreo de entrada (0 o 1)
        
    Returns:
        Tupla (suma, cout) donde:
        - suma: Resultado de la suma (0 o 1)
        - cout: Acarreo de salida (0 o 1)
        
    Examples:
        >>> full_adder(0, 1, 0)
        (1, 0)
        >>> full_adder(1, 1, 1)
        (1, 1)
    """
    # Primer half adder: suma a y b
    suma_temp, carry1 = half_adder(a, b)
    
    # Segundo half adder: suma el resultado temporal con cin
    suma, carry2 = half_adder(suma_temp, cin)
    
    # El carry de salida es OR de los dos carries
    cout = OR(carry1, carry2)
    
    return suma, cout


def prueba_full_adder():
    """
    Prueba el sumador completo con todas las combinaciones posibles.
    """
    print("Prueba del Sumador Completo (Full Adder):")
    print("=" * 50)
    print("A B Cin | Suma | Cout")
    print("-" * 50)
    
    for a in [0, 1]:
        for b in [0, 1]:
            for cin in [0, 1]:
                suma, cout = full_adder(a, b, cin)
                print(f"{a} {b}  {cin}   |   {suma}   |   {cout}")
    
    return True


if __name__ == "__main__":
    prueba_full_adder()