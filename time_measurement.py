import csv
import random
import sys

# Add Python's timer
from timeit import default_timer as timer

# generate_data for the connected network.
from generate_data import generate_data

#import dijkstra library and print path
from dijkstra import dijkstra
from print_path import print_path

# Raised the limit from Python’s default (1000) to 100000 (our nested network).
sys.setrecursionlimit(100000)

# 100 random pairs.
PAIRS = 100


def average_search_time(n, pairs=PAIRS):
    graph = generate_data(n, n // 6)
    total = 0.0
    for _ in range(pairs):
        start = random.randrange(n)
        destination = random.randrange(n)

        t0 = timer()
        d, pi = dijkstra(graph, start)
        route = print_path(pi, start, destination, lambda i: i)
        t1 = timer()

        total += t1 - t0
    return total / pairs


if __name__ == "__main__":
    random.seed(1)

    # Network sizes
    sizes = list(range(100, 1001, 100)) + list(range(2000, 10001, 
    1000)) + list(range(20000, 100001, 10000))

    results = []
    print(f"{'n':>8} | {'average time (ms)':>18}")
    print("-" * 30)
    for n in sizes:
        avg = average_search_time(n)
        results.append((n, avg))
        print(f"{n:>8} | {avg * 1000:>18.3f}")

    with open("timing_results (100-100000).csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "average_seconds"])
        writer.writerows(results)
    print("\nSaved to timing_results (100-100000).csv")

