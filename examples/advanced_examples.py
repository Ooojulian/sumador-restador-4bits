"""
Ejemplos avanzados del sumador-restador de 4 bits.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.adder_subtractor import sumador_restador_4bits
from src.utils import mostrar_operacion, bits_a_entero
from src.complement import complemento_a_1, complemento_a_2


def demostracion_complementos():
    """Demuestra el uso de complementos a 1 y a 2."""
    print("=" * 70)
    print("DEMOSTRACIÓN DE COMPLEMENTOS A 1 Y A 2")
    print("=" * 70)
    
    numeros = [
        ([0,0,0,0], "0"),
        ([0,0,0,1], "1"),
        ([0,1,0,1], "5"),
        ([1,0,0,0], "8"),
        ([1,1,1,1], "15"),
    ]
    
    print("\nComplemento a 1 (inversión de bits):")
    print("Número | Binario  | Comp. a 1 | Valor")
    print("-" * 50)
    
    for bits, nombre in numeros:
        comp1 = complemento_a_1(bits)
        valor_comp1 = bits_a_entero(comp1)
        print(f"  {nombre:4}  |   {bits}   |   {comp1}   | {valor_comp1:4}")
    
    print("\nComplemento a 2 (para números negativos):")
    print("Número | Binario  | Comp. a 2 | Valor")
    print("-" * 50)
    
    for bits, nombre in numeros:
        comp2 = complemento_a_2(bits)
        valor_comp2 = bits_a_entero(comp2, es_resta=True, cout=0)
        print(f"  {nombre:4}  |   {bits}   |   {comp2}   | {valor_comp2:4}")
    
    print("\nPropiedad: A + complemento_a_2(A) = 0")
    print("-" * 40)
    
    for bits, nombre in numeros:
        if nombre != "0":  # Evitar el caso 0 + (-0)
            comp2 = complemento_a_2(bits)
            # Usamos el adder_4bits directamente
            from src.adder_4bit import adder_4bits
            suma, cout = adder_4bits(bits, comp2, 0)
            es_cero = suma == [0, 0, 0, 0]
            estado = "✓" if es_cero else "✗"
            print(f"  {nombre} + (-{nombre}) = {suma} {estado}")


def demostracion_rangos():
    """Demuestra los rangos de operación del sistema."""
    print("\n" + "=" * 70)
    print("RANGOS DE OPERACIÓN")
    print("=" * 70)
    
    print("\n1. Suma (sin signo):")
    print("   Rango: 0 a 15")
    print("   Overflow cuando resultado > 15")
    
    print("\n   Ejemplos de overflow:")
    casos_overflow = [
        ([1,0,0,0], [1,0,0,0], "8 + 8 = 16 > 15"),
        ([1,1,1,1], [0,0,0,1], "15 + 1 = 16 > 15"),
        ([1,0,1,0], [0,1,1,0], "10 + 6 = 16 > 15"),
    ]
    
    for a, b, desc in casos_overflow:
        resultado, cout = sumador_restador_4bits(a, b, 0)
        print(f"\n   {desc}:")
        print(f"     {a} + {b} = {resultado} (cout={cout})")
        if cout == 1:
            print("     ⚠️  OVERFLOW DETECTADO")
    
    print("\n2. Resta (con signo, complemento a 2):")
    print("   Rango: -8 a +7")
    print("   Overflow cuando resultado < -8 o > 7")
    
    print("\n   Ejemplos en el rango válido:")
    casos_validos = [
        ([0,1,1,1], [0,0,1,0], "7 - 2 = 5 (dentro del rango)"),
        ([0,0,1,0], [0,1,1,1], "2 - 7 = -5 (dentro del rango)"),
        ([1,0,0,0], [0,0,0,1], "-8 - 1 = -9 (fuera del rango)"),
    ]
    
    for a, b, desc in casos_validos:
        resultado, cout = sumador_restador_4bits(a, b, 1)
        valor = bits_a_entero(resultado, es_resta=True, cout=cout)
        print(f"\n   {desc}:")
        print(f"     {a} - {b} = {resultado} = {valor}")
        if cout == 0 and valor < 0:
            print("     📉 Resultado negativo")


def demostracion_propiedades_aritmeticas():
    """Demuestra propiedades aritméticas del sistema."""
    print("\n" + "=" * 70)
    print("PROPIEDADES ARITMÉTICAS")
    print("=" * 70)
    
    print("\n1. Propiedad conmutativa de la suma:")
    a = [0, 1, 0, 1]  # 5
    b = [0, 0, 1, 1]  # 3
    
    resultado1, cout1 = sumador_restador_4bits(a, b, 0)
    resultado2, cout2 = sumador_restador_4bits(b, a, 0)
    
    print(f"   A + B: {a} + {b} = {resultado1} (cout={cout1})")
    print(f"   B + A: {b} + {a} = {resultado2} (cout={cout2})")
    
    if resultado1 == resultado2 and cout1 == cout2:
        print("   ✓ Propiedad conmutativa verificada")
    else:
        print("   ✗ Propiedad conmutativa NO verificada")
    
    print("\n2. Elemento neutro de la suma (0):")
    a = [0, 1, 0, 1]  # 5
    cero = [0, 0, 0, 0]  # 0
    
    resultado, cout = sumador_restador_4bits(a, cero, 0)
    print(f"   A + 0: {a} + {cero} = {resultado} (cout={cout})")
    
    if resultado == a and cout == 0:
        print("   ✓ Elemento neutro verificada")
    else:
        print("   ✗ Elemento neutro NO verificada")
    
    print("\n3. Propiedad: A - A = 0:")
    a = [0, 1, 0, 1]  # 5
    
    resultado, cout = sumador_restador_4bits(a, a, 1)
    print(f"   A - A: {a} - {a} = {resultado} (cout={cout})")
    
    if resultado == [0, 0, 0, 0] and cout == 1:
        print("   ✓ Propiedad A - A = 0 verificada")
    else:
        print("   ✗ Propiedad A - A = 0 NO verificada")
    
    print("\n4. Propiedad: A - B = A + (-B):")
    a = [0, 1, 0, 1]  # 5
    b = [0, 0, 1, 1]  # 3
    
    # Resta directa
    resultado_resta, cout_resta = sumador_restador_4bits(a, b, 1)
    
    # Suma con complemento a 2
    from src.adder_4bit import adder_4bits
    b_neg = complemento_a_2(b)
    resultado_suma, cout_suma = adder_4bits(a, b_neg, 0)
    
    print(f"   A - B: {a} - {b} = {resultado_resta} (cout={cout_resta})")
    print(f"   A + (-B): {a} + {b_neg} = {resultado_suma} (cout={cout_suma})")
    
    if resultado_resta == resultado_suma and cout_resta == cout_suma:
        print("   ✓ Propiedad A - B = A + (-B) verificada")
    else:
        print("   ✗ Propiedad A - B = A + (-B) NO verificada")


if __name__ == "__main__":
    demostracion_complementos()
    demostracion_rangos()
    demostracion_propiedades_aritmeticas()
    
    print("\n" + "=" * 70)
    print("FIN DE LOS EJEMPLOS AVANZADOS")
    print("=" * 70)