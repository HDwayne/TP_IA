"""
Fichier: test.py
Auteur: Dwayne HERZBERG, Nathan FLEURY
description:
    Ce fichier contient les Etats initiaux et les Etats buts pour les tests
    de l'algorithme IDA*.
"""

from classes import Rumba, Element


def situation_initiale_1() -> Rumba:
    rb = Rumba(3, 4)
    rb.tiges[0].empiler(Element("jaune", 3))
    rb.tiges[0].empiler(Element("jaune", 2))
    rb.tiges[1].empiler(Element("jaune", 1))
    rb.tiges[2].empiler(Element("bleu", 3))
    rb.tiges[2].empiler(Element("bleu", 2))
    rb.tiges[2].empiler(Element("bleu", 1))
    rb.tiges[3].empiler(Element("rouge", 3))
    rb.tiges[3].empiler(Element("rouge", 2))
    rb.tiges[3].empiler(Element("rouge", 1))
    return rb


def situation_initiale_2() -> Rumba:
    rb = Rumba(3, 4)
    rb.tiges[0].empiler(Element("jaune", 3))
    rb.tiges[0].empiler(Element("jaune", 2))
    rb.tiges[0].empiler(Element("jaune", 1))
    rb.tiges[1].empiler(Element("bleu", 3))
    rb.tiges[1].empiler(Element("bleu", 2))
    rb.tiges[1].empiler(Element("bleu", 1))
    rb.tiges[2].empiler(Element("rouge", 3))
    rb.tiges[2].empiler(Element("rouge", 2))
    rb.tiges[2].empiler(Element("rouge", 1))
    return rb


def but_1() -> Rumba:
    rb = Rumba(3, 4)
    rb.tiges[0].empiler(Element("jaune", 3))
    rb.tiges[0].empiler(Element("jaune", 2))
    rb.tiges[0].empiler(Element("jaune", 1))
    rb.tiges[2].empiler(Element("bleu", 3))
    rb.tiges[2].empiler(Element("bleu", 2))
    rb.tiges[2].empiler(Element("bleu", 1))
    rb.tiges[3].empiler(Element("rouge", 3))
    rb.tiges[3].empiler(Element("rouge", 2))
    rb.tiges[3].empiler(Element("rouge", 1))
    return rb


def but_2() -> Rumba:
    rb = Rumba(3, 4)
    rb.tiges[0].empiler(Element("jaune", 3))
    rb.tiges[0].empiler(Element("jaune", 2))
    rb.tiges[0].empiler(Element("jaune", 1))
    rb.tiges[1].empiler(Element("rouge", 3))
    rb.tiges[1].empiler(Element("rouge", 2))
    rb.tiges[1].empiler(Element("rouge", 1))
    rb.tiges[2].empiler(Element("bleu", 3))
    rb.tiges[2].empiler(Element("bleu", 2))
    rb.tiges[2].empiler(Element("bleu", 1))
    return rb


def but_3() -> Rumba:
    rb = Rumba(3, 4)
    rb.tiges[0].empiler(Element("jaune", 3))
    rb.tiges[0].empiler(Element("jaune", 2))
    rb.tiges[0].empiler(Element("rouge", 1))
    rb.tiges[1].empiler(Element("bleu", 3))
    rb.tiges[1].empiler(Element("bleu", 1))
    rb.tiges[1].empiler(Element("rouge", 2))
    rb.tiges[2].empiler(Element("rouge", 3))
    rb.tiges[2].empiler(Element("bleu", 2))
    rb.tiges[2].empiler(Element("jaune", 1))
    return rb


def but_4() -> Rumba:
    rb = Rumba(3, 4)
    rb.tiges[0].empiler(Element("jaune", 3))
    rb.tiges[0].empiler(Element("jaune", 1))
    rb.tiges[0].empiler(Element("jaune", 2))
    rb.tiges[1].empiler(Element("bleu", 3))
    rb.tiges[1].empiler(Element("bleu", 1))
    rb.tiges[1].empiler(Element("bleu", 2))
    rb.tiges[2].empiler(Element("rouge", 3))
    rb.tiges[2].empiler(Element("rouge", 1))
    rb.tiges[2].empiler(Element("rouge", 2))
    return rb


def but_5() -> Rumba:
    rb = Rumba(3, 4)
    rb.tiges[0].empiler(Element("jaune", 3))
    rb.tiges[0].empiler(Element("jaune", 2))
    rb.tiges[0].empiler(Element("rouge", 2))
    rb.tiges[1].empiler(Element("bleu", 3))
    rb.tiges[1].empiler(Element("bleu", 1))
    rb.tiges[2].empiler(Element("rouge", 3))
    rb.tiges[2].empiler(Element("rouge", 1))
    rb.tiges[2].empiler(Element("bleu", 2))
    rb.tiges[3].empiler(Element("jaune", 1))
    return rb


def but_6() -> Rumba:
    rb = Rumba(3, 4)
    rb.tiges[0].empiler(Element("bleu", 1))
    rb.tiges[0].empiler(Element("rouge", 1))
    rb.tiges[0].empiler(Element("jaune", 1))
    rb.tiges[1].empiler(Element("bleu", 2))
    rb.tiges[1].empiler(Element("rouge", 2))
    rb.tiges[1].empiler(Element("jaune", 2))
    rb.tiges[2].empiler(Element("bleu", 3))
    rb.tiges[2].empiler(Element("rouge", 3))
    rb.tiges[2].empiler(Element("jaune", 3))
    return rb


def but_7() -> Rumba:
    rb = Rumba(3, 4)
    rb.tiges[0].empiler(Element("bleu", 1))
    rb.tiges[0].empiler(Element("rouge", 1))
    rb.tiges[0].empiler(Element("jaune", 1))
    rb.tiges[1].empiler(Element("bleu", 2))
    rb.tiges[1].empiler(Element("rouge", 2))
    rb.tiges[1].empiler(Element("jaune", 2))
    rb.tiges[2].empiler(Element("bleu", 3))
    rb.tiges[2].empiler(Element("rouge", 3))
    rb.tiges[2].empiler(Element("jaune", 3))
    return rb
