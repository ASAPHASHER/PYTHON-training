import heapq
import threading
from time import sleep
from random import randint


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def add_edge(self, neighbor, weight):
        self.neighbors[neighbor] = weight

    def __lt__(self, other):
        return self.name < other.name


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        self.nodes[name] = Node(name)

    def add_edge(self, u, v, w):
        self.nodes[u].add_edge(self.nodes[v], w)
        self.nodes[v].add_edge(self.nodes[u], w)  # undirected


def heuristic(a, b):
    """Fake heuristic for demo purposes (pretend coordinates)."""
    return abs(ord(a.name[0]) - ord(b.name[0]))


def a_star(graph, start, goal):
    start, goal = graph.nodes[start], graph.nodes[goal]

    pq = []
    heapq.heappush(pq, (0, start))
    distances = {node: float('inf') for node in graph.nodes.values()}
    distances[start] = 0

    came_from = {}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            break

        for neighbor, weight in current.neighbors.items():
            new_cost = distances[current] + weight
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(pq, (priority, neighbor))
                came_from[neighbor] = current

    # reconstruct path
    path = []
    node = goal
    while node != start:
        path.append(node.name)
        node = came_from[node]
    path.append(start.name)
    return list(reversed(path)), distances[goal]


def run_search(graph, start, goal):
    sleep(randint(1, 3))  # pretend heavy work
    path, cost = a_star(graph, start, goal)
    print(f"Thread {start}->{goal}: Path = {path}, Cost = {cost}")


# Build a sample graph
g = Graph()
for n in ["A", "B", "C", "D", "E", "F"]:
    g.add_node(n)

edges = [
    ("A", "B", 3), ("A", "C", 1),
    ("B", "D", 5), ("C", "D", 2),
    ("C", "E", 4), ("D", "F", 1), ("E", "F", 2)
]

for u, v, w in edges:
    g.add_edge(u, v, w)

# Run multiple A* searches simultaneously
pairs = [("A", "F"), ("B", "E"), ("C", "F")]

threads = [
    threading.Thread(target=run_search, args=(g, s, t))
    for s, t in pairs
]

for t in threads:
    t.start()

for t in threads:
    t.join()
