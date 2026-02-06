# Detalles de Implementación

## Estructura del Proyecto

### Jerarquía de Archivos

sumador-restador-4bits/
├── src/ # Código fuente principal
│ ├── logic_gates.py # Puertas básicas y derivadas
│ ├── half_adder.py # Medio sumador
│ ├── full_adder.py # Sumador completo
│ ├── adder_4bit.py # Sumador de 4 bits
│ ├── complement.py # Complemento a 1 y 2
│ ├── adder_subtractor.py # Circuito principal
│ └── utils.py # Funciones auxiliares
├── tests/ # Pruebas unitarias
├── examples/ # Ejemplos demostrativos
├── docs/ # Documentación
└── archivos de configuración


## Implementación por Capas

### Capa 1: Puertas Lógicas (logic_gates.py)

```python
def AND(a, b):
    return 1 if (a and b) else 0

def OR(a, b):
    return 1 if (a or b) else 0

def NOT(a):
    return 1 if not a else 0

def XOR(a, b):
    # Implementación usando solo AND, OR, NOT
    return OR(AND(a, NOT(b)), AND(NOT(a), b))

Decisiones de diseño:

Usar operadores booleanos de Python para simular hardware

Retornar enteros (0/1) en lugar de booleanos para consistencia

Documentar cada función con ejemplos

### Capa 2: Medio Sumador (half_adder.py)

def half_adder(a, b):
    suma = XOR(a, b)      # Suma = A XOR B
    carry = AND(a, b)     # Carry = A AND B
    return suma, carry

Características:

Implementación directa de la tabla de verdad

Retorna tupla (suma, carry)

Validación implícita a través de las puertas

### Capa 3: Sumador Completo (full_adder.py)

def full_adder(a, b, cin):
    # Usar dos half adders
    sum1, carry1 = half_adder(a, b)
    suma, carry2 = half_adder(sum1, cin)
    cout = OR(carry1, carry2)
    return suma, cout

Optimización:

Reutilización del half adder

Implementación mínima (2 half adders + 1 OR)

Claridad sobre eficiencia

### Capa 4: Sumador de 4 bits (adder_4bit.py)

def adder_4bits(a_bits, b_bits, cin=0):
    resultado = [0, 0, 0, 0]
    carry = cin
    
    # Iterar de LSB a MSB (índice 3 a 0)
    for i in range(3, -1, -1):
        suma, carry = full_adder(a_bits[i], b_bits[i], carry)
        resultado[i] = suma
    
    return resultado, carry

Decisiones importantes:

Representación de bits como lista [MSB...LSB]

Iteración de derecha a izquierda (LSB primero)

Validación de entrada (4 bits, valores 0/1)

### Capa 5: Complementos (complement.py)

def complemento_a_1(bits):
    return [NOT(bit) for bit in bits]

def complemento_a_2(bits):
    comp1 = complemento_a_1(bits)
    uno = [0, 0, 0, 1]
    resultado, _ = adder_4bits(comp1, uno, 0)
    return resultado

Propiedades verificadas:

complemento_a_2(complemento_a_2(x)) == x

x + complemento_a_2(x) == 0 (módulo 16)

### Capa 6: Sumador-Restador (adder_subtractor.py)

def sumador_restador_4bits(a_bits, b_bits, operacion):
    if operacion == 1:  # Resta
        b_operand = complemento_a_2(b_bits)
    else:               # Suma
        b_operand = b_bits
    
    return adder_4bits(a_bits, b_operand, 0)

Manejo de signo:

Para resta: A - B = A + complemento_a_2(B)

cout en resta tiene significado especial

### Capa 7: Utilidades (utils.py)

def bits_a_entero(bits, es_resta=False, cout=0):
    if not es_resta or (es_resta and cout == 1):
        # Interpretación normal
        return bits_a_decimal(bits)
    else:
        # Complemento a 2 para negativo
        comp2 = complemento_a_2(bits)
        return -bits_a_decimal(comp2)

# Interpretación flexible:

## Maneja tanto números positivos como negativos

### Considera el contexto (suma vs resta)

## Manejo de Errores
### Validación de Entrada
def adder_4bits(a_bits, b_bits, cin=0):
    if len(a_bits) != 4 or len(b_bits) != 4:
        raise ValueError("Las listas deben tener exactamente 4 bits")
    
    for bit in a_bits + b_bits:
        if bit not in [0, 1]:
            raise ValueError("Los bits deben ser 0 o 1")

### Validación de Operación

def sumador_restador_4bits(a_bits, b_bits, operacion):
    if operacion not in [0, 1]:
        raise ValueError("La operación debe ser 0 (suma) o 1 (resta)")


### Decisiones de Diseño Clave
1. Representación de Datos

Listas sobre strings: Más fácil de manipular

Enteros sobre booleanos: Compatibilidad matemática

MSB primero: Convención estándar

2. Modularidad

Cada componente es independiente

Fácil de probar individualmente

Reutilizable en otros proyectos

3. Documentación

Docstrings completos con ejemplos

Type hints para claridad

Ejemplos ejecutables

4. Pruebas

Unitarias para cada componente

Integración para el sistema completo

Casos límite y errores

Consideraciones de Rendimiento
Complejidad Temporal
Puertas lógicas: O(1)

Sumador 4 bits: O(1) (tamaño fijo)

En general: Constante para 4 bits

Complejidad Espacial
Minimalista: Solo almacena los 4 bits de resultado

No recursión: Evita problemas de profundidad de pila

Extensiones Posibles
Más bits: Cambiar constantes y bucles

Pipeline: Paralelizar etapas

Look-ahead carry: Mejorar velocidad

Patrones de Diseño Utilizados
1. Builder Pattern (Implícito)
Construcción gradual desde puertas básicas hasta el sistema completo.

2. Strategy Pattern
Selección de operación (suma/resta) mediante parámetro.

3. Composite Pattern
Sumador de 4 bits compuesto de sumadores de 1 bit.

4. Facade Pattern
sumador_restador_4bits como interfaz simplificada.

Limitaciones y Mejoras Futuras
Limitaciones Actuales
Solo 4 bits (rangos limitados)

Software (no hardware real)

Sin soporte para punto flotante

Mejoras Potenciales
Extensión a n bits: Parámetro de tamaño

Implementación hardware: VHDL/Verilog

Operaciones adicionales: AND, OR, XOR bit a bit

Interfaz gráfica: Visualización del flujo de bits

Simulación temporal: Considerar retardos de propagación


## Directorio .github/workflows/

### .github/workflows/python-tests.yml
```yaml
name: Python Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.8", "3.9", "3.10", "3.11"]

    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest pytest-cov
    
    - name: Run tests with pytest
      run: |
        python -m pytest tests/ -v --cov=src --cov-report=xml
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
        fail_ci_if_error: true
    
    - name: Run examples (sanity check)
      run: |
        python examples/basic_operations.py > /dev/null 2>&1 && echo "Basic examples passed"
        python examples/advanced_examples.py > /dev/null 2>&1 && echo "Advanced examples passed"
    
    - name: Verify imports
      run: |
        python -c "from src import *; print('All imports successful')"