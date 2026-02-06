# Especificaciones de Diseño

## Objetivo
Implementar un sumador-restador de 4 bits usando únicamente puertas lógicas AND, OR y NOT.

## Restricciones
- Solo se pueden usar las funciones AND, OR, NOT como primitivas
- Todas las demás funciones deben construirse a partir de estas
- Debe manejar números de 4 bits
- Debe soportar suma y resta

## Especificaciones Técnicas

### Entradas
- Dos números de 4 bits (A[3:0], B[3:0])
- Un bit de control (OP):
  - 0: Operación de suma
  - 1: Operación de resta

### Salidas
- Resultado de 4 bits (R[3:0])
- Bit de acarreo/overflow (Cout)

### Rango de Operación
- Suma: 0 a 15 (sin signo)
- Resta: -8 a +7 (complemento a 2)

### Esquema de Circuito
            ┌─────────────────┐
     A[3:0] │                 │ R[3:0]
     B[3:0] │ 4-bit Adder/    ├───────► Resultado
       OP   │  Subtractor     │
            │                 ├───────► Cout
            └─────────────────┘



### Algoritmo de Resta
Para A - B:
1. Calcular complemento a 2 de B
2. Sumar A + complemento_a_2(B)
3. Interpretar resultado en complemento a 2 si es negativo

## Estructura Modular

1. **Nivel 0**: Puertas básicas (AND, OR, NOT)
2. **Nivel 1**: Puertas derivadas (XOR, NAND)
3. **Nivel 2**: Medio sumador (Half Adder)
4. **Nivel 3**: Sumador completo (Full Adder)
5. **Nivel 4**: Sumador de 4 bits (4-bit Adder)
6. **Nivel 5**: Circuito de complemento
7. **Nivel 6**: Sumador-restador final

## Implementación en Software

### Jerarquía de Módulos

src/
├── logic_gates.py # Nivel 0-1
├── half_adder.py # Nivel 2
├── full_adder.py # Nivel 3
├── adder_4bit.py # Nivel 4
├── complement.py # Nivel 5
├── adder_subtractor.py # Nivel 6
└── utils.py # Utilidades


### Representación de Datos
- Los bits se representan como enteros 0 o 1
- Los números de 4 bits se representan como listas: [bit3, bit2, bit1, bit0]
- bit3 es el MSB (Most Significant Bit)
- bit0 es el LSB (Least Significant Bit)

### Manejo de Errores
- Validación de entrada (longitud, valores válidos)
- Manejo de operaciones inválidas
- Documentación de excepciones

## Decisiones de Diseño

### Representación de Números Negativos
Se usa complemento a 2 porque:
1. Permite usar el mismo circuito para suma y resta
2. Elimina la representación dual del cero
3. Es estándar en sistemas digitales

### Detección de Overflow
- **Suma**: Cout = 1 indica overflow
- **Resta**: Interpretación especial del cout

### Extensibilidad
El diseño es modular para permitir:
- Extender a más bits (8, 16, 32)
- Agregar nuevas operaciones
- Implementar en hardware real