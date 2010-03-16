#!/usr/bin/env python2.6

# exercicios:
# 1. escrever transpose e show usando for e map

notas = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']

def transpose(lista_de_notas, eixo):
    return [(x + eixo) % 12 for x in lista_de_notas]

def show(lista_de_numeros):
    return [notas[x] for x in lista_de_numeros]

print transpose([1,20,3], 3)
print show(transpose([1,20,3], 3))
