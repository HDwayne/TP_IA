"""
Fichier: fonctions.py
Auteur: Dwayne HERZBERG, Nathan FLEURY
description:
    Ce fichier contient les fonctions utilisées par le programme.
"""

from typing import Callable, List, Optional, Tuple
from copy import deepcopy
from classes import Rumba

################################################################################
# Heuristiques
################################################################################


def manhattan_distance(init: Rumba, goal: Rumba) -> int:
    total_distance = 0
    for i, tige in enumerate(init.tiges):
        for j, element in enumerate(tige.elements):
            for k, tige_but in enumerate(goal.tiges):
                for l, element_but in enumerate(tige_but.elements):
                    if element == element_but:
                        total_distance += abs(i - k) + abs(j - l)

    return total_distance


def nombreMalMis(init: Rumba, goal: Rumba) -> int:
    mal_places = 0
    for i, tige in enumerate(init.tiges):
        for j, element in enumerate(tige.elements):
            if (j >= goal.tiges[i].size()):
                mal_places += 1
            elif element != goal.tiges[i].elements[j]:
                mal_places += 1
    return mal_places


################################################################################
# Algorithme IDA*
################################################################################


def search(path: List[Rumba], g: int, bound, heuristique, but):
    node = path[-1]
    f = g + heuristique(node, but)
    if f > bound:
        return f
    if node == but:
        return "found"
    min = float("inf")
    for op, etat, cout in node.opPoss():
        if etat not in path:
            path.append(etat)
            t = search(path, g + cout, bound,
                       heuristique, but)
            if t == "found":
                return "found"
            if t < min:
                min = t
            path.pop()
    return min


def IDA_star(depart: Rumba,
             heuristique: Callable[[Rumba, Rumba], int],
             but: Rumba) -> Optional[Rumba]:
    bound = heuristique(depart, but)
    path = [depart]
    while True:
        t = search(path, 0, bound, heuristique, but)
        print("bound", bound)
        if t == "found":
            return (path, bound)
        elif t == float("inf"):
            return "no solution"
        bound = t
