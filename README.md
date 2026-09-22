# IAI_SLE2

## SLE-2: BFS and DFS Search with Performance Analysis

This repository contains Python implementations of **Breadth First Search (BFS)** and **Depth First Search (DFS)**. The programs demonstrate graph searching, best/average/worst-case analysis, execution-time measurement, and profiling with **py-spy**.

## Repository Files

| File | Description |
|---|---|
| `BFS.py` | BFS search with best/average/worst-case timing |
| `DFS.py` | DFS search with best/average/worst-case timing |
| `graph.dot` | Graph representation compatible with Graphviz |
| `CONTRIBUTION_LOG.md` | Project contribution record |
| `README.md` | Project documentation |

## Graph Used

```text
        A
       / \
      B   C
     / \   \
    D   E---F
```

The programs use an adjacency-list representation.

## Case Analysis

The programs search for a target vertex rather than always traversing the complete graph. Therefore, the case depends on where the target occurs.

| Case | Target used | Meaning | Time complexity |
|---|---|---|---|
| Best | `A` | Target is the starting vertex | O(1) |
| Average | `E` | Target is found after some exploration | O(V + E) upper bound |
| Worst | `Z` | Target is absent, so all reachable vertices are explored | O(V + E) |

For a **full traversal** of a graph represented by adjacency lists, both BFS and DFS are O(V + E). A full traversal does not have a meaningful O(1) best case because all reachable vertices/edges are processed. citeturn0search24turn0search14

Here, `V` is the number of vertices and `E` is the number of edges.

## BFS

BFS uses a queue and explores the graph level by level.

Run normally:

```bash
python BFS.py
```

The program prints whether each target is found and measures each case over 10,000 repetitions.

## DFS

DFS uses recursion and explores one branch as deeply as possible before backtracking.

Run normally:

```bash
python DFS.py
```

The program prints whether each target is found and measures each case over 10,000 repetitions.

## py-spy Profiling

`py-spy` is a sampling profiler for Python. Its `record` command can run a Python program and generate an SVG flame graph. citeturn0search0

### Check installation

```bash
py-spy --version
```

If needed:

```bash
pip install py-spy
```

### Profile BFS

```bash
py-spy record -o BFS_profile.svg -- python BFS.py
```

### Profile DFS

```bash
py-spy record -o DFS_profile.svg -- python DFS.py
```

The programs intentionally repeat each case 10,000 times so the profiler has enough execution activity to sample. The resulting SVG files can be opened in a browser.

If `py-spy` is not recognized in Git Bash, first run:

```bash
where py-spy
```

Then use the returned executable path, for example:

```bash
"/c/Users/<YOUR_USERNAME>/AppData/Roaming/Python/Python313/Scripts/py-spy.exe" record -o BFS_profile.svg -- python BFS.py
```

The exact path depends on where Python installed `py-spy`.

## Important Note About py-spy

py-spy is a **profiler**, not a tool that proves Big-O complexity. The Big-O cases are derived from the algorithm; py-spy provides a practical visualization of where the Python program spends execution time. citeturn0search0

## Expected Outputs

BFS and DFS both print three cases:

```text
Best case
Average case
Worst case
```

They also print measured elapsed time for 10,000 repetitions. Exact times will vary with the computer, Python version, and system load.

## Git Commands

After making local changes or generating files:

```bash
git status
git add .
git commit -m "Add BFS DFS case analysis and py-spy profiling"
git push origin main
```

## Learning Outcomes

- Implement BFS using a queue.
- Implement DFS using recursion.
- Understand best, average and worst search cases.
- Understand O(1) early-success search and O(V + E) graph exploration.
- Measure practical execution time with Python.
- Generate profiling visualizations using py-spy.
- Maintain a GitHub repository with documentation.
