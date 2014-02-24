#!/usr/bin/env python
# -*- coding: utf8 -*-

# Problema:
# Simular que salimos a la calle a contar 100 personas.
# Solo vamos a contar hombres primero y mujeres despues,
# nunca intercalados. En cada caso vamos a contar hasta
# 5 y cambiamos al otro grupo.

from random import choice

GENEROS = ['masculino', 'femenino']
MAX_EVENTOS = 10
MAX_PERSONAS_POR_TURNO = 5

turno = 'masculino'
contador = 0

def devolver_genero():
    return choice(GENEROS)

def siguiente_elemento_rotativo(lista, elemento):
    """
    Devuelve el siguiente elemento de forma rotativa.
    Solo funciona con listas de elementos distintos.
    """
    posicion_elemento = lista.index(elemento)
    indice_siguiente = (posicion_elemento + 1) % len(lista)
    return lista[indice_siguiente]

def cambiar_turno(turno):
    return siguiente_elemento_rotativo(GENEROS, turno)

def contar(genero, turno, contador):
    if genero == turno:
        contador += 1
    return contador

def problema(contador, turno):
    for x in range(MAX_EVENTOS):
        genero = devolver_genero()
        print "genero devuelto: %s" % genero
        contador = contar(genero, turno, contador)
        if contador == MAX_PERSONAS_POR_TURNO:
            contador = 0
            turno = cambiar_turno(turno)
    return (contador, turno)

if __name__ == '__main__':
    contador, turno = problema(contador, turno)
    print "contador: %d" % contador
    print "turno: %s" % turno
