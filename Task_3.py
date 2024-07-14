import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, u, v, weight):
        if u not in self.vertices:
            self.vertices[u] = []
        if v not in self.vertices:
            self.vertices[v] = []
        self.vertices[u].append((v, weight))
        self.vertices[v].append((u, weight))  # If the graph is undirected

def dijkstra(graph, start):
    # Initialize distances and priority queue
    distances = {vertex: float('inf') for vertex in graph.vertices}
    distances[start] = 0
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)
    visited = set()
    parents = {vertex: None for vertex in graph.vertices}  # To track the path

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph.vertices[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, parents

def visualize_graph(graph, start, distances, parents):
    G = nx.Graph()

    # Add edges
    for u in graph.vertices:
        for v, weight in graph.vertices[u]:
            G.add_edge(u, v, weight=weight)

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=15, font_weight='bold', edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Highlight the shortest paths
    for end_vertex, distance in distances.items():
        if end_vertex != start:
            path = []
            current = end_vertex
            while current:
                path.append(current)
                current = parents[current]
            path = path[::-1]
            nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i + 1]) for i in range(len(path) - 1)], width=3, edge_color='r')

    plt.title(f"Shortest paths from {start}")
    plt.show()

# Example usage
g = Graph()
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'C', 2)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 1)

start_vertex = 'A'
distances, parents = dijkstra(g, start_vertex)

print(f"Distances from start vertex {start_vertex}:")
for vertex, distance in distances.items():
    print(f"Vertex {vertex}: {distance}")

visualize_graph(g, start_vertex, distances, parents)
