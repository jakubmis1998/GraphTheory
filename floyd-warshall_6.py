"""
Program znajduje wagi najkrótszych ścieżek pomiędzy wszystkimi parami wierzchołków grafu ważonego.
tutorial przykładowy: http://algorytmy.ency.pl/tutorial/algorytm_floyda_warshalla
"""

INF = 1000

class Graph:
    def __init__(self):
        self.matrix_weight = [] # macierz wag

    def read_graph(self):
        """Wczytanie grafu"""

        # Wczytanie ilości wierzchołków i krawędzi
        vertices_and_edges = input("Podaj ilość wierzchołków i krawędzi [n m]: ")
        n, m = vertices_and_edges.split(" ")
        n = int(n)
        m = int(m)

        # Wypełnienie macierzy wag wartościami INF i wstawienie w przekątne zer.
        self.matrix_weight = [[INF for i in range(n)] for j in range(n)]
        for i in range(n):
            self.matrix_weight[i][i] = 0

        # Wczytanie krawędzi
        print("Podaj krawędzie z wagami [v1 v2 weight]: ")
        for i in range(m):
            edge = input()
            v1, v2, weight = edge.split(" ")
            self.matrix_weight[int(v1)][int(v2)] = int(weight)


    def print_matrix(self, iteration):
        """Metoda wypisująca macierz w formie prostokątnej"""

        print("\nIteracja po k = {}".format(iteration))
        for row in self.matrix_weight:
            print('\t'.join([str(elem) for elem in row]))


    def floyd_warshall(self):
        """Algorytm Floyd'a-Warshall'a"""

        print("Macierze wynikowe")
        for k in range(len(self.matrix_weight)):
            for i in range(len(self.matrix_weight)):
                for j in range(len(self.matrix_weight)):
                    if self.matrix_weight[i][k] != INF and self.matrix_weight[k][j] != INF:
                        self.matrix_weight[i][j] = min(
                            self.matrix_weight[i][j],
                            self.matrix_weight[i][k] + self.matrix_weight[k][j]
                        )
            self.print_matrix(k)


if __name__ == "__main__":
    g = Graph()
    g.read_graph()
    g.floyd_warshall()

"""
Przykładowe grafy skierowane z dowolnymi wagami
5 13
0 1 5
0 2 4
0 3 8
1 0 -4
1 2 -2
1 4 5
2 3 5
2 4 2
3 0 -1
3 1 2
3 4 -1
4 2 4
4 3 2

5 7
0 1 2
0 2 4
1 2 3
1 3 3
2 3 -1
2 4 4
3 4 2
"""