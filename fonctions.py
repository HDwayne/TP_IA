"""
Fichier: fonctions.py
Auteur: Dwayne HERZBERG, Nathan FLEURY
description:
    Ce fichier contient les fonctions utilisées par le programme.
"""

from typing import Callable, List, Optional, Tuple
from copy import deepcopy
from classes import Rumba


def manhattan_distance(init: Rumba, goal: Rumba) -> int:
    """
    Fonction qui calcule la distance de Manhattan entre l'état init et l'état but.
    """
    if not isinstance(init, Rumba):
        raise TypeError(f"init must be of type {Rumba}")
    if not isinstance(goal, init.__class__):
        raise TypeError(f"goal must be of type {init.__class__}")

    total_distance = 0
    for i, tige in enumerate(init.tiges):
        for j, element in enumerate(tige.elements):
            for k, tige_but in enumerate(goal.tiges):
                for l, element_but in enumerate(tige_but.elements):
                    if element == element_but:
                        total_distance += abs(i - k) + abs(j - l)

    return total_distance


def heuristique(init: Rumba, g: int, but: Rumba):
    """
    Fonction qui calcule l'heuristique de l'état init en fonction de l'état but.
    """
    if not isinstance(init, Rumba):
        raise TypeError(f"init must be of type {Rumba}")
    if not isinstance(but, init.__class__):
        raise TypeError(f"but must be of type {init.__class__}")
    if not isinstance(g, int):
        raise TypeError(f"g must be of type int")
    h = manhattan_distance(init, but)
    return g + h


def opPoss(init: Rumba) -> list:
    """
    Fonction qui prend en paramètre un état de type Rumba et renvoi une liste de tuple de la forme (opération, nouvel état, coût).
    Pour chaque état de la liste de tuple, la valeur de la variable operation est une chaîne de caractère indiquant l'opération
    qui a été effectuée pour passer de l'état init à cet état, nouvel_etat est l'état résultant de l'opération et coût est le coût
    de l'opération.
    """
    if not isinstance(init, Rumba):
        raise TypeError(f"init must be of type {Rumba}")
    operations = []
    for i, tige_depart in enumerate(init.tiges):
        for j, tige_arrivee in enumerate(init.tiges):
            if i != j and not tige_depart.est_vide() and not tige_arrivee.est_pleine():
                nouvel_etat = deepcopy(init)
                nouvel_etat.deplacer(i, j)
                operation = f"Deplacer {tige_depart.head()} de Tige {i+1} à Tige {j+1}"
                operations.append((operation, nouvel_etat, 1))
    return operations


def estBut(init: Rumba, but: Rumba) -> bool:
    if not isinstance(init, Rumba):
        raise TypeError(f"init must be of type {Rumba}")
    if not isinstance(but, init.__class__):
        raise TypeError(f"but must be of type {init.__class__}")
    return init == but


# def IDA_star(init: Rumba, goal: Rumba) -> Tuple[List[str], int]:
#     def search(path: List[Rumba], g: int, bound: int) -> Tuple[int, List[Rumba]]:
#         node = path[-1]
#         f = g + heuristique(node, g, goal)
#         if f > bound:
#             return f, []
#         if estBut(node, goal):
#             return f, path
#         min_cost = float('inf')
#         for operation, child, cost in opPoss(node):
#             if child not in path:
#                 path.append(child)
#                 new_bound, result = search(path, g + cost, bound)
#                 if result:
#                     return new_bound, result
#                 min_cost = min(min_cost, new_bound)
#                 path.pop()
#         return min_cost, []

#     path = [init]
#     bound = heuristique(init, 0, goal)
#     while True:
#         new_bound, result = search(path, 0, bound)
#         if result:
#             operations = []
#             for i in range(len(result) - 1):
#                 tige_depart, tige_arrivee = None, None
#                 for tige_index in range(init.size()):
#                     if result[i].tiges[tige_index] != result[i + 1].tiges[tige_index]:
#                         if result[i].tiges[tige_index].head() == result[i + 1].tiges[tige_index].head():
#                             tige_arrivee = tige_index
#                         else:
#                             tige_depart = tige_index
#                 print(tige_arrivee, tige_depart)
#                 operations.append(
#                     f"Deplacer {result[i].tiges[tige_depart].head()} de Tige {tige_depart + 1} à Tige {tige_arrivee + 1}")
#             return operations, new_bound
#         bound = new_bound


def search(path: List[Rumba], g: int, bound, is_goal, h, successors, but):
    node = path[-1]
    f = g + h(node, g, but)
    if f > bound:
        return f
    if is_goal(node, but):
        return "found"
    min = float("inf")
    for op, etat, cout in successors(node):
        if etat not in path:
            # print(f"Opération: {op}")
            path.append(etat)
            t = search(path, g + cout, bound, is_goal, h, successors, but)
            if t == "found":
                return "found"
            if t < min:
                min = t
            path.pop()
    # print("path", path)
    return min


def IDA_star(depart: Rumba,
             is_goal: Callable[[Rumba, Rumba], bool],
             successors: Callable[[Rumba], List[Tuple[str, Rumba, int]]],
             h: Callable[[Rumba, int, Rumba], int],
             but: Rumba) -> Optional[Rumba]:
    bound = h(depart, 0, but)
    path = [depart]
    while True:
        t = search(path, 0, bound, is_goal, h, successors, but)
        print("bound", bound)
        if t == "found":
            return (path, bound)
        elif t == float("inf"):
            return "no solution"
        bound = t
