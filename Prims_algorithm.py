import heapq
import networkx as nx
import matplotlib.pyplot as plt

def prim(graph):
    priority_queue = [(0, None, list(graph.keys())[0])]  # (weight, source, destination)
    visited = set()

    minimum_spanning_tree = []

    while priority_queue:
        weight, source, current_node = heapq.heappop(priority_queue)

        if current_node not in visited:
            visited.add(current_node)

            if source is not None:
                minimum_spanning_tree.append((source, current_node, weight))

            for neighbor, edge_weight in graph[current_node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (edge_weight, current_node, neighbor))

    return minimum_spanning_tree

def plot_graph(graph, minimum_spanning_tree):
    G = nx.Graph()
    
    for node, edges in graph.items():
        G.add_node(node)
        for neighbor, weight in edges:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    labels = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=8)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', label_pos=0.5)
    nx.draw_networkx_edges(G, pos, edgelist=minimum_spanning_tree, edge_color='red', width=2)
    plt.show()

# Get graph input from the user
graph = {}
num_vertices = int(input("Enter the number of vertices: "))

for _ in range(num_vertices):
    vertex = input("Enter a vertex: ")
    edges = input(f"Enter the edges for {vertex} in the format (neighbor, weight) separated by commas: ")
    edges_list = [tuple(map(str.strip, edge.split(','))) for edge in edges.split()]
    graph[vertex] = edges_list

minimum_spanning_tree = prim(graph)
print("Minimum Spanning Tree:", minimum_spanning_tree)

plot_graph(graph, minimum_spanning_tree)
