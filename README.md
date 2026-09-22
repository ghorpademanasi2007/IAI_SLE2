# IAI_SLE2

## SLE-2: BFS and DFS Performance Analysis

This project implements **Breadth First Search (BFS)** and **Depth First Search (DFS)** in Python. It measures **average, best and worst execution time** and provides a BFS-vs-DFS comparison table.

## Files

| File | Purpose |
|---|---|
| `BFS.py` | BFS search, timing and complexity analysis |
| `DFS.py` | DFS search, timing and complexity analysis |
| `BFS_DFS_Comparison.py` | Combined BFS and DFS comparison |
| `5.py` | Standalone combined program |
| `graph.dot` | Graphviz graph |
| `CONTRIBUTION_LOG.md` | Contribution history |

## Graph

```text
                 A
               /   \
              B     C
             / \     \
            D   E     F
             \ /     /
              G-----
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

## Test Cases

The search starts at `A`.

| Case | Target | Meaning |
|---|---|---|
| Best | `A` | Target is the starting node. |
| Average | `E` | Target is reached after partial exploration. |
| Worst | `Z` | Target is absent, so all reachable nodes are explored. |

For adjacency-list BFS/DFS traversal, the standard full-traversal bound is **O(V + E)**. A search can finish earlier when the target is found; the best case here is O(1) because the target is the starting node.

## Timing

Each case is measured **10,000 times** using Python `time.perf_counter()`.

The programs calculate:

- **Average time** — mean of all measured runs.
- **Best time** — minimum measured run.
- **Worst time** — maximum measured run.
- **Nodes expanded** — number of nodes examined.
- **Path** — path found when the target exists.

The actual millisecond values are generated on the computer where the program is run. They are not hard-coded.

## Run BFS

```bash
python BFS.py
```

## Run DFS

```bash
python DFS.py
```

## Run Comparison

```bash
python BFS_DFS_Comparison.py
```

Example table format:

```text
Case        Algorithm   Target   Average(ms)    Best(ms)       Worst(ms)      Nodes
------------------------------------------------------------------------------------
Best        BFS         A        actual value   actual value   actual value   1
Best        DFS         A        actual value   actual value   actual value   1
Average     BFS         E        actual value   actual value   actual value   ...
Average     DFS         E        actual value   actual value   actual value   ...
Worst       BFS         Z        actual value   actual value   actual value   7
Worst       DFS         Z        actual value   actual value   actual value   7
```

## py-spy

`py-spy` is used for sampling profiling and SVG flame graphs. It is separate from `time.perf_counter()`: the Python program calculates the numerical times, while py-spy profiles sampled execution.

Install:

```bash
python -m pip install py-spy
```

Check:

```bash
py-spy --version
```

### BFS profile

```bash
py-spy record --rate 100 -o BFS_profile.svg -- python BFS.py
```

### DFS profile

```bash
py-spy record --rate 100 -o DFS_profile.svg -- python DFS.py
```

### Comparison profile

```bash
py-spy record --rate 100 -o BFS_DFS_profile.svg -- python BFS_DFS_Comparison.py
```

Open the generated SVG files in Chrome.

If Git Bash cannot find py-spy:

```bash
where py-spy
```

Then use the returned `py-spy.exe` path.

## Complexity

| Algorithm | Best Search Case | Average/Worst Bound | Space |
|---|---|---|---|
| BFS | O(1) | O(V + E) | O(V) |
| DFS | O(1) | O(V + E) | O(V) |

## Learning Outcomes

- Implement BFS using a queue.
- Implement DFS using recursion.
- Measure best, average and worst execution times.
- Count expanded nodes and display paths.
- Compare BFS and DFS on the same graph.
- Generate profiling graphs with py-spy.
- Understand the difference between measured runtime and Big-O complexity.
