"""
Algorytm Edmondsa-Karpa. Maksymalny przepływ w sieci.
"""

from queue import Queue

class Graph:
    """Klasa reprezentująca graf"""

    def __init__(self):
        self.source = None  # Źródło sieci
        self.outlet = None  # Ujście sieci
        self.N = 0  # Ilość wierzchołków
        self.fathers = []  # Lista ojców
        self.neighborhood_list = {}  # Lista sąsiedztwa
        self.queue = Queue()  # Kolejka do bfs
        self.CFP = []  # Lista wartości najmniejszych przepustowości rezydualnych danego kanału

    def read_graph(self):
        """Wczytanie grafu"""

        # Wczytanie ilości wierzchołków i krawędzi
        vertices_and_edges = input("Podaj ilość wierzchołków i krawędzi [n m]: ")
        n, m = vertices_and_edges.split(" ")
        n = int(n)
        m = int(m)

        self.N = n

        for i in range(n):
            self.neighborhood_list[i] = []

        # Wczytanie krawędzi
        print("Podaj krawędzie [v1 v2 przepustowość]: ")
        for i in range(m):
            edge = input()
            v1, v2, capacity = edge.split(" ")
            # v1 -> (v2, przepustowość, przepływ)
            self.neighborhood_list[int(v1)].append([int(v2), int(capacity), 0])
        
        # Ustawienie źródła i ujścia sieci
        source_and_outlet = input("Podaj źródło i ujście [źródło ujście]: ")
        v1, v2 = source_and_outlet.split(" ")
        self.source = int(v1)
        self.outlet = int(v2)
    
    def print_graph(self):
        print(self.neighborhood_list)

    def edmonds_karp(self):
        fmax = 0  # Maksymalny przepływ
        # Tworzenie sieci rezydualnej od s do t
        for i in range(self.N):
            for j in self.neighborhood_list[i]:
                # Czy na liście sąsiadów j jest wierzchołek i?
                # Jeśli nie - tworzymy, jeśli tak - nic nie robimy
                for k in self.neighborhood_list[j[0]]:
                    if k[0] == i:
                        continue
                # Dodanie pustej krawędzi
                self.neighborhood_list[j[0]].append([i, 0, 0])

        # Wyznaczanie maksymalnych przepływów w sieci  
        while True:
            # Czyszczenie i inicjalizacja listy ojców i najmniejszych przepustowości rezydualnych
            self.fathers.clear()
            self.CFP.clear()
            for i in range(self.N):
                self.fathers.append(-1)
                self.CFP.append(0)
            
            # Przepustowość źródła jest nieskończona
            self.CFP[self.source] = 1000000

            # Czyszczenie kolejki i wrzucenie do niej źródła
            while not self.queue.empty():
                self.queue.get()
            self.queue.put(self.source)

            # Szukanie ścieżki w sieci rezydualnej od źródła do ujścia
            while not self.queue.empty():
                path_exists = False  # Zakładamy brak ścieżki
                i = self.queue.get()
                for j in self.neighborhood_list[i]:
                    cp = j[1] - j[2]  # Przepustowość rezydualna kanału
                    # Przetwarzane są tylko istniejące i nieodwiedzone jeszcze krawędzie
                    if cp != 0 and self.fathers[j[0]] == -1:
                        self.fathers[j[0]] = i  # Poprzednik
                        # Przepustowość rezydualna do węzła j[0]
                        if cp < self.CFP[i]:
                            self.CFP[j[0]] = cp
                        else:
                            self.CFP[j[0]] = self.CFP[i]
                        # Czy ścieżka dotarła do ujścia?
                        if j[0] == self.outlet:
                            path_exists = True  # Dotarła, mamy ścieżkę
                            break
                        else:
                            self.queue.put(j[0])  # Nie dotarła, dorzucamy do kolejki węzęł j[0]
                if path_exists: break  # Ścieżka znaleziona - koniec
            if not path_exists: break  # Ścieżka nieznaleziona - koniec

            # Zwiększenie przepływu sieciowego
            fmax += self.CFP[self.outlet]

            # Cofanie po ścieżce od ujścia do źródła
            v = self.outlet
            while v != self.source:
                i = self.fathers[v]  # Poprzednik
                # Szukamy na liście sąsiadów i krawędzi prowadzącej do v
                for k in self.neighborhood_list[i]:
                    if k[0] == v:
                        k[2] += self.CFP[self.outlet]  # Kierunek zgodny - zwiększamy przepływ
                        break
                # Szukamy na liście sąsiadów v krawędzi prowadzącej do i
                for z in self.neighborhood_list[v]:
                    if k[0] == i:
                        k[2] -= self.CFP[self.outlet]  # Kierunek przeciwny - zmniejszamy przepływ
                        break
                v = i  # Cofamy się dalej

        print("Przepływ maksymalny = {}".format(fmax))


if __name__ == "__main__":

    # Stworzenie grafu
    g = Graph()
    # Wczytanie grafu
    g.read_graph()
    # Obliczenie maksymalnego przepływu sieci
    g.edmonds_karp()


# Przykładowe dane
"""
7 11
0 1 7
0 3 3
1 3 4
1 4 6
2 0 9
2 5 9
3 4 9
3 6 2
5 3 3
5 6 6
6 4 8
2 4
"""