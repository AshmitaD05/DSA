import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_edge(self, u, v):
        self.graph.add_edge(u, v)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        traversal_order = []

        while queue:
            current_node = queue.pop(0)
            traversal_order.append(current_node)

            for neighbor in self.graph.neighbors(current_node):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return traversal_order

# Input edges from the user
graph = Graph()
num_edges = int(input("Enter the number of edges: "))

for _ in range(num_edges):
    u, v = map(int, input("Enter edge (u v): ").split())
    graph.add_edge(u, v)

# Perform BFS on the graph
start_node = int(input("Enter the starting node for BFS: "))
bfs_order = graph.bfs(start_node)

# Print the BFS traversal order
print("BFS Traversal Order:", bfs_order)

# Plotting the graph using NetworkX and Matplotlib

pos = nx.spring_layout(graph.graph)
nx.draw(graph.graph, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", arrowsize=20)

plt.title("Directed Graph")
plt.show()
