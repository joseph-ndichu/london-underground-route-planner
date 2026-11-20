# London Underground Route Planner

A Python program that finds the **fastest route** between any two London Underground stations. It shows:

1. The list of stations on the route, in order.
2. The total journey time in minutes.

---

## The idea

Think of the tube map as **dots and lines**:

- Each **station** is a dot.
- Each **connection** between two stations is a line.
- Each line has a **number**: the minutes it takes to travel it.

To find the fastest route, the program uses **Dijkstra's algorithm**. It starts at your station and always moves on to the **closest station it has not finished yet**, keeping a note of the quickest time to reach every station. When it reaches your destination, that time is the fastest one.

---

## What is in this project

| File | What it does |
|---|---|
| `task2a.py` | Finds the fastest route on a small, made-up map with 5 stations (A to E). |
| `generate_data.py` | Makes random tube-like maps of any size, where every station can be reached. |
| `time_measurement.py` | Times how long a route search takes on maps of different sizes. |
| `plot_results.py` | Draws a graph of those times. |
| `task2b.py` | Finds the fastest route on the **real** London Underground map. |
| `London Underground data.csv` | The real tube data: stations, connections and minutes. |
| `clrsPython/` | The library used for the map and Dijkstra's algorithm (not changed). |

---

## Part 1: A small test map (`task2a.py`)

A tiny map with 5 stations was solved **by hand** first, and then by the program.

Fastest route from A to D:

```
A -> B -> E -> D | 14 minutes
```

The hand answer and the program's answer were the **same**.

---

## Part 2: How fast is it? (`generate_data.py`, `time_measurement.py`, `plot_results.py`)

**Making test maps.** `generate_data.py` first joins every station into one connected tree, so you can always get from any station to any other. Then it adds a few extra random connections, like the real tube. Each connection gets a random time from 1 to 10 minutes.

**Timing.** For each map size, the program picks **100 random pairs** of stations, finds the fastest route for each pair, and works out the average time.

| Number of stations | Average time per search |
|---|---|
| 100 | 0.78 ms |
| 1,000 | 10.6 ms |
| 10,000 | 147 ms |
| 100,000 | 1.89 seconds |

**What this shows.** When the map gets **10 times bigger**, the search takes **a little more than 10 times longer**. This matches the theory for Dijkstra's algorithm, which says the time grows at about *n log n*.

**The biggest map tested** had 100,000 stations. Bigger maps were not tested because they would take too long to run.

---

## Part 3: The real tube map (`task2b.py`)

The program reads the real data and cleans it first:

- It skips rows that only name a station and have no time.
- It removes extra spaces from station names.
- If the same two stations are joined on more than one tube line, it keeps **one** connection with the **fastest** time.

The final map has **270 stations** and **311 connections**.

**Results:**

```
From: Covent Garden
To  : Leicester Square
Total journey time: 1 minutes

From: Wimbledon
To  : Stratford
Fastest route: Wimbledon -> Wimbledon Park -> ... -> Mile End -> Stratford
Total journey time: 50 minutes
```

---

## How to run it

You need **Python 3**. The plotting file also needs **matplotlib** and **numpy**:

```bash
pip install matplotlib numpy
```

Then run any file from inside this folder, for example:

```bash
python3 task2a.py
python3 task2b.py
python3 generate_data.py
python3 time_measurement.py
python3 plot_results.py
```

Note: `time_measurement.py` can take a long time, because it tests maps up to 100,000 stations.

---

## Sources

- **clrsPython**: the code library for the book *Introduction to Algorithms* (4th edition), by Cormen et al.
- **Stack Overflow**: methods used for making random connected maps, timing, plotting and reading CSV files.
- **London Underground data**: journey times in minutes between neighbouring stations.
