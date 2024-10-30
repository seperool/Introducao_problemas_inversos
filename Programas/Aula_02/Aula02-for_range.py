# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:18:50 2024

@author: Sérgio
"""

soma = 0
for termo in range(1,11):
    soma += termo
    print(str(termo)+ " - " +str(soma))

print(f"A soma dos 10 primeiros termos: {soma}")