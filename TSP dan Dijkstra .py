import networkx as nx
import time

def tsp(graph, start):
    num_vertices = len(graph)
    vertices = list(graph.nodes)
    path = [start]
    visited = {start}

    def backtrack(curr_vertex):
        if len(path) == num_vertices:
            return path + [start]

        min_cost = float('inf')
        min_path = None

        for neighbor in graph.neighbors(curr_vertex):
            if neighbor not in visited:
                path.append(neighbor)
                visited.add(neighbor)
                new_path = backtrack(neighbor)
                path.pop()
                visited.remove(neighbor)

                cost = graph[curr_vertex][neighbor]['weight']
                if new_path is not None and cost < min_cost:
                    min_cost = cost
                    min_path = new_path

        return min_path

    start_time = time.time()
    shortest_path = backtrack(start)
    end_time = time.time()
    execution_time = end_time - start_time

    return shortest_path, execution_time

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    previous_vertices = {vertex: None for vertex in graph}

    unvisited_vertices = list(graph.nodes)

    start_time = time.time()

    while unvisited_vertices:
        current_vertex = min(unvisited_vertices, key=lambda vertex: distances[vertex])
        unvisited_vertices.remove(current_vertex)

        for neighbor in graph.neighbors(current_vertex):
            alternative_route = distances[current_vertex] + graph[current_vertex][neighbor]['weight']
            if alternative_route < distances[neighbor]:
                distances[neighbor] = alternative_route
                previous_vertices[neighbor] = current_vertex

    end_time = time.time()
    execution_time = end_time - start_time

    shortest_path = []
    for vertex in graph:
        if distances[vertex] != float('inf'):
            shortest_path.append(vertex)

    return shortest_path, execution_time

def print_results(shortest_path, execution_time):
    print("Iterasi:")
    for i, vertex in enumerate(shortest_path):
        print(f"Iterasi {i + 1}: {vertex}")
    print(f"\nHasil akhir (Shortest path): {' -> '.join(shortest_path)}")
    print(f"Waktu komputasi: {execution_time:.6f} detik")

def main():
    graph = nx.Graph()
    graph.add_edge('A', 'B', weight=12)
    graph.add_edge('A', 'C', weight=10)
    graph.add_edge('A', 'G', weight=12)
    graph.add_edge('B', 'C', weight=8)
    graph.add_edge('B', 'D', weight=12)
    graph.add_edge('C', 'D', weight=11)
    graph.add_edge('C', 'E', weight=3)
    graph.add_edge('C', 'G', weight=9)
    graph.add_edge('D', 'E', weight=11)
    graph.add_edge('D', 'F', weight=10)
    graph.add_edge('E', 'F', weight=6)
    graph.add_edge('E', 'G', weight=7)
    graph.add_edge('F', 'G', weight=9)

    while True:
        print("Pilih algoritma:")
        print("1. TSP")
        print("2. Dijkstra")
        algorithm_choice = input("Masukkan pilihan algoritma (1/2): ")

        if algorithm_choice == '1':
            shortest_path, execution_time = tsp(graph, 'A')
        elif algorithm_choice == '2':
            shortest_path, execution_time = dijkstra(graph, 'A')
        else:
            print("Pilihan algoritma tidak valid.")
            continue

        print_results(shortest_path, execution_time)

        continue_choice = input("Apakah Anda ingin melanjutkan program? (y/n): ")
        if continue_choice.lower() != 'y':
            break

if __name__ == '__main__':
    main()