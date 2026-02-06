# Sumador-Restador de 4 Bits con Puertas Lógicas Básicas

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/tu-usuario/sumador-restador-4bits/actions/workflows/python-tests.yml/badge.svg)](https://github.com/tu-usuario/sumador-restador-4bits/actions)

Implementación educativa de un sumador-restador de 4 bits utilizando únicamente puertas lógicas AND, OR y NOT. Este proyecto demuestra los fundamentos de la lógica digital y arquitectura de computadoras desde los principios más básicos.

## 📋 Características

- ✅ Implementación pura usando solo AND, OR, NOT
- ✅ Suma y resta de números de 4 bits
- ✅ Manejo de acarreos (carry) y overflow
- ✅ Representación en complemento a 2 para números negativos
- ✅ Pruebas unitarias completas
- ✅ Documentación detallada
- ✅ Ejemplos interactivos

## Descargar el proyecto

Copia este comando en la terminal
git clone https://github.com/Ooojulian/sumador-restador-4bits.git

Entra a la carpeta
cd sumador-restador-4bits


## Probar que funciona
Abre una terminal en la carpeta del proyecto y ejecuta:

python examples/interactive_demo.py

## Demo interactiva
python examples/interactive_demo.py

## Ejemplos predefinidos
python examples/basic_operations.py

## Ejemplo avanzado
python examples/advanced_examples.py


## 🏗️ Arquitectura del Proyecto

```mermaid
graph TD
    A[AND/OR/NOT] --> B[Half Adder]
    B --> C[Full Adder]
    C --> D[4-bit Adder]
    D --> E[Complemento a 2]
    E --> F[4-bit Adder/Subtractor]
    
    style A fill:#f9f,stroke:#333
    style F fill:#ccf,stroke:#333


## Descargar el proyecto


