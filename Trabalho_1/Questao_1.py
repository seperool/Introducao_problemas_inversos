# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:53:56 2024

@author: Sérgio
"""

def desmembra_num(num):
    """
    Recebe um número qualquer e desmembra ele.
    Devolve uma lista com cada digito do número.
    """
    lista_num_fatiado =[]
    x = 1
    while len(str(num)) >= x:
        parte = int((num%10**x - num%10**(x-1))/10**(x-1))
        lista_num_fatiado.append(parte)
        x += 1
        print(lista_num_fatiado)
    return lista_num_fatiado

def inverte_num(lista_num_fatiado):
    """
    Recebe uma lista de digitos, inverete e concatena  a lista.
    """
    j=1
    num_inv = 0
    for dig in lista_num_fatiado:
        num_inv = num_inv + dig*(10**(len(lista_num_fatiado)-j))
        j+=1
        print(num_inv)
    print("Número invertido: ")
    print(int(num_inv))

def inv_digitos():
    """
    Chama as funções que destrincha um número qualquer e
    inverte e concatena a lista dos digitos.
    """
    num = int(input("digite um numero inteiro: "))
    print(num)
    lista_dig = desmembra_num(num)
    decisao = input("Gostaria de inverter o número(y/n): ")
    if decisao == "y":
        inverte_num(lista_dig)

#Chama as funções
inv_digitos()