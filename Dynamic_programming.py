import networkx as nx
import matplotlib.pyplot as plt

class BellmanFordGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, src, dest, weight):
        self.graph.append((src, dest, weight))

def draw_graph(graph):
    G = nx.DiGraph()

    for edge in graph:
        src, dest, weight = edge
        G.add_edge(src, dest, weight=weight)

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    nx.draw_networkx_nodes(G, pos, node_color='lightblue')
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)

    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.axis('off')
    plt.show()

def MainBellmanFord(vertices, graph):
    g = BellmanFordGraph(vertices)

    for edge in graph:
        src, dest, weight = edge
        g.addEdge(src, dest, weight)

    def BellmanFord(src):
        dist = [float("Inf")] * g.V
        dist[src] = 0

        for _ in range(g.V - 1):
            for u, v, w in g.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in g.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                return "Graph contains a negative weight cycle"

        return dist

    return BellmanFord(0)

def show_graph(graph):
    vertices = 5
    g = BellmanFordGraph(vertices)
    for edge in graph:
        src, dest, weight = edge
        g.addEdge(src, dest, weight)
    draw_graph(g.graph)

# Example usage:
graph_example = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3)
]

result_distances = MainBellmanFord(5, graph_example)
print("Result Distances:", result_distances)

show_graph(graph_example)
