import heapq   
import networkx as nx   
import matplotlib.pyplot as plt   
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        if current_vertex not in graph:
            print(f"Vertex {current_vertex} is not in the graph. Skipping.")
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def input_graph():
    graph = {}   
    vertices = input("Enter the vertices (comma-separated): ").split(',')   
    
    for vertex in vertices:
        graph[vertex] = {}   
        
    for vertex in graph:
        neighbors_str = input(f"Enter neighbors and distances for vertex {vertex} (neighbor1,distance1,neighbor2,distance2,...): ")
        neighbors_list = neighbors_str.split(',')   # Input neighbors and distances for each vertex
        
        print(f"neighbors_list for vertex {vertex}: {neighbors_list}")  
        for i in range(0, len(neighbors_list), 2):
            if i + 1 < len(neighbors_list):  
                neighbor, distance = neighbors_list[i], float(neighbors_list[i + 1])
                graph[vertex][neighbor] = distance   # Add neighbors and distances to the graph
            else:
                print(f"Illegal format for neighbors and distances for vertex {vertex}. Skipping.")
    
    return graph   
def visualize_graph(graph):
    G = nx.Graph()   
    
    for vertex, neighbors in graph.items():
        for neighbor, distance in neighbors.items():
            G.add_edge(vertex, neighbor, weight=distance)   
    
    pos = nx.spring_layout(G)   
    labels = nx.get_edge_attributes(G, 'weight')   
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10)   
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)   # Label the edges
    
    plt.axis('off')   
    plt.show()  
if __name__ == "__main__":
    graph = input_graph()   # Get user input for the graph
    start_vertex = input("Enter the starting vertex: ")   
    shortest_distances = dijkstra(graph, start_vertex)   
    
    for vertex, distance in shortest_distances.items():
        print(f'Shortest distance from {start_vertex} to {vertex} is {distance}')   
    visualize_graph(graph)   
