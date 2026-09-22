# IAI_SLE2

## SLE-2: BFS and DFS Graph Traversal

This repository contains a simple implementation and performance study of **Breadth First Search (BFS)** and **Depth First Search (DFS)** in Python.

### Files

| File | Purpose |
|---|---|
| `BFS.py` | BFS traversal, search path and timing analysis |
| `DFS.py` | DFS traversal, search path and timing analysis |
| `graph.dot` | Graph used for the experiment |
| `CONTRIBUTION_LOG.md` | Work/contribution record |

Extra experimental files have been removed so the repository contains only the required SLE-2 files.

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

Adjacency list used by both programs:

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

The programs measure three practical search cases:

- **Best case:** target `A` is the starting node.
- **Average case:** target `E` is found after partial exploration.
- **Worst case:** target `Z` is absent, so the reachable graph is fully explored.

The exact measured time depends on the computer, Python version and current system load. Therefore the programs calculate the values during execution instead of storing fixed values.

## Time Measurement

Python's `time.perf_counter()` is used to measure execution time in milliseconds. Each case is executed **5000 times**. The program reports:

- Average Time = mean of all measured runs
- Best Time = minimum measured run
- Worst Time = maximum measured run
- Nodes = number of nodes expanded by the search

### Comparison table for the report

After running both programs, record the printed values in this format:

| Case | BFS Average (ms) | BFS Best (ms) | BFS Worst (ms) | DFS Average (ms) | DFS Best (ms) | DFS Worst (ms) |
|---|---:|---:|---:|---:|---:|---:|
| Best | from run | from run | from run | from run | from run | from run |
| Average | from run | from run | from run | from run | from run | from run |
| Worst | from run | from run | from run | from run | from run | from run |

Do not copy example timing values from another computer; use the values printed by your own run.

## Complexity

For an adjacency-list graph, both BFS and DFS have a standard worst-case time complexity of **O(V + E)** and space complexity of **O(V)**, where `V` is the number of vertices and `E` is the number of edges.

If the starting node is already the target, the search can finish immediately, giving a practical best case of **O(1)** for these search programs.

## Running the Programs

Open Git Bash or PowerShell in the repository folder.

```bash
python BFS.py
python DFS.py
```

## py-spy Profiling

Install py-spy:

```bash
python -m pip install py-spy
```

Check the installation:

```bash
py-spy --version
```

Create the BFS profiling SVG:

```bash
py-spy record --rate 100 -o BFS_profile.svg -- python BFS.py
```

Create the DFS profiling SVG:

```bash
py-spy record --rate 100 -o DFS_profile.svg -- python DFS.py
```

The generated files are:

```text
BFS_profile.svg
DFS_profile.svg
```

Open either SVG file in a browser to inspect the py-spy flame graph.

### Important

`time.perf_counter()` provides the numerical average/best/worst timing values. **py-spy is used for sampling/profiling and generating the SVG flame graph.** The two tools have different purposes and should not be treated as the same measurement.

## Expected Output Format

Each program prints a table similar to:

```text
Case       Target   Average(ms)     Best(ms)        Worst(ms)       Nodes
----------------------------------------------------------------------------
Best       A        ...              ...             ...              ...
Average    E        ...              ...             ...              ...
Worst      Z        ...              ...             ...              ...
```

The `...` values are generated on the student's computer when the program is run.
