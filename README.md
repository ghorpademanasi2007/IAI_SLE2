# IAI_SLE2

## SLE-2: BFS and DFS Performance Analysis

This project implements **Breadth First Search (BFS)** and **Depth First Search (DFS)** in Python. It measures **average, best and worst execution time** for three search cases and compares BFS and DFS using the same graph.

`py-spy` is used separately to generate SVG flame-graph profiles of the Python programs.

## Files

| File | Purpose |
|---|---|
| `BFS.py` | BFS implementation and timing analysis |
| `DFS.py` | DFS implementation and timing analysis |
| `BFS_DFS_Comparison.py` | Combined BFS vs DFS comparison table |
| `graph.dot` | Graph in Graphviz DOT format |
| `CONTRIBUTION_LOG.md` | Contribution history |

## Graph

The same graph is used by both algorithms so the comparison is consistent.

```text
                 A
               /   \
              B     C
             / \     \
            D   E     F
             \ /     /
              G-----
```

### Adjacency list

```text
A -> B, C
B -> D, E
C -> F
D -> G
E -> G
F -> G
G -> none
```

## Search Cases

The start node is `A`.

| Case | Target | Description |
|---|---|---|
| Best | `A` | Target is the starting node, so only one node is expanded. |
| Average | `E` | Target is reached after partial exploration. |
| Worst | `Z` | Target is absent, so every reachable node is explored. |

For an adjacency-list graph, a full BFS or DFS traversal is **O(V + E)**. The best-case search can be **O(1)** when the target is the starting node. The selected average case is an experimental example, so its measured time depends on the computer and implementation.

## Timing Method

Each search case is executed **10,000 times** using Python's `time.perf_counter()`.

The programs calculate:

- **Average time:** mean of all measured runs.
- **Best time:** minimum measured run time.
- **Worst time:** maximum measured run time.
- **Nodes expanded:** number of nodes examined by the search.
- **Path:** path found by BFS or DFS, if the target exists.

The millisecond values are intentionally calculated at runtime and are not hard-coded because execution time varies by computer.

## Run BFS

```bash
python BFS.py
```

BFS prints the path, nodes expanded, average time, best time and worst time for Best, Average and Worst cases.

## Run DFS

```bash
python DFS.py
```

DFS prints the same measurements using the same graph and targets.

## BFS vs DFS Comparison Table

Run:

```bash
python BFS_DFS_Comparison.py
```

The program produces a table in this format:

```text
====================================================================================================
                         BFS vs DFS PERFORMANCE COMPARISON
====================================================================================================
COMPARISON TABLE
----------------------------------------------------------------------------------------------------
Case      Algorithm   Target   Average(ms)    Best(ms)       Worst(ms)      Nodes
----------------------------------------------------------------------------------------------------
Best      BFS         A        actual value   actual value   actual value   1
Best      DFS         A        actual value   actual value   actual value   1
Average   BFS         E        actual value   actual value   actual value   ...
Average   DFS         E        actual value   actual value   actual value   ...
Worst     BFS         Z        actual value   actual value   actual value   7
Worst     DFS         Z        actual value   actual value   actual value   7
----------------------------------------------------------------------------------------------------
```

Do not copy the words `actual value` into the report. Your computer will print the numerical values when you run the program.

## py-spy Profiling

`py-spy` is a sampling profiler for Python. It creates a profile of the running Python program and can save it as an SVG flame graph.

### Install py-spy

```bash
python -m pip install py-spy
```

Check installation:

```bash
py-spy --version
```

### Profile BFS

```bash
py-spy record --rate 100 -o BFS_profile.svg -- python BFS.py
```

### Profile DFS

```bash
py-spy record --rate 100 -o DFS_profile.svg -- python DFS.py
```

### Profile the comparison program

```bash
py-spy record --rate 100 -o BFS_DFS_profile.svg -- python BFS_DFS_Comparison.py
```

After the command finishes, open the generated `.svg` file in Chrome. The SVG is the actual profile produced from the student's machine.

If Git Bash cannot find `py-spy`, use:

```bash
where py-spy
```

Then run the returned executable path, for example:

```bash
"C:\path\to\py-spy.exe" record --rate 100 -o BFS_profile.svg -- python BFS.py
```

## Timing vs py-spy

These two tools have different purposes:

- `time.perf_counter()` gives the numerical average, best and worst execution times.
- `py-spy` generates the profiling/flame graph and shows where sampled execution time is spent.
- Big-O complexity is determined from algorithm analysis, not from py-spy measurements.

## Complexity Summary

| Algorithm | Best Search Case | Average/Worst Search Bound | Space |
|---|---:|---:|---:|
| BFS | O(1) | O(V + E) | O(V) |
| DFS | O(1) | O(V + E) | O(V) |

## Learning Outcomes

- Implement BFS using a queue.
- Implement DFS using recursion.
- Measure average, best and worst execution time.
- Count expanded nodes.
- Compare BFS and DFS using a common graph.
- Generate SVG profiling graphs using py-spy.
- Distinguish measured execution time from Big-O complexity.
