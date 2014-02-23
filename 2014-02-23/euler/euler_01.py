#!/usr/bin/env python
# -*- coding: utf8 -*-

INITIAL_VALUE = 1
MAX_VALUE = 1000

def es_divisible(numero, divisor):
    return numero % divisor == 0

def es_multiplo(a, b):
    return es_divisible(a, b)

def problema_01():
    acum = 0
    for n in range(INITIAL_VALUE, MAX_VALUE + 1):
        # print "%d es múltiplo de 3: %s" % ( n, es_multiplo(n, 3) )
        # print "%d es múltiplo de 5: %s" % ( n, es_multiplo(n, 5) )
        if es_multiplo(n, 3) or es_multiplo(n, 5):
            acum += n
    print acum 

# Esta condición solo se cumple cuando se ejecuta el script 
# directamente, no cuando se importa desde la consola interactiva
# o desde otro módulo.
if __name__ == '__main__':
    problema_01()
