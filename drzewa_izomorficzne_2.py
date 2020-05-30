"""
Program sprawdza czy podane dwa drzewa ukorzenione są izomorficzne.
"""

class Node(): # Węzęł
    def __init__(self, name, parent=None, id=-1):
        self.name = name # Nazwa węzła
        self.parent = parent # Rodzic węzła
        self.children = None # Dzieci węzła
        self.id = id # id węzła

    def __str__(self): # Wypisuje dane o węźle
        if self.parent is None: # root - nie ma rodzica
            return "Node:{}, id:{} ROOT".format(self.name, self.id)
        elif self.children is None: # liść - nie ma dzieci
            return "Node:{}, Parent:{}, id:{} LEAF".format(self.name, self.parent.name, self.id)
        else:
            return "Node:{}, Parent:{}, id:{}".format(self.name, self.parent.name, self.id)


class Tree(): # Drzewo jako lista węzłów z zależnościami zawartymi w węzłach(dzieci, rodzice, id)
    def __init__(self, root, nodes):
        self.root = root # Korzeń drzewa
        self.nodes = nodes # Lista węzłów

    def __str__(self): # Wypisuje dane o drzewie
        tree = ""
        for node in self.nodes:
            tree = tree + "\n" + node.__str__()
        return tree

    def identificator(self): # Wylicza identyfikator drzewa
        id_dict = {} # Słownik identyfikatorów
        children_id_list = [] # Multizbiór identyfikatorów dzieci danego rodzica
        parents_of_leaves = [] # Lista rodziców aktulanych liści

        while self.nodes[0].id == -1: # Dopóki korzeń drzewa nie otrzyma identyfikatora
            parents_of_leaves = []

            for node in self.nodes: # Dla każdego węzła w drzewie
                if node.children is None :  # Jeśli węzeł jest liściem
                    for child in node.parent.children: # Dla każdego dziecka rodzica aktualnie przeglądanego dziecka
                        if child.children is not None: # Jeśli dziecko rodzica ma dzieci - rodzic nie może mieć wyznaczonego identyfikatora
                            break
                    else: # Dodanie rodzica liścia do listy, mogę wyznaczyć idenytyfikator rodzica
                        parents_of_leaves.append(node.parent)

            parents_of_leaves = list(set(parents_of_leaves)) # Usunięcie powtórzeń nazw rodziców

            for parent_node in parents_of_leaves: # Dla każdego rodzica aktualnych liści
                for child_node in parent_node.children: # Dla każdego dziecka przeglądanego rodzica
                    children_id_list.append(child_node.id) # Dodanie identyfikatora dziecka do listy
                children_id_list.sort() # Posortowanie listy identyfikatorów dzieci
                if children_id_list.__str__() not in id_dict.keys(): # Sprawdzenie czy taka lista identyfikatorów istnieje w słowniku
                    id_dict.update({children_id_list.__str__(): len(id_dict)+1}) # Jeśli nie istnieje, jest dodana
                parent_node.id = id_dict.get(children_id_list.__str__()) # Ustawienie nowego identyfikatora dla rodzica
                children_id_list.clear() # Wyczyszczenie listy dzieci aktualnego rodzica

            leaves_to_delete = [] # Lista liści, które zostaną usunięte z drzewa

            for node in self.nodes: # Dla każdego węzła w drzewie
                if node.children is None: # Jeśli węzeł jest liściem
                    for child in node.parent.children: # Jeśli dziecko rodzica ma dzieci - rodzic nie może mieć wyznaczonego identyfikatora
                        if child.children is not None:
                            break
                    else: # Dodanie węzła do listy, może zostać usunięty z drzewa
                        leaves_to_delete.append(node)

            for node in leaves_to_delete: # Usunięcie wcześniej wybranych liści
                node.parent.children = None
                self.nodes.remove(node)

        return self.nodes[0].id # Zwrócenie identyfikatora drzewa


if __name__ == "__main__":

    # Drzewo z prezentacji Slajd 16, drzewo T1
    A = Node("A")
    B = Node("B", A)
    C = Node("C", A)
    D = Node("D", B, 0)
    E = Node("E", B, 0)
    F = Node("F", B, 0)
    G = Node("G", C)
    H = Node("H", C, 0)
    I = Node("I", C)
    J = Node("J", G, 0)
    K = Node("K", G, 0)
    L = Node("L", I, 0)
    M = Node("M", I, 0)
    A.children = [B, C]
    B.children = [D, E, F]
    C.children = [G, H, I]
    G.children = [J, K]
    I.children = [L, M]
    first_tree = Tree(A, [A, B, C, D, E, F, G, H, I, J, K, L, M])

    # Drzewo z prezentacji Slajd 16, drzewo T2
    A1 = Node("A1")
    B1 = Node("B1", A1)
    C1 = Node("C1", A1)
    D1 = Node("D1", B1)
    E1 = Node("E1", B1)
    F1 = Node("F1", B1)
    G1 = Node("G1", C1, 0)
    H1 = Node("H1", C1, 0)
    I1 = Node("I1", C1, 0)
    J1 = Node("J1", D1, 0)
    K1 = Node("K1", D1, 0)
    L1 = Node("L1", E1, 0)
    M1 = Node("M1", E1, 0)
    A1.children = [B1, C1]
    B1.children = [D1, E1, F1]
    C1.children = [G1, H1, I1]
    D1.children = [J1, K1]
    E1.children = [L1, M1]
    second_tree = Tree(A1, [A1, B1, C1, D1, E1, F1, G1, H1, I1, J1, K1, L1, M1])

    T1_id = first_tree.identificator()
    T2_id = second_tree.identificator()
    if T1_id == T2_id:
        print("Identyfikatory są równe (ID={}). ".format(T1_id) +
            "Drzewa są izomorficzne!")
    else:
        print("Identyfikatory nie są równe (T1_ID={} - T2_ID={}). ".format(T1_id, T2_id) +
            "Drzewa nie są izomorficzne!")