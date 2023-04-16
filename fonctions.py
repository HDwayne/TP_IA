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


def heuristique(init: Rumba, but: Rumba):
    """
    Fonction qui calcule l'heuristique de l'état init en fonction de l'état but.
    """
    if not isinstance(init, Rumba):
        raise TypeError(f"init must be of type {Rumba}")
    if not isinstance(but, init.__class__):
        raise TypeError(f"but must be of type {init.__class__}")
    h = manhattan_distance(init, but)
    return h


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
    return init.__eq__(but)


def search(path: List[Rumba], g: int, bound, is_goal, heuristique, successors, but):
    node = path[-1]
    f = g + heuristique(node, but)
    if f > bound:
        return f
    if is_goal(node, but):
        return "found"
    min = float("inf")
    for op, etat, cout in successors(node):
        if etat not in path:
            path.append(etat)
            t = search(path, g + cout, bound, is_goal,
                       heuristique, successors, but)
            if t == "found":
                return "found"
            if t < min:
                min = t
            path.pop()
    return min


def IDA_star(depart: Rumba,
             is_goal: Callable[[Rumba, Rumba], bool],
             successors: Callable[[Rumba], List[Tuple[str, Rumba, int]]],
             heuristique: Callable[[Rumba, int, Rumba], int],
             but: Rumba) -> Optional[Rumba]:
    bound = heuristique(depart, but)
    path = [depart]
    while True:
        t = search(path, 0, bound, is_goal, heuristique, successors, but)
        print("bound", bound)
        if t == "found":
            return (path, bound)
        elif t == float("inf"):
            return "no solution"
        bound = t
