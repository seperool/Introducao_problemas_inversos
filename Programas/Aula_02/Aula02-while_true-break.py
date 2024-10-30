# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:37:04 2024

@author: Sérgio
"""

print("*** Operação de divisão ***")
prompt1 = "Infome o primeiro número: "
prompt2 = "Infome o segundo número: "
while True:
    n1 = int(input(prompt1))
    n2 = int(input(prompt2))
    if n2 == 0:
        prompt3 = "O divisor não pode ser 0."
        prompt3 += "\nO programa será encerrado ..."
        print(prompt3)
        break
    print(f"n1/n2 = {n1/n2:.2f}")
print("*** Fim do programa ***")