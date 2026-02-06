"""
Sumador-Restador de 4 bits con puertas lógicas básicas.

Este módulo implementa un sumador-restador de 4 bits utilizando
únicamente puertas lógicas AND, OR y NOT.

Módulos exportados:
- logic_gates: Puertas lógicas básicas
- half_adder: Medio sumador
- full_adder: Sumador completo
- adder_4bit: Sumador de 4 bits
- complement: Complemento a 1 y 2
- adder_subtractor: Sumador-restador principal
- utils: Funciones auxiliares
"""

from .logic_gates import AND, OR, NOT, XOR, NAND
from .half_adder import half_adder
from .full_adder import full_adder
from .adder_4bit import adder_4bits
from .complement import complemento_a_1, complemento_a_2
from .adder_subtractor import sumador_restador_4bits
from .utils import bits_a_entero, mostrar_operacion, ingresar_bits

__version__ = "1.0.0"
__author__ = "Tu Nombre"
__all__ = [
    "AND", "OR", "NOT", "XOR", "NAND",
    "half_adder", "full_adder", "adder_4bits",
    "complemento_a_1", "complemento_a_2",
    "sumador_restador_4bits",
    "bits_a_entero", "mostrar_operacion", "ingresar_bits"
]