# Teoría del Sumador-Restador de 4 bits

## Fundamentos de Lógica Digital

### Puertas Lógicas Básicas

#### AND (Y)
La puerta AND produce 1 solo si todas sus entradas son 1.

A B | AND
0 0 | 0
0 1 | 0
1 0 | 0
1 1 | 1


#### OR (O)
La puerta OR produce 1 si al menos una entrada es 1.

A B | OR
0 0 | 0
0 1 | 1
1 0 | 1
1 1 | 1


#### NOT (NO)
La puerta NOT invierte su entrada.

A | NOT
0 | 1
1 | 0


### Puertas Derivadas

#### XOR (O Exclusivo)
Implementada con AND, OR, NOT:

XOR(A,B) = (A AND NOT B) OR (NOT A AND B)

A B | XOR
0 0 | 0
0 1 | 1
1 0 | 1
1 1 | 0


## Aritmética Binaria

### Suma Binaria

Ejemplo: 5 + 3 = 8
0101 (5)

0011 (3)

1000 (8)


### Acarreos (Carry)
Cuando la suma de dos bits excede 1, se genera un acarreo:

1 ← acarreo
0110 (6)

0111 (7)

1101 (13)


## Medio Sumador (Half Adder)

Suma dos bits sin considerar acarreo de entrada:

Suma = A XOR B
Carry = A AND B

A B | Suma | Carry
0 0 | 0 | 0
0 1 | 1 | 0
1 0 | 1 | 0
1 1 | 0 | 1


## Sumador Completo (Full Adder)

Suma tres bits (dos bits + acarreo de entrada):

Suma = A XOR B XOR Cin
Cout = (A AND B) OR (A AND Cin) OR (B AND Cin)

A B Cin | Suma | Cout
0 0 0 | 0 | 0
0 0 1 | 1 | 0
0 1 0 | 1 | 0
0 1 1 | 0 | 1
1 0 0 | 1 | 0
1 0 1 | 0 | 1
1 1 0 | 0 | 1
1 1 1 | 1 | 1


## Sumador de 4 bits

Conecta 4 sumadores completos en cascada:

     A3 B3       A2 B2       A1 B1       A0 B0
     |  |        |  |        |  |        |  |
    [FA3]       [FA2]       [FA1]       [FA0]
     |  |        |  |        |  |        |  |
    Cout└→Cin   Cout└→Cin   Cout└→Cin   Cout└→Cin
     |           |           |           |
    S3          S2          S1          S0


## Representación de Números Negativos

### Complemento a 1
Invertir todos los bits:

5 = 0101 → Complemento a 1 = 1010


### Complemento a 2
Complemento a 1 + 1:

5 = 0101
Complemento a 1 = 1010
Complemento a 2 = 1010 + 0001 = 1011 (-5)


### Rango en Complemento a 2 (4 bits)

0000 = 0
0001 = 1
...
0111 = 7
1000 = -8
1001 = -7
...
1111 = -1


## Resta usando Complemento a 2

La resta A - B se convierte en A + (-B):

Ejemplo: 7 - 5 = 2
7 = 0111
5 = 0101
-5 en complemento a 2 = 1011

0111 (7)

1011 (-5)

0010 (2) con carry=1 (ignorado)


## Detección de Overflow

### En Suma
Overflow ocurre cuando el resultado excede el rango representable:

8 + 8 = 16 (fuera de rango 0-15)
1000 (8)

1000 (8)

0000 (0) con carry=1 (overflow)


### En Resta
Overflow ocurre cuando el resultado está fuera del rango -8 a 7:

-8 - 1 = -9 (fuera de rango)
1000 (-8)

0001 (1) = 1000 + 1111 = 0111 (7) incorrecto


## Ventajas del Complemento a 2

1. **Unicidad del cero**: Solo una representación (0000)
2. **Suma y resta unificadas**: Mismo circuito para ambas operaciones
3. **Ciclicidad**: A - 1 = A + (-1) funciona correctamente
4. **Detección sencilla**: Signo determinado por el MSB

## Aplicaciones en Computación

Este diseño es fundamental para:
- Unidades Aritmético-Lógicas (ALU)
- Procesadores y microcontroladores
- Circuitos aritméticos en FPGAs
- Sistemas embebidos
- Educación en arquitectura de computadoras

## Referencias

1. "Digital Design and Computer Architecture" - Harris & Harris
2. "Computer Organization and Design" - Patterson & Hennessy
3. "From NAND to Tetris" - Noam Nisan & Shimon Schocken