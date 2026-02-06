"""
Funciones auxiliares para el sumador-restador.

Incluye conversiones, visualización y entrada de datos.
"""

from .adder_4bit import bits_a_decimal


def bits_a_entero(bits: list, es_resta: bool = False, cout: int = 0) -> int:
    """
    Convierte una lista de 4 bits a su valor entero.
    
    Para resultados de resta, interpreta en complemento a 2 si es negativo.
    
    Args:
        bits: Lista de 4 bits (0 o 1)
        es_resta: True si el resultado proviene de una resta
        cout: Bit de carry/overflow de la operación
        
    Returns:
        Valor entero del número
        
    Examples:
        >>> bits_a_entero([1,0,0,0])
        8
        >>> bits_a_entero([1,0,1,1], es_resta=True, cout=0)
        -5
    """
    # Para suma o para resta con resultado positivo (cout=1)
    if not es_resta or (es_resta and cout == 1):
        return bits_a_decimal(bits)
    else:
        # Para resta con cout=0, el resultado es negativo en complemento a 2
        # Para obtener el valor absoluto, calculamos complemento a 2 nuevamente
        from .complement import complemento_a_2
        valor_positivo = bits_a_decimal(complemento_a_2(bits))
        return -valor_positivo


def mostrar_operacion(a_bits: list, b_bits: list, resultado: list, 
                      cout: int, operacion: int) -> None:
    """
    Muestra una operación y sus resultados de forma legible.
    
    Args:
        a_bits: Primer operando (4 bits)
        b_bits: Segundo operando (4 bits)
        resultado: Resultado de la operación (4 bits)
        cout: Bit de carry/overflow
        operacion: 0 para suma, 1 para resta
    """
    a_dec = bits_a_decimal(a_bits)
    b_dec = bits_a_decimal(b_bits)
    
    op_str = "+" if operacion == 0 else "-"
    
    print(f"\nOperación: {'SUMA' if operacion == 0 else 'RESTA'}")
    print(f"  {a_bits} ({a_dec}) {op_str} {b_bits} ({b_dec})")
    
    if operacion == 0:  # Suma
        resultado_dec = bits_a_entero(resultado)
        print(f"  Resultado: {resultado} ({resultado_dec})")
        print(f"  Acarreo de salida: {cout}")
        
        # Detección de overflow en suma
        if a_dec + b_dec > 15:
            print("  ⚠️  OVERFLOW! (Resultado > 15)")
    
    else:  # Resta
        resultado_dec = bits_a_entero(resultado, es_resta=True, cout=cout)
        print(f"  Resultado: {resultado} ({resultado_dec})")
        print(f"  Acarreo/overflow: {cout}")
        
        # En resta, cout=0 indica que el resultado es negativo
        if cout == 0:
            print("  📉 Resultado negativo (complemento a 2)")
        
        # Detección de overflow en resta
        if a_dec - b_dec < -8 or a_dec - b_dec > 7:
            print("  ⚠️  OVERFLOW! (Resultado fuera de rango -8 a 7)")


def ingresar_bits(mensaje: str) -> list:
    """
    Solicita al usuario que ingrese 4 bits y valida la entrada.
    
    Args:
        mensaje: Mensaje a mostrar al usuario
        
    Returns:
        Lista de 4 bits (enteros 0 o 1)
    """
    while True:
        entrada = input(mensaje).strip()
        
        # Verificar longitud
        if len(entrada) != 4:
            print("❌ Error: Debe ingresar exactamente 4 bits")
            continue
        
        # Verificar que todos sean 0 o 1
        if not all(c in '01' for c in entrada):
            print("❌ Error: Solo se permiten los caracteres 0 y 1")
            continue
        
        # Convertir a lista de enteros
        bits = [int(c) for c in entrada]
        return bits


def mostrar_tabla_verdad_puerta(puerta_nombre: str, puerta_func) -> None:
    """
    Muestra la tabla de verdad de una puerta lógica.
    
    Args:
        puerta_nombre: Nombre de la puerta
        puerta_func: Función que implementa la puerta
    """
    print(f"\nTabla de verdad {puerta_nombre}:")
    print("A B | Salida")
    print("-" * 15)
    
    for a in [0, 1]:
        for b in [0, 1]:
            salida = puerta_func(a, b)
            print(f"{a} {b} |   {salida}")


if __name__ == "__main__":
    # Prueba de las funciones auxiliares
    print("Prueba de funciones auxiliares:")
    print("=" * 40)
    
    # Prueba de bits_a_entero
    print("\nPrueba de bits_a_entero:")
    print(f"[1,0,0,0] -> {bits_a_entero([1,0,0,0])} (esperado: 8)")
    print(f"[1,0,1,1] con es_resta=True, cout=0 -> {bits_a_entero([1,0,1,1], True, 0)} (esperado: -5)")
    
    # Prueba de ingresar_bits (simulada)
    print("\nPrueba simulada de ingresar_bits:")
    # Simulamos una entrada válida
    print("Simulación: usuario ingresa '0101'")
    bits_simulados = ingresar_bits.__wrapped__("Ingrese 4 bits: ") if hasattr(ingresar_bits, '__wrapped__') else [0,1,0,1]
    print(f"Bits ingresados: {bits_simulados}")