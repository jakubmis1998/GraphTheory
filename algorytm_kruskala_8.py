"""
Algorytm Kruskala z własną implementacją kopca(push, pop) i funkcji UNION, FIND.
"""

class Graph:
    """Klasa reprezentująca graf"""

    def __init__(self):
        self.V = 0  # liczba wierzchołków
        self.E = 0  # liczba krawędzi
        self.father = []  # lista ojców
        self.rank = {}  # rangi
        self.edges = [] # lista krawędzi

    def read_graph(self):
        """Wczytanie grafu"""

        # Wczytanie ilości wierzchołków i krawędzi
        vertices_and_edges = input("Podaj ilość wierzchołków i krawędzi [n m]: ")
        n, m = vertices_and_edges.split(" ")
        n = int(n)
        m = int(m)

        # Ustawienie ilości wierzchołków i krawędzi
        self.V = n
        self.E = m

        # Wczytanie krawędzi
        print("Podaj krawędzie [v1 v2 weight]: ")
        for i in range(m):
            edge = input()
            v1, v2, weight = edge.split(" ")
            self.edges.append(Edge(int(v1), int(v2), int(weight)))

    def find(self, v):
        """Operacja FIND
        
        Znajduje reprezentanta podzbioru danego wierzchołka
        """
        if self.father[v] == v:
            return v
        return self.find(self.father[v])
    
    def union(self, v1, v2):
        """Operacja UNION

        Wykonuje sumę podzbiorów, mniej liczny podzbiór jest włączany do liczniejszego.
        """
        # Znalezienie reprezentantów wierzchołków danej krawędzi
        root1 = self.find(v1)
        root2 = self.find(v2)

        # Mniejsza ranga podłączona do większej
        if self.rank[root1] < self.rank[root2]: 
            self.father[root1] = root2 
        elif self.rank[root1] > self.rank[root2]: 
            self.father[root2] = root1
        # Gdy rangi takie same, ranga wzrasta o 1
        else: 
            self.father[root2] = root1 
            self.rank[root1] += 1

    def make_set(self, v):
        """Inicjalizuje ojców i rangi dla danego wierzchołka"""
        self.father[v] = v
        self.rank[v] = 0

    def kruskal(self):
        """Algorytm Kruskala"""

        # MST
        T = []

        # Inicjalizacja zbiorów początkowych
        for v in range(self.V):
            self.father.append(-1)
            self.make_set(v)

        # Inicjalizacja kopca krawędziami grafu
        heap = Heap()
        for e in self.edges:
            heap.push(e)
        
        # Liczba krawędzi zbadanych, liczba krawędzi w T
        ecount = 0
        tcount = 0

        # Główna pętla
        while (tcount < self.V - 1) and (ecount < self.E):

            # Wzięcie krawędzi z najmniejszą wagą
            e = heap.pop()
            ecount += 1

            # Sprawdzenie czy wzięta krawędź tworzy cykl z krawędziami ze zbioru T
            r1 = self.find(e.get_v1())
            r2 = self.find(e.get_v2())
            if r1 != r2:
                T.append(e)
                tcount += 1
                self.union(r1, r2)

        if tcount < self.V - 1:
            print("Sieć nie jest spójna!")
        
        return T


class Edge:
    """Klasa reprezentująca krawędź ważoną"""

    def __init__(self, v1, v2, weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

    def get_weight(self):
        return self.weight

    def get_v1(self):
        return self.v1

    def get_v2(self):
        return self.v2

    def __str__(self):
        return "{} {} {}".format(self.v1, self.v2, self.weight)


class Heap:
    """Klasa reprezentująca kopiec MIN"""

    def __init__(self):
        self.array = []  # Tablica jako kopiec

    def push(self, edge):
        """Dodaje element do kopca"""

        # Ilośc elementów kopca
        i = len(self.array)

        # Powiększenie kopca o 1 element
        self.array.append(edge)
        j = (i - 1) // 2

        # Sprawdzenie warunku kopca
        while i > 0 and self.array[j].get_weight() > edge.get_weight():
            self.array[i] = self.array[j]
            i = j
            j = (i - 1) // 2

        # Ustawienie dodanej wartości
        self.array[i] = edge

    def pop(self):
        """Usuwa element z kopca"""

        # Gdy kopiec jest pusty
        if len(self.array) == 0:
            return

        # Ilość elemntów kopca zmniejszona o usuwany element
        n = len(self.array) - 1

        # Ostatnia krawędź, wstawiana do korzenia
        edge = self.array[n]

        # Korzeń, zwracany jako minimum całej tablicy
        top = self.array[0]

        # Usunięcie ostatniego elementu kopca
        self.array.pop()
        i = 0
        j = 1

        # Sprawdzenie warunku kopca i ustawienie ojca
        while(j < n):
            # Szukanie mniejszego syna
            if j + 1 < n and self.array[j + 1].get_weight() < self.array[j].get_weight():
                j += 1
            # Spełnienie warunku kopca
            if edge.get_weight() < self.array[j].get_weight():
                break
            # Mniejszy syn do ojca, przechodzimy na jego pozycję, wskazanie lewego syna
            self.array[i] = self.array[j]
            i = j
            j = 2 * j + 1

        # Ustawienie wartości
        self.array[i] = edge

        return top

    def print_heap(self):
        """Wypisuje elementy tablicy kopca"""
        for edge in self.array:
            print(edge)


if __name__ == "__main__":

    # Stworzenie grafu
    g = Graph()
    # Wczytanie grafu
    g.read_graph()
    # Obliczenie drzewa MST
    MST = g.kruskal()

    # Wypisanie drzewa MST
    print("\n*** MST ***")
    for edge in MST:
        print(edge)
    

# Przykładowe dane
"""
8 16
0 1 5
0 3 9
0 6 3
1 2 9
1 4 8
1 5 6
1 7 7
2 3 9
2 4 4
2 6 5
2 7 3
3 6 8
4 5 2
4 6 1
5 6 6
6 7 9
"""