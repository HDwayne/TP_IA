class TerminalColors:
    WHITE = '\033[97m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'


class Element:
    def __init__(self, couleur: str, chiffre: int):
        if type(couleur) is not str:
            raise TypeError("couleur doit être une chaîne de caractères")
        if type(chiffre) is not int:
            raise TypeError("chiffre doit être un entier")
        self.couleur = couleur
        self.chiffre = chiffre

    def __str__(self) -> str:
        return f"{self.couleur} {self.chiffre}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            raise TypeError(f"other must be of type {self.__class__}")
        return self.couleur == other.couleur and self.chiffre == other.chiffre

    def __ne__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            raise TypeError(f"other must be of type {self.__class__}")
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
        if not isinstance(taille, int):
            raise TypeError("taille doit être un entier")
        if taille <= 0:
            raise ValueError("La taille doit être positive")
        self.taille: int = taille
        self.elements: list = []

    def __str__(self) -> str:
        return str([str(element) for element in self.elements]) + f" - {self.size()} / {self.max_size()}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            raise TypeError(f"other must be of type {self.__class__}")
        return self.elements == other.elements

    def __ne__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            raise TypeError(f"other must be of type {self.__class__}")
        return not self.__eq__(other)

    def est_vide(self) -> bool:
        return self.size() == 0

    def est_pleine(self) -> bool:
        return self.size() == self.max_size()

    def empiler(self, element: Element) -> None:
        if not isinstance(element, Element):
            raise TypeError("element must be of type Element")
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
            raise Exception("La pile est vide")
        return self.elements[-1]


class Rumba:
    def __init__(self, tailleTige: int, taille: int):
        if not isinstance(tailleTige, int):
            raise TypeError("tailleTige must be of type int")
        if not isinstance(taille, int):
            raise TypeError("taille must be of type int")
        self.taille = taille
        self.tiges: list[Tige] = [Tige(tailleTige) for i in range(taille)]

    def __str__(self) -> str:
        return "\n".join([f"Tige {i+1} : {tiges}" for i, tiges in enumerate(self.tiges)])

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            raise TypeError(f"other must be of type {self.__class__}")
        return all([tige == other_tige for tige, other_tige in zip(self.tiges, other.tiges)])

    def __ne__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            raise TypeError(f"other must be of type {self.__class__}")
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
        if not isinstance(index_depart, int):
            raise TypeError("index_depart must be of type int")
        if not isinstance(index_arrivee, int):
            raise TypeError("index_arrivee must be of type int")
        if index_depart < 0 or index_depart > self.size():
            raise ValueError(
                "index_depart must be between 0 and the size of the game")
        if index_arrivee < 0 or index_arrivee > self.size():
            raise ValueError(
                "index_arrivee must be between 0 and the size of the game")
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
        if not isinstance(tige_depart, Tige):
            raise TypeError("tige_depart must be of type Tige")
        if tige_depart not in self.tiges:
            raise ValueError("tige_depart must be in the game")
        destinations = []
        for tige in self.tiges:
            if tige != tige_depart:
                if not tige.est_pleine():
                    destinations.append(tige)
        return destinations

    def nombreMalMis(self, but: 'Rumba') -> int:
        if not isinstance(but, self.__class__):
            raise TypeError(f"but must be of type {self.__class__}")
        mal_places = 0
        for i, tige in enumerate(self.tiges):
            for j, element in enumerate(tige.elements):
                if (j >= but.tiges[i].size()):
                    mal_places += 1
                elif element != but.tiges[i].elements[j]:
                    mal_places += 1
        return mal_places


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
        if t == "found":
            return (path, bound)
        elif t == float("inf"):
            return "no solution"
        bound = t


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


si1 = situation_initiale_1()
but2 = but_2()

result = IDA_star(si1, estBut, opPoss, heuristique, but2)
print(result)
