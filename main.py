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

# test déplacement (affiche les déplacements possibles depuis la situation initiale)


# si1.afficherEtat()
# for op, etatSucc, cout in si1.opPoss():
#     print(op)
#     etatSucc.afficherEtat()


# test heuristique (affiche le nombre d'éléments mal placés et la distance de Manhattan)


# si1.afficherEtat()
# but3.afficherEtat()
# print(nombreMalMis(si1, but3))
# print(manhattan_distance(si1, but3))


# test IDA* (affiche le résultat de l'algorithme)


# result = IDA_star(si1, nombreMalMis, but2)
# print(result)


# test IDA* (affiche le résultat de l'algorithme pour toutes les situations initiales et buts)


# for but in [but1, but2, but3, but4, but5]:
#     result = IDA_star(si1, nombreMalMis, but)
#     print(result)
