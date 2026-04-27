# Graph structure: Adjacency list with weights
# graph[node] = {neighbor: weight, ...}
graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'B': 2, 'C': 5, 'G': 12},
    'B': {'C': 2},
    'C': {'G': 3},
    'G': {}
}

# Heuristic values for each node (e.g., straight-line distance to goal 'G')
heuristics = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 1,
    'G': 0
}

def print_graph_info(graph, heuristics):
    print("Graph Edges and Weights:")
    for node, edges in graph.items():
        if not edges:
            print(f"  {node} has no outgoing edges.")
        for neighbor, weight in edges.items():
            print(f"  {node} -> {neighbor} (weight: {weight})")
            
    print("\nHeuristic Values:")
    for node, h_val in heuristics.items():
        print(f"  h({node}) = {h_val}")

if __name__ == "__main__":
    print_graph_info(graph, heuristics)
