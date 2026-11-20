import sys, os

# Library folders (clrsPython is used unmodified).
LIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "clrsPython")
for folder in ("Utility functions", "Chapter 6", "Chapter 10", "Chapter 20", "Chapter 22"):
    sys.path.append(os.path.join(LIB, folder))

from adjacency_list_graph import AdjacencyListGraph   # Utility functions/adjacency_list_graph.py
from dijkstra import dijkstra                          # Chapter 22/dijkstra.py
from print_path import print_path                      # Chapter 20/print_path.py

# Dataset (same as the manual trace)
stations = ["A", "B", "C", "D", "E"]                   # vertex numbers 0..4
connections = [("A", "B", 4), ("B", "C", 5), ("B", "E", 3),
               ("C", "D", 8), ("E", "C", 6), ("E", "D", 7)]

# Undirected, weighted graph: library stores each connection in both directions.
graph = AdjacencyListGraph(len(stations), directed=False, weighted=True)
for u, v, minutes in connections:
    graph.insert_edge(stations.index(u), stations.index(v), minutes)

# Search for the same pair as the manual trace
start, destination = "A", "D"
d, pi = dijkstra(graph, stations.index(start))
route = print_path(pi, stations.index(start), stations.index(destination), lambda i: stations[i])
total = d[stations.index(destination)]

print("Final distances and predecessors from", start)
for i, name in enumerate(stations):
    pred = "-" if pi[i] is None else stations[pi[i]]
    print(f"  {name}: {d[i]} minutes, predecessor {pred}")
print()
print(f"Fastest route from {start} to {destination}: {' -> '.join(route)}")
print(f"Total journey time: {total} minutes")

# Verification against the manual computation
manual_route = ["A", "B", "E", "D"]
manual_total = 14
print()
print("Manual route :", " -> ".join(manual_route), "|", manual_total, "minutes")
print("Code route   :", " -> ".join(route), "|", total, "minutes")
print("Identical    :", route == manual_route and total == manual_total)
