"""
Fichier: main.py
Auteur: Dwayne HERZBERG, Nathan FLEURY
description:
    Ce fichier contient le code principal du programme.
"""

from fonctions import *
from test import *


si1 = situation_initiale_1()
si2 = situation_initiale_2()
but1 = but_1()
but2 = but_2()
but3 = but_3()
but4 = but_4()
but5 = but_5()
but6 = but_6()
but7 = but_7()

# afficher

# si1.afficherEtat()
# but1.afficherEtat()

# heuristique

# print(heuristique(si1, but5))
# print(heuristique(si1, si1))

# opPoss

# for op, init, n in opPoss(si):
#     print(op)

# estBut

# print(estBut(si, but5))
# print(estBut(but6, but7))
# print(but6.afficherEtat())
# print(opPoss(but6))

result = IDA_star(si1, nombreMalMis, but3)
print(result)

# for but in [but1, but2, but3, but4, but5]:
#     result = IDA_star(si1, but)
#     print(result)
