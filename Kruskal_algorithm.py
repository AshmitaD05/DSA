import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
    def kruskal_algorithm(self):
        result = []
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = [i for i in range(self.V)]

        def find_set(x):
            if parent[x] == x:
                return x
            parent[x] = find_set(parent[x])
            return parent[x]

        def union_sets(x, y):
            root_x = find_set(x)
            root_y = find_set(y)
            parent[root_x] = root_y

        for edge in self.graph:
            u, v, w = edge
            if find_set(u) != find_set(v):
                result.append([u, v, w])
                union_sets(u, v)

        return result
g = Graph(6)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 3)
g.add_edge(0, 3, 2)
g.add_edge(1, 3, 20)
g.add_edge(1, 4, 10)
g.add_edge(2, 3, 4)
g.add_edge(2, 5, 8)
g.add_edge(3, 5, 15)
g.add_edge(4, 5, 6)

minimum_spanning_tree = g.kruskal_algorithm()
G = nx.Graph()
for edge in g.graph:
    G.add_edge(edge[0], edge[1], weight=edge[2])
mst_edges = [(edge[0], edge[1]) for edge in minimum_spanning_tree]
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(edge[0], edge[1]): edge[2] for edge in minimum_spanning_tree})
nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='red', width=2)
plt.title("Minimum Spanning Tree")
plt.show()
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")
-