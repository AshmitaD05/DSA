import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start_node):
        visited = set()
        self._dfs_recursive(start_node, visited)

    def _dfs_recursive(self, current_node, visited):
        if current_node not in visited:
            print(current_node, end=' ')
            visited.add(current_node)

            if current_node in self.graph:
                for neighbor in self.graph[current_node]:
                    self._dfs_recursive(neighbor, visited)

    def plot_graph(self):
        G = nx.DiGraph(self.graph)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold', arrowsize=20, node_size=700, node_color='skyblue')
        plt.show()

# Get input from the user to construct the graph
g = Graph()
num_edges = int(input("Enter the number of edges: "))

for _ in range(num_edges):
    u, v = map(int, input("Enter edge (u v): ").split())
    g.add_edge(u, v)

start_node = int(input("Enter the starting node for DFS:"))

# Perform DFS starting from the user-specified node
print(f"Depth-First Search starting from node {start_node}:")
g.dfs(start_node)

# Plot the directed graph using networkx and matplotlib
g.plot_graph()
