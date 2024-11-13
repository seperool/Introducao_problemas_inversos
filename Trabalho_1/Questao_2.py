# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 17:13:02 2024

@author: Sérgio
"""

#Função desmembra número inteiro
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
        #print(lista_num_fatiado)
    return lista_num_fatiado

def num_descartar(lista_num_fatiado):
    i=0 #Contador
    i1 = 0 #Criterio 1 = dig 1, conta interação
    i2 = 0 #Criterio 2 = dig 7
    mensagem = "o número não é meliante!"
    for dig in lista_num_fatiado:
        i+=1
        print(f"digito: {dig}")
        if dig == 1: #Criterio 1
            if i1 == (i - 2):
                print("")
            else:
                i1=i
                print("entrou 1")
        if dig == 7 and (i1 == (i - 1)): #Criterio 2
            i2 = i
            print("entrou 2")
        if dig == 1 and ((i2 == (i - 1)) and (i1 == (i - 2))): #Criterio final
            mensagem = "o numero é meliante!"
            print("entrou 3")
    
    #Mensagem final
    print(mensagem)

numero = int(input("Digite um número inteiro: "))
lista = desmembra_num(numero)
num_descartar(lista)