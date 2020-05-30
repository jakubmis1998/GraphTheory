"""
Program wyznacza najdłuższą ścieżkę drzewa i wierzchołek/ki centralne.
"""

from queue import Queue

class Tree:
    def __init__(self):
        self.tree = {} # lista sąsiedztwa
        self.visited = [] # lista odwiedzonych wierzchołków
        self.fathers = [] # lista ojców
        self.vertices_degrees = [] # lista stopni wierzchołków
        self.vertices_labels = [] # lista etykiet wierzchołków
        self.queue = Queue() # kolejka do bfs

    def read_tree(self):
        """Funkcja do wczytywania ilości wierzchołków drzewa i jego krawędzi"""
        vertices_count = int(input("Liczba wierzchołków drzewa: "))
        for i in range(vertices_count):
            self.tree[i] = []
            self.vertices_degrees.append(0)
        self.init_fathers()
        self.init_labels()
        self.init_visited()
        
        print("Zdefiniuj krawędzie drzewa: ")
        for i in range(vertices_count-1):
            edge = input()
            v1, v2 = edge.split(" ")
            self.tree[int(v1)].append(int(v2))
            self.vertices_degrees[int(v1)] += 1
            self.tree[int(v2)].append(int(v1))
            self.vertices_degrees[int(v2)] += 1

    def print_tree(self):
        """Funkcja do wyświetlania drzewa"""
        for i in self.tree:
            print("{}: {}".format(i, self.tree[i]))

    def init_visited(self):
        """Funkcja inicjalizująca listę odwiedzonych wierzchołków"""
        self.visited.clear()
        for i in range(len(self.tree)):
            self.visited.append(0)

    def init_fathers(self):
        """Funkcja inicjalizująca listę ojców wierzchołków"""
        self.fathers.clear()
        for i in range(len(self.tree)):
            self.fathers.append(-1)

    def init_labels(self):
        """Funkcja inicjalizująca listę etykiet wierzchołków"""
        self.vertices_labels.clear()
        for i in range(len(self.tree)):
            self.vertices_labels.append(0)

    def bfs(self, start_v):
        """BFS + nadawanie etykiet"""
        self.queue.put(start_v)
        self.visited[start_v] = True
        self.vertices_labels[start_v] = path_length = 0

        while not self.queue.empty():
            v = self.queue.get()
            for neighboor in self.tree[v]:
                if not self.visited[neighboor]:
                    self.queue.put(neighboor)
                    self.visited[neighboor] = True
                    self.fathers[neighboor] = v
                    self.vertices_labels[neighboor] = self.vertices_labels[self.fathers[neighboor]]+1

    def find_longest_path(self):
        """Funkcja znajdująca najdłuższą ścieżkę drzewa i wierzchołki centralne"""
        any_leaf = self.vertices_degrees.index(1)
        self.bfs(any_leaf)
        vertex_with_the_biggest_label = self.vertices_labels.index(max(self.vertices_labels))
        self.init_fathers()
        self.init_labels()
        self.init_visited()
        self.bfs(vertex_with_the_biggest_label)

        i = self.vertices_labels.index(max(self.vertices_labels))
        path = [i]
        while self.fathers[i] != -1:
            i = self.fathers[i]
            path.append(i)

        print("Najdłuższa ścieżka w drzewie: {}".format(path))
        if len(path) % 2 == 0:
            print("Wierzchołki centralne: {}, {}".format(
                path[len(path // 2)],
                path[len(path // 2 - 1)]
            ))
        else:
            print("Wierzchołek centralny: {}".format(
                path[len(path) // 2]
            ))


if __name__ == "__main__":
    g = Tree()
    g.read_tree()
    g.find_longest_path()


"""
Drzewo z prezentacji, slajd 17.
16
0 2
1 2
2 5
3 4
4 5
5 6
6 7
7 8
6 9
5 10
10 11
11 12
12 13
13 14
13 15
"""
