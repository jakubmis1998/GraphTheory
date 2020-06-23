"""
Algorytm kolorowania wierzchołków badający dwudzielność grafu.
"""

from queue import Queue

class Graph:
    def __init__(self):
        self.neighbours_list = {} # lista sąsiedztwa
        self.visited = [] # lista odwiedzonych wierzchołków
        self.queue = Queue() # kolejka do bfs

    def init_visited(self):
        """Funkcja inicjalizująca listę odwiedzonych wierzchołków"""
        self.visited.clear()
        for i in range(len(self.neighbours_list)):
            self.visited.append(False)

    def read_graph(self):
        """Funkcja do wczytywania ilości wierzchołków i krawędzi grafu"""

        # Wczytanie ilości wierzchołków i krawędzi
        vertices_and_edges = input("Podaj ilość wierzchołków i krawędzi [n m]: ")
        n, m = vertices_and_edges.split(" ")
        n = int(n)
        m = int(m)

        for i in range(n):
            self.neighbours_list[i] = []
        self.init_visited()

        # Wczytanie krawędzi
        print("Podaj krawędzie [v1 v2]: ")
        for i in range(m):
            edge = input()
            v1, v2 = edge.split(" ")
            self.neighbours_list[int(v1)].append(int(v2))
            self.neighbours_list[int(v2)].append(int(v1))

    def print_graph(self):
        """Funkcja do wyświetlania grafu"""
        for i in self.neighbours_list:
            print("{}: {}".format(i, self.neighbours_list[i]))

    def vertices_painting(self, start_v):
        """BFS + kolorowanie wierzchołków"""

        self.queue.put(start_v)
        self.visited[start_v] = True

        while not self.queue.empty():
            u = self.queue.get()
            for v in self.neighbours_list[u]:
                if not self.visited[v]:
                    self.visited[v] = not self.visited[u]
                    self.queue.put(v)
                elif self.visited[v] == self.visited[u]:
                    return "Graf nie jest dwudzielny!"

        return "Graf jest dwudzielny!"


if __name__ == "__main__":
    g = Graph()
    g.read_graph()
    print(g.vertices_painting(0))

"""
Dwudzielny
17 23
0 2
0 3
1 2
1 14
2 6
3 4
3 6
3 13
4 7
4 12
5 6
5 9
5 10
6 7
6 8
6 12
7 13
8 9
10 11
10 14
10 15
11 16
12 16

Niedwudzielny
17 24
0 2
0 3
1 2
1 14
2 6
3 4
3 6
3 13
4 7
4 12
5 6
5 9
5 10
6 7
6 8
6 12
7 13
8 9
10 11
10 14
10 15
11 16
12 16
13 16
"""