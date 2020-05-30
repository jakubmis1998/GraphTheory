"""
Program wyznacza najkrótszą drogę pomiędzy wprowadzanymi wierzchołkami v i u.
"""

from queue import Queue

def init_visited(visited):
    for i in range(len(graph)):
        visited.append(False)

def init_fathers(fathers):
    for i in range(len(graph)):
        fathers.append(-1)

def bfs(graph, start_v):
    q.put(start_v)
    visited[start_v] = True

    while not q.empty():
        v = q.get()
        for neighboor in graph[v]:
            if not visited[neighboor]:
                q.put(neighboor)
                visited[neighboor] = True
                fathers[neighboor] = v

def find_shortest_way(fathers, start_v, end_v):
    x = end_v
    way = []
    while x != start_v:
        if (x == -1):
            print("Taka droga nie istnieje!")
            return
        way.append(x)
        x = fathers[x]
    way.append(start_v)
    print("Najkrótsza droga od {} do {}: {}".format(start_v, end_v, way[::-1]))

if __name__ == "__main__":
    graph = {}
    graph[0] = [1, 2, 10]
    graph[1] = [0, 2, 5, 6, 15]
    graph[2] = [0, 1, 4, 13]
    graph[3] = [12]
    graph[4] = [2, 11, 13]
    graph[5] = [1, 6, 8, 9]
    graph[6] = [1, 5, 15]
    graph[7] = []
    graph[8] = [5, 9]
    graph[9] = [5, 8]
    graph[10] = [0]
    graph[11] = [4, 13]
    graph[12] = [3]
    graph[13] = [14]
    graph[14] = [13]
    graph[15] = [1, 6]

    visited = []
    fathers = []
    q = Queue()

    init_visited(visited)
    init_fathers(fathers)

    start_v = int(input("Wierzchołek startowy: "))
    end_v = int(input("Wierzchołek końcowy: "))
    try:
        if start_v > len(graph) or end_v > len(graph):
            raise IndexError
        bfs(graph, start_v)
        find_shortest_way(fathers, start_v, end_v)
    except IndexError:
        print("Taki wierzchołek nie istnieje!")
