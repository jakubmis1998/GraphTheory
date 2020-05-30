"""
Dany jest digraf D, dwa jego wierzchołki v i u oraz liczba naturalna k.
Program znajduje liczbę wszystkich marszrut długości k, łączących te wierzchołki.
"""

class Graph:
    def __init__(self):
        self.matrix = [] # macierz sąsiedztwa

    def read_graph(self):
        """Wczytanie grafu"""

        # Wczytanie ilości wierzchołków i krawędzi
        vertices_and_edges = input("Podaj ilość wierzchołków i krawędzi [n m]: ")
        n, m = vertices_and_edges.split(" ")
        n = int(n)
        m = int(m)

        # Inicjalizacja macierzy sąsiedztwa zerami
        self.matrix = [[0 for i in range(n)] for j in range(n)]

        # Wczytanie krawędzi
        print("Podaj krawędzie [v1 v2]: ")
        for i in range(m):
            edge = input()
            v1, v2 = edge.split(" ")
            self.matrix[int(v1)][int(v2)] = 1

    def print_matrix(self, matrix):
        """Metoda wypisująca macierz w formie prostokątnej"""

        print("Macierz z liczbą marszrut długości k")
        for row in matrix:
            print(' '.join([str(elem) for elem in row]))

    def matrix_multiplication(self, A, B):
        """Metoda zwraca iloczyn macierzy A i B"""

        n = len(A)
        result = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                for m in range(n):
                    result[i][j] += A[i][m] * B[m][j]
        return result

    def matrix_exponentation(self, k):
        """Metoda zwraca macierz sąsiedztwa do potęgi k"""

        result = self.matrix
        for i in range(1, k):
            result = self.matrix_multiplication(result, self.matrix)
        return result

    def routes(self):
        """Metoda znajduje liczbę wszystkich marszrut długości k"""
        
        k = int(input("Podaj k: "))
        vertices = input("Podaj wierzchołki u, v [u v]: ")
        u, v = vertices.split(" ")
        matrix = self.matrix_exponentation(k)
        self.print_matrix(matrix)
        return [k, u, v, matrix[int(u)][int(v)]]


if __name__ == "__main__":
    g = Graph()
    g.read_graph()
    results = g.routes()
    print("Liczba marszrut długości {} z wierzchołka {} do {} = {}".format(
        results[0], results[1], results[2], results[3]
    ))

"""
Przykładowy digraf
12 19
0 1
0 4
0 6
1 4
1 5
2 1
3 6
3 7
3 11
4 8
5 4
5 8
5 10
5 11
6 2
6 7
6 11
8 9
10 11
"""