# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 11:19:01 2024

@author: Sérgio
"""

dados = ["Caroline Paula Oliveira da Silva", 0,1.7,True]

def formulario(dados):
    print(f"Nome........: {dados[0]}")
    print(f"Filhos......: {dados[1]}")
    print(f"Estatura....: {dados[2]:.2f}m")
    if dados[3] == True:
        print("Usa instagram: sim")
    else:
        print("Usa instagram: não")

formulario(dados)