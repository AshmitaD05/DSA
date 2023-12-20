import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def floyd_warshall(graph):
    n = len(graph)
    
    # Initialize the distance matrix with the graph's adjacency matrix
    dist = np.array(graph)
    
    # Apply the Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i, k] + dist[k, j] < dist[i, j]:
                    dist[i, j] = dist[i, k] + dist[k, j]
    
    return dist

# Example usage:
# Define the graph as an adjacency matrix
# Use np.inf for unreachable or infinite distances
graph = [
    [0, 3, np.inf, 7],
    [8, 0, 2, np.inf],
    [5, np.inf, 0, 1],
    [2, np.inf, np.inf, 0]
]

# Call the Floyd-Warshall function
shortest_paths = floyd_warshall(graph)

# Display the result
print("Shortest Paths:")
print(shortest_paths)

# Create a directed graph using NetworkX
G = nx.DiGraph()
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] != np.inf:
            G.add_edge(i, j, weight=graph[i][j])

# Visualize the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", edge_color="gray", arrowsize=20)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
