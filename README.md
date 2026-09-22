# IAI_SLE2

## SLE-2: BFS and DFS Performance Analysis

This project implements **Breadth First Search (BFS)** and **Depth First Search (DFS)** in Python. It demonstrates best, average and worst search cases, measured execution time, expanded nodes, graph paths, and **py-spy** profiling.

## Files

| File | Purpose |
|---|---|
| `BFS.py` | BFS search with case-wise timing and node count |
| `DFS.py` | DFS search with case-wise timing and node count |
| `BFS_DFS_Comparison.py` | Combined BFS vs DFS comparison table |
| `graph.dot` | Seven-node Graphviz/DOT graph |
| `CONTRIBUTION_LOG.md` | Contribution history |

## Graph

The experiment uses a seven-node directed graph:

```text
              A
            /   \
           B     C
         /  \     \
        D    E     F
         \   |    /
          \  |   /
             G
```

Adjacency list:

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

The programs search for a target from `A`.

| Case | Target | Description | Complexity |
|---|---|---|---|
| Best | `A` | Target is the starting node | O(1) |
| Average | `E` | Target requires partial graph exploration | O(V + E) upper bound |
| Worst | `Z` | Target does not exist; all reachable nodes are explored | O(V + E) |

For a **complete traversal**, both BFS and DFS on an adjacency-list graph are O(V + E).

## Program Output

Each program performs **1000 timing runs per case** and displays:

- Target vertex
- Search path
- Nodes expanded
- Average measured time
- Best measured time
- Worst measured time
- A final summary table

Example format:

```text
==========================================================
             BFS PERFORMANCE ANALYSIS
==========================================================
Graph nodes : A, B, C, D, E, F, G
Start node  : A
Runs/case   : 1000

BEST CASE
Target          : A
Path            : A
Nodes expanded  : 1
Average time    : <your measured value> ms
Best time       : <your measured value> ms
Worst time      : <your measured value> ms
----------------------------------------------------------

AVERAGE CASE
Target          : E
Path            : A -> B -> E
...

WORST CASE
Target          : Z
Path            : Not found
...

SUMMARY TABLE
Case        Target    Average(ms)    Best(ms)    Worst(ms)    Nodes
--------------------------------------------------------------------------
Best        A         ...            ...         ...          1
Average     E         ...            ...         ...          5
Worst       Z         ...            ...         ...          7
```

The exact timing values are intentionally **not fixed** because they depend on the computer, Python version and system load.

## Run the Programs

```bash
python BFS.py
```

```bash
python DFS.py
```

For the combined table:

```bash
python BFS_DFS_Comparison.py
```

## py-spy Profiling

`py-spy` is used to record the Python program and generate an SVG flame graph. It is a profiling tool; it does not determine Big-O complexity.

### Check installation

```bash
py-spy --version
```

If it is not recognized:

```bash
python -m pip install py-spy
```

### Profile BFS

```bash
py-spy record -o BFS_profile.svg -- python BFS.py
```

### Profile DFS

```bash
py-spy record -o DFS_profile.svg -- python DFS.py
```

### Profile the combined comparison

```bash
py-spy record -o BFS_DFS_profile.svg -- python BFS_DFS_Comparison.py
```

After profiling, open the generated `.svg` file in Chrome or another browser. The SVG is the actual profile generated from your computer and should be attached to the SLE-2 document if required.

If Git Bash cannot find `py-spy`, run:

```bash
where py-spy
```

Then use the returned `.exe` path in the `py-spy record` command.

## Complexity Summary

| Algorithm | Best Search Case | Average Search Case | Worst Search Case | Space |
|---|---|---|---|---|
| BFS | O(1) | O(V + E) upper bound | O(V + E) | O(V) |
| DFS | O(1) | O(V + E) upper bound | O(V + E) | O(V) |

These best/average/worst labels refer to **target searching**. For a full graph traversal, both algorithms use O(V + E) time.

## Learning Outcomes

- Implement BFS using a queue.
- Implement DFS using recursion.
- Compare search paths and expanded nodes.
- Measure execution time in milliseconds.
- Understand best, average and worst search cases.
- Generate profiling graphs using py-spy.
- Maintain code and documentation in GitHub.
