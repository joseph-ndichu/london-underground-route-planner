import os
import random
import sys

# Tell Python where to find the library files
LIB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "clrsPython")
for folder in ("Utility functions", "Chapter 6", "Chapter 10", "Chapter 20", "Chapter 22"):
    sys.path.append(os.path.join(LIB, folder))

# Load the adjacency list graph from the library
from adjacency_list_graph import AdjacencyListGraph

def generate_data(n, extra_lines, min_minutes=1, max_minutes=10):
    m = (n - 1) + extra_lines 
    if m > n * (n - 1) // 2:
        m = n * (n - 1) // 2

    # create an empty network of n stations
    graph = AdjacencyListGraph(n, directed=False, weighted=True)

    # build a tree that connects every station.
    for i in range(1, n):
        j = random.randint(0, i - 1)
        graph.insert_edge(i, j, random.randint(min_minutes, max_minutes))

    # add extra random lines, skipping repeats and same-station pairs.
    while graph.get_card_E() < m:
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        if a != b and not graph.has_edge(a, b):
            graph.insert_edge(a, b, random.randint(min_minutes, max_minutes))

    return graph


if __name__ == "__main__":
    random.seed(1) # build and print a small network.
    g = generate_data(6, 2)
    print("Stations:", g.get_card_V(), "| Lines:", g.get_card_E())
    print("Each station: neighbour (minutes)")
    print(g)
