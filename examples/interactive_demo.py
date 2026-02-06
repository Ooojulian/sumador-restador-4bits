"""
Demostración interactiva del sumador-restador de 4 bits.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.adder_subtractor import sumador_restador_4bits
from src.utils import mostrar_operacion, ingresar_bits
from src.logic_gates import prueba_tablas_verdad
from src.half_adder import prueba_half_adder
from src.full_adder import prueba_full_adder
from src.adder_4bit import prueba_adder_4bits
from src.complement import prueba_complementos
from src.adder_subtractor import prueba_sumador_restador


def mostrar_menu_principal():
    """Muestra el menú principal de la demo interactiva."""
    print("\n" + "=" * 70)
    print("DEMOSTRACIÓN INTERACTIVA - SUMADOR-RESTADOR DE 4 BITS")
    print("=" * 70)
    print("\nOpciones disponibles:")
    print("  1. Realizar una operación (suma o resta)")
    print("  2. Ver tablas de verdad de puertas lógicas")
    print("  3. Ver demostración del medio sumador")
    print("  4. Ver demostración del sumador completo")
    print("  5. Ver demostración del complemento a 1 y 2")
    print("  6. Ver demostración del sumador de 4 bits")
    print("  7. Ver demostración completa del sumador-restador")
    print("  8. Ejecutar todas las pruebas automáticamente")
    print("  9. Salir")
    print("-" * 70)


def realizar_operacion():
    """Permite al usuario realizar una operación manualmente."""
    print("\n" + "-" * 70)
    print("REALIZAR OPERACIÓN")
    print("-" * 70)
    
    try:
        # Ingresar primer número
        print("\nPrimer número (A):")
        a_bits = ingresar_bits("  Ingrese 4 bits (ej: 0101 para 5): ")
        
        # Ingresar segundo número
        print("\nSegundo número (B):")
        b_bits = ingresar_bits("  Ingrese 4 bits (ej: 0011 para 3): ")
        
        # Seleccionar operación
        print("\nSeleccione la operación:")
        print("  0 - Suma (A + B)")
        print("  1 - Resta (A - B)")
        
        while True:
            opcion = input("  Opción (0/1): ").strip()
            if opcion in ['0', '1']:
                operacion = int(opcion)
                break
            else:
                print("  ❌ Error: Debe ingresar 0 o 1")
        
        # Realizar la operación
        resultado, cout = sumador_restador_4bits(a_bits, b_bits, operacion)
        
        # Mostrar resultado
        print("\n" + "=" * 50)
        print("RESULTADO")
        print("=" * 50)
        mostrar_operacion(a_bits, b_bits, resultado, cout, operacion)
        
        # Mostrar interpretación adicional
        from src.utils import bits_a_entero
        a_dec = bits_a_entero(a_bits)
        b_dec = bits_a_entero(b_bits)
        resultado_dec = bits_a_entero(resultado, es_resta=(operacion==1), cout=cout)
        
        print("\nInterpretación:")
        if operacion == 0:
            print(f"  {a_dec} + {b_dec} = {resultado_dec}")
            if cout == 1:
                print("  ⚠️  ADVERTENCIA: Overflow detectado")
                print(f"     El resultado correcto sería {a_dec + b_dec}")
                print(f"     pero solo podemos representar hasta 15")
        else:
            print(f"  {a_dec} - {b_dec} = {resultado_dec}")
            if cout == 0 and resultado_dec < 0:
                print("  📉 El resultado es negativo (complemento a 2)")
            
            # Mostrar también en complemento a 2
            if resultado_dec < 0:
                print(f"  En complemento a 2: {resultado} representa {resultado_dec}")
        
    except ValueError as e:
        print(f"\n❌ Error: {e}")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")


def ejecutar_todas_pruebas():
    """Ejecuta todas las pruebas automáticamente."""
    print("\n" + "=" * 70)
    print("EJECUTANDO TODAS LAS PRUEBAS")
    print("=" * 70)
    
    pruebas = [
        ("Puertas lógicas", prueba_tablas_verdad),
        ("Medio sumador", prueba_half_adder),
        ("Sumador completo", prueba_full_adder),
        ("Complementos", prueba_complementos),
        ("Sumador 4 bits", prueba_adder_4bits),
        ("Sumador-restador", prueba_sumador_restador),
    ]
    
    resultados = []
    
    for nombre, funcion in pruebas:
        print(f"\n{'='*30}")
        print(f"PRUEBA: {nombre}")
        print(f"{'='*30}")
        
        try:
            exito = funcion()
            if exito:
                resultados.append((nombre, "✓ PASÓ"))
                print(f"\n✅ {nombre}: PRUEBA EXITOSA")
            else:
                resultados.append((nombre, "✗ FALLÓ"))
                print(f"\n❌ {nombre}: PRUEBA FALLIDA")
        except Exception as e:
            resultados.append((nombre, f"✗ ERROR: {e}"))
            print(f"\n💥 {nombre}: ERROR - {e}")
    
    # Resumen
    print("\n" + "=" * 70)
    print("RESUMEN DE PRUEBAS")
    print("=" * 70)
    
    for nombre, resultado in resultados:
        print(f"  {nombre:30} {resultado}")
    
    total = len(resultados)
    exitosas = sum(1 for _, r in resultados if "✓" in r or "PASÓ" in r)
    
    print(f"\nTotal: {exitosas}/{total} pruebas exitosas")
    
    if exitosas == total:
        print("🎉 ¡TODAS LAS PRUEBAS PASARON EXITOSAMENTE!")
    else:
        print("⚠️  Algunas pruebas fallaron")


def mostrar_bienvenida():
    """Muestra el mensaje de bienvenida."""
    print("\n" + "*" * 70)
    print("* BIENVENIDO AL SUMADOR-RESTADOR DE 4 BITS")
    print("*" * 70)
    print("\nEste programa implementa un sumador-restador de 4 bits usando")
    print("únicamente puertas lógicas AND, OR y NOT.")
    print("\nCaracterísticas:")
    print("  • Suma y resta de números de 4 bits")
    print("  • Manejo de acarreos y overflow")
    print("  • Representación en complemento a 2 para números negativos")
    print("  • Implementado desde las puertas lógicas más básicas")
    print("\nInstrucciones:")
    print("  • Use el menú para seleccionar opciones")
    print("  • Para operaciones, ingrese 4 bits (ej: 0101 para 5)")
    print("  • 0 representa falso/apagado, 1 representa verdadero/encendido")


def main():
    """Función principal de la demo interactiva."""
    mostrar_bienvenida()
    
    while True:
        mostrar_menu_principal()
        
        opcion = input("\nSeleccione una opción (1-9): ").strip()
        
        if opcion == "1":
            realizar_operacion()
            input("\nPresione Enter para continuar...")
        
        elif opcion == "2":
            print("\n" + "=" * 70)
            print("TABLAS DE VERDAD")
            print("=" * 70)
            prueba_tablas_verdad()
            input("\nPresione Enter para continuar...")
        
        elif opcion == "3":
            print("\n" + "=" * 70)
            print("MEDIO SUMADOR (HALF ADDER)")
            print("=" * 70)
            prueba_half_adder()
            input("\nPresione Enter para continuar...")
        
        elif opcion == "4":
            print("\n" + "=" * 70)
            print("SUMADOR COMPLETO (FULL ADDER)")
            print("=" * 70)
            prueba_full_adder()
            input("\nPresione Enter para continuar...")
        
        elif opcion == "5":
            print("\n" + "=" * 70)
            print("COMPLEMENTO A 1 Y A 2")
            print("=" * 70)
            prueba_complementos()
            input("\nPresione Enter para continuar...")
        
        elif opcion == "6":
            print("\n" + "=" * 70)
            print("SUMADOR DE 4 BITS")
            print("=" * 70)
            prueba_adder_4bits()
            input("\nPresione Enter para continuar...")
        
        elif opcion == "7":
            print("\n" + "=" * 70)
            print("SUMADOR-RESTADOR COMPLETO")
            print("=" * 70)
            prueba_sumador_restador()
            input("\nPresione Enter para continuar...")
        
        elif opcion == "8":
            ejecutar_todas_pruebas()
            input("\nPresione Enter para continuar...")
        
        elif opcion == "9":
            print("\n" + "=" * 70)
            print("¡GRACIAS POR USAR EL SUMADOR-RESTADOR DE 4 BITS!")
            print("=" * 70)
            print("\nEsperamos que esta demostración haya sido útil")
            print("para entender los fundamentos de la lógica digital.")
            print("\n¡Hasta pronto!")
            break
        
        else:
            print("\n❌ Opción no válida. Por favor, seleccione 1-9.")
            input("Presione Enter para continuar...")


if __name__ == "__main__":
    main()