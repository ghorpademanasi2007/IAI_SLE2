# IAI_SLE2

## SLE-2: BFS and DFS Performance Analysis

This project implements **Breadth First Search (BFS)** and **Depth First Search (DFS)** in Python. It measures **average time, best time and worst time** for selected search cases and provides a direct BFS-vs-DFS comparison table. The programs can also be profiled using **py-spy**.

## Files

| File | Purpose |
|---|---|
| `BFS.py` | BFS search with average, best and worst timing |
| `DFS.py` | DFS search with average, best and worst timing |
| `BFS_DFS_Comparison.py` | Combined BFS vs DFS comparison table |
| `graph.dot` | Seven-node graph |
| `CONTRIBUTION_LOG.md` | Contribution history |

## Graph

The same graph is used for BFS and DFS so the measured comparison is consistent:

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

## Cases Used

The programs search for a target starting from `A`.

| Case | Target | Meaning | Search complexity |
|---|---|---|---|
| Best | `A` | Target is the starting node | O(1) |
| Average | `E` | Target is found after partial exploration | O(V + E) upper bound |
| Worst | `Z` | Target is absent, so all reachable nodes are explored | O(V + E) |

For a complete graph traversal, both BFS and DFS are O(V + E) with an adjacency-list representation.

## Timing Method

Each case is measured **10,000 times** using Python's `time.perf_counter()`.

For every case the program reports:

- **Average time** = total measured time / number of runs
- **Best time** = smallest measured run time
- **Worst time** = largest measured run time
- Search path
- Number of nodes expanded

The exact millisecond values are generated on the student's computer and are not hard-coded.

## BFS Output

Run:

```bash
python BFS.py
```

The output contains a section for each case followed by a table such as:

```text
Case        Target    Average(ms)      Best(ms)       Worst(ms)      Nodes
-----------------------------------------------------------------------------
Best        A         ...              ...            ...             1
Average     E         ...              ...            ...             3
Worst       Z         ...              ...            ...             7
```

## DFS Output

Run:

```bash
python DFS.py
```

DFS prints the same metrics so the two algorithms can be compared using the same graph and targets.

## BFS vs DFS Comparison

Run:

```bash
python BFS_DFS_Comparison.py
```

It prints one combined table:

```text
Case      Algorithm   Target   Average(ms)    Best(ms)    Worst(ms)    Nodes
----------------------------------------------------------------------------
Best      BFS         A        ...             ...         ...          1
Best      DFS         A        ...             ...         ...          1
Average   BFS         E        ...             ...         ...          3
Average   DFS         E        ...             ...         ...          3
Worst     BFS         Z        ...             ...         ...          7
Worst     DFS         Z        ...             ...         ...          7
```

The values shown as `...` are intentionally produced by the actual run rather than copied from another computer.

## py-spy Profiling

`py-spy` is a sampling profiler for Python. It can record a Python program and create an interactive SVG flame graph without modifying the program. citeturn0search0

Install/check it with:

```bash
python -m pip install py-spy
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

`py-spy record` supports running a Python command directly and writing the profile to an SVG file. citeturn0search0

After the command finishes, open the generated `.svg` file in Chrome. The SVG is the actual profile generated from your computer.

If Git Bash cannot find `py-spy`, run:

```bash
where py-spy
```

Then use the returned `py-spy.exe` path.

## Important Difference

**Timing and profiling have different purposes:**

- `time.perf_counter()` in the programs gives the numerical average/best/worst execution times.
- `py-spy` gives a sampling profile/flame graph showing where execution time is spent. It does not calculate Big-O complexity. citeturn0search0
- Big-O complexity is obtained from analysis of the algorithm.

## Complexity Summary

| Algorithm | Best Search Case | Average Search Case | Worst Search Case | Space |
|---|---|---|---|---|
| BFS | O(1) | O(V + E) upper bound | O(V + E) | O(V) |
| DFS | O(1) | O(V + E) upper bound | O(V + E) | O(V) |

## Learning Outcomes

- Implement BFS using a queue.
- Implement DFS using recursion.
- Measure average, best and worst execution times.
- Count expanded nodes and display search paths.
- Compare BFS and DFS in one table.
- Generate SVG profiling graphs using py-spy.
- Understand the difference between measured runtime and Big-O complexity.
