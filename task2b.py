import csv
import os
import sys

# Tell Python where to find the library files
FOLDER = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(FOLDER, "clrsPython")
for folder in ("Utility functions", "Chapter 6", "Chapter 10", "Chapter 20", "Chapter 22"):
    sys.path.append(os.path.join(LIB, folder))

# Load the graph, Dijkstra & path functions
from adjacency_list_graph import AdjacencyListGraph
from dijkstra import dijkstra
from print_path import print_path

# Read data
with open(os.path.join(FOLDER, "London Underground data.csv"), newline="", encoding="utf-8-sig") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    data_read = [row for row in reader]

# Clean data
lines = {}
for row in data_read:
    if row[3] == "":
        continue
    a = row[1].strip() 
    b = row[2].strip()
    minutes = int(row[3])
    pair = tuple(sorted((a, b)))
    if pair not in lines or minutes < lines[pair]:
        lines[pair] = minutes

# Give each station a number
stations = sorted(set(name for pair in lines for name in pair))
number = {name: i for i, name in enumerate(stations)}

# Build the network
graph = AdjacencyListGraph(len(stations), directed=False, weighted=True)
for (a, b), minutes in lines.items():
    graph.insert_edge(number[a], number[b], minutes)

print("Stations:", graph.get_card_V(), "| Lines:", graph.get_card_E())

# Find & print fastest route
def find_route(start, destination):
    d, pi = dijkstra(graph, number[start])
    route = print_path(pi, number[start], number[destination], lambda i: stations[i])
    print()
    print("From:", start)
    print("To  :", destination)
    print("Fastest route:", " -> ".join(route))
    print("Total journey time:", d[number[destination]], "minutes")

# Short & long journey tests
find_route("Covent Garden", "Leicester Square")
find_route("Wimbledon", "Stratford")
