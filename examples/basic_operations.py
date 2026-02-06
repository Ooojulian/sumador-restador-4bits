"""
Ejemplos básicos de operaciones con el sumador-restador de 4 bits.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.adder_subtractor import sumador_restador_4bits
from src.utils import mostrar_operacion


def demostracion_basica():
    """Demostración de operaciones básicas."""
    print("=" * 60)
    print("DEMOSTRACIÓN DE OPERACIONES BÁSICAS")
    print("=" * 60)
    
    # Ejemplo 1: Suma simple
    print("\n1. Suma simple: 5 + 3")
    a = [0, 1, 0, 1]  # 5
    b = [0, 0, 1, 1]  # 3
    resultado, carry = sumador_restador_4bits(a, b, 0)
    mostrar_operacion(a, b, resultado, carry, 0)
    
    # Ejemplo 2: Resta simple
    print("\n2. Resta simple: 7 - 2")
    a = [0, 1, 1, 1]  # 7
    b = [0, 0, 1, 0]  # 2
    resultado, carry = sumador_restador_4bits(a, b, 1)
    mostrar_operacion(a, b, resultado, carry, 1)
    
    # Ejemplo 3: Resta con resultado negativo
    print("\n3. Resta con resultado negativo: 2 - 7")
    a = [0, 0, 1, 0]  # 2
    b = [0, 1, 1, 1]  # 7
    resultado, carry = sumador_restador_4bits(a, b, 1)
    mostrar_operacion(a, b, resultado, carry, 1)
    
    # Ejemplo 4: Overflow en suma
    print("\n4. Overflow en suma: 8 + 8")
    a = [1, 0, 0, 0]  # 8
    b = [1, 0, 0, 0]  # 8
    resultado, carry = sumador_restador_4bits(a, b, 0)
    mostrar_operacion(a, b, resultado, carry, 0)
    
    # Ejemplo 5: Overflow en resta (resultado muy positivo)
    print("\n5. Overflow en resta: 7 - (-8) = 15")
    a = [0, 1, 1, 1]  # 7
    b = [1, 0, 0, 0]  # -8
    resultado, carry = sumador_restador_4bits(a, b, 1)
    mostrar_operacion(a, b, resultado, carry, 1)
    
    # Ejemplo 6: Overflow en resta (resultado muy negativo)
    print("\n6. Overflow en resta: -8 - 7 = -15 (fuera de rango)")
    a = [1, 0, 0, 0]  # -8
    b = [0, 1, 1, 1]  # 7
    resultado, carry = sumador_restador_4bits(a, b, 1)
    mostrar_operacion(a, b, resultado, carry, 1)


def demostracion_tablas_verdad():
    """Muestra las tablas de verdad de las puertas lógicas básicas."""
    print("\n" + "=" * 60)
    print("TABLAS DE VERDAD DE PUERTAS LÓGICAS")
    print("=" * 60)
    
    from src.logic_gates import AND, OR, NOT, XOR
    
    print("\n1. Puerta AND:")
    print("   A B | AND")
    print("   ---------")
    for a in [0, 1]:
        for b in [0, 1]:
            print(f"   {a} {b} |  {AND(a, b)}")
    
    print("\n2. Puerta OR:")
    print("   A B | OR")
    print("   ---------")
    for a in [0, 1]:
        for b in [0, 1]:
            print(f"   {a} {b} |  {OR(a, b)}")
    
    print("\n3. Puerta NOT:")
    print("   A | NOT")
    print("   ------")
    for a in [0, 1]:
        print(f"   {a} |  {NOT(a)}")
    
    print("\n4. Puerta XOR (implementada con AND, OR, NOT):")
    print("   A B | XOR")
    print("   ---------")
    for a in [0, 1]:
        for b in [0, 1]:
            print(f"   {a} {b} |  {XOR(a, b)}")


if __name__ == "__main__":
    demostracion_basica()
    demostracion_tablas_verdad()
    print("\n" + "=" * 60)
    print("FIN DE LA DEMOSTRACIÓN")
    print("=" * 60)