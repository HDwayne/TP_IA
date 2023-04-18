"""
Fichier: classes.py
Auteur: Dwayne HERZBERG, Nathan FLEURY
description:
    Ce fichier contient les classes Element, Tige et Rumba.
"""


from copy import deepcopy


class TerminalColors:
    WHITE = '\033[97m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'


class Element:
    def __init__(self, couleur: str, chiffre: int):
        assert type(
            couleur) is str, "couleur doit être une chaîne de caractères"
        assert type(chiffre) is int, "chiffre doit être un entier"
        self.couleur = couleur
        self.chiffre = chiffre

    def __str__(self) -> str:
        return f"{self.couleur} {self.chiffre}"

    def __eq__(self, other) -> bool:
        if (other == None):
            return False
        return self.couleur == other.couleur and self.chiffre == other.chiffre

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def colored(self) -> str:
        match self.couleur:
            case "bleu":
                return f"{TerminalColors.BLUE}{self.couleur} {self.chiffre}{TerminalColors.ENDC}"
            case "jaune":
                return f"{TerminalColors.YELLOW}{self.couleur} {self.chiffre}{TerminalColors.ENDC}"
            case "rouge":
                return f"{TerminalColors.RED}{self.couleur} {self.chiffre}{TerminalColors.ENDC}"
            case _:
                return f"{TerminalColors.WHITE}{self.couleur} {self.chiffre}{TerminalColors.ENDC}"


class Tige:
    def __init__(self, taille: int):
        assert type(taille) is int, "taille doit être un entier"
        assert taille > 0, "La taille doit être positive"
        self.taille: int = taille
        self.elements: list = []

    def __str__(self) -> str:
        return str([str(element) for element in self.elements]) + f" - {self.size()} / {self.max_size()}"

    def __eq__(self, other) -> bool:
        return self.elements == other.elements

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def est_vide(self) -> bool:
        return self.size() == 0

    def est_pleine(self) -> bool:
        return self.size() == self.max_size()

    def empiler(self, element: Element) -> None:
        try:
            self.elements.append(element)
        except Exception as e:
            raise Exception("La pile est pleine") from e

    def depiler(self) -> Element:
        if self.est_vide():
            raise Exception("La pile est vide")
        return self.elements.pop()

    def size(self) -> int:
        return len(self.elements)

    def max_size(self) -> int:
        return self.taille

    def as_list(self) -> list:
        return self.elements

    def head(self) -> Element:
        if self.est_vide():
            return None
        return self.elements[-1]


class Rumba:
    def __init__(self, tailleTige: int, taille: int):
        assert type(tailleTige) is int, "tailleTige doit être un entier"
        assert type(taille) is int, "taille doit être un entier"
        self.taille = taille
        self.tiges: list[Tige] = [Tige(tailleTige) for i in range(taille)]

    def __str__(self) -> str:
        return "\n".join([f"Tige {i+1} : {tiges}" for i, tiges in enumerate(self.tiges)])

    def __eq__(self, other) -> bool:
        return all([tige == other_tige for tige, other_tige in zip(self.tiges, other.tiges)])

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __getitem__(self, index: int) -> Tige:
        try:
            return self.tiges[index]
        except IndexError:
            raise IndexError("Index out of range")
        except TypeError:
            raise TypeError("Index must be an integer")

    def __hash__(self):
        return hash(str(self))

    def size(self) -> int:
        return self.taille

    def deplacer(self, index_depart: int, index_arrivee: int) -> None:
        td = self.tiges[index_depart-1]
        ta = self.tiges[index_arrivee-1]
        if not td.est_vide():
            if not ta.est_pleine():
                ta.empiler(td.depiler())

    def afficherEtat(self) -> None:
        max_size = max([tige.size() for tige in self.tiges])

        for i in range(max_size, 0, -1):
            row = []
            for tige in self.tiges:
                if tige.size() >= i:
                    row.append(
                        tige.elements[i-1].colored() + " "*(max([len(str(element)) for element in tige.elements])-len(str(tige.elements[i-1]))))
                else:
                    row.append(
                        " " * len(str(tige.elements[0])) if tige.elements else " "*7)
            print(" | ".join(row))

        sperator = ["‒" * (len(str(tige.elements[0])))
                    if tige.elements else "‒"*7 for tige in self.tiges]

        tige_labels = [f"Tige {i+1}" for i, tige in enumerate(self.tiges)]

        label_spacing = [len(str(tige.elements[0]))
                         if tige.elements else 7 for tige in self.tiges]

        aligned_labels = [f"{label:^{spacing}}" for label,
                          spacing in zip(tige_labels, label_spacing)]

        print(" | ".join(sperator))
        print(" | ".join(aligned_labels))

    def trouverDestinations(self, tige_depart: Tige) -> list:
        destinations = []
        for tige in self.tiges:
            if tige != tige_depart:
                if not tige.est_pleine():
                    destinations.append(tige)
        return destinations

    def opPoss(self) -> list:
        """
        Fonction qui prend en paramètre un état de type Rumba et renvoi une liste de tuple de la forme (opération, nouvel état, coût).
        Pour chaque état de la liste de tuple, la valeur de la variable operation est une chaîne de caractère indiquant l'opération
        qui a été effectuée pour passer de l'état init à cet état, nouvel_etat est l'état résultant de l'opération et coût est le coût
        de l'opération.
        """
        operations = []
        for i, tige_depart in enumerate(self.tiges):
            for j, tige_arrivee in enumerate(self.tiges):
                if i != j and not tige_depart.est_vide() and not tige_arrivee.est_pleine():
                    nouvel_etat = deepcopy(self)
                    nouvel_etat.deplacer(i, j)
                    operation = f"Deplacer {tige_depart.head()} de Tige {i+1} à Tige {j+1}"
                    operations.append((operation, nouvel_etat, 1))
        return operations
