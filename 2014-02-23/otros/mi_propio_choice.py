#!/usr/bin/env python
# -*- encoding: utf8 -*-

from random import randint

def mi_propio_choice(lista):
    longitud_lista = len(lista)
    indice = randint(0, longitud_lista - 1)
    return lista[indice]

if __name__ == '__main__':
    vocales = ['a', 'e', 'i', 'o', 'u']
    for x in range(10):
        print mi_propio_choice(vocales)
