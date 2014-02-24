#!/usr/bin/env python
# -*- coding: utf8 -*-
# Calcula la cantidad de múltiplos de 3 o 5 que existen
# entre 1 y 999.

INITIAL_VALUE = 1
MAX_VALUE = 1000

def es_divisible(numero, divisor):
    return numero % divisor == 0

def es_multiplo(a, b):
    return es_divisible(a, b)

def problema():
    contador = 0
    for n in range(INITIAL_VALUE, MAX_VALUE):
        if es_multiplo(n, 3) or es_multiplo(n, 5):
            contador += 1
    print contador

# Esta condición solo se cumple cuando se ejecuta el script 
# directamente, no cuando se importa desde la consola interactiva
# o desde otro módulo.
if __name__ == '__main__':
    problema()
