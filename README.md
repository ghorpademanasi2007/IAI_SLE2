# IAI_SLE2

## SLE-2: BFS and DFS Graph Traversal

This repository contains Python implementations of **Breadth First Search (BFS)** and **Depth First Search (DFS)** for graph traversal. It also includes a graph representation, py-spy profiling commands, complexity analysis, and a contribution log.

## Repository Files

| File | Description |
|---|---|
| `BFS.py` | Breadth First Search implementation using a queue |
| `DFS.py` | Depth First Search implementation using recursion |
| `graph.dot` | Graph representation compatible with Graphviz |
| `CONTRIBUTION_LOG.md` | Project contribution record |
| `README.md` | Project documentation |

## Graph Used

The graph contains six vertices: A, B, C, D, E and F.

```text
        A
       / \
      B   C
     / \   \
    D   E---F
```

### Traversals from A

- **BFS:** A -> B -> C -> D -> E -> F
- **DFS:** A -> B -> D -> E -> F -> C

## BFS

BFS visits vertices level by level. It uses a queue, so the first discovered vertex is processed first.

Run:

```bash
python BFS.py
```

Expected output:

```text
BFS traversal: A -> B -> C -> D -> E -> F
```

## DFS

DFS explores one path as deeply as possible before backtracking. This implementation uses recursion.

Run:

```bash
python DFS.py
```

Expected output:

```text
DFS traversal: A -> B -> D -> E -> F -> C
```

## Time and Space Complexity

For an adjacency-list graph with **V vertices** and **E edges**:

| Algorithm | Best Case | Average Case | Worst Case | Space |
|---|---|---|---|---|
| BFS | O(V + E) | O(V + E) | O(V + E) | O(V) |
| DFS | O(V + E) | O(V + E) | O(V + E) | O(V) |

For graph traversal, the standard complexity is O(V + E) because each reachable vertex and edge is processed a bounded number of times.

## py-spy Profiling

`py-spy` is a sampling profiler for Python programs. It can be used without changing the BFS or DFS source code.

### 1. Check py-spy installation

```bash
py-spy --version
```

If `py-spy` is not recognized, use the full executable path, for example:

```bash
"/c/Users/<YOUR_USERNAME>/AppData/Roaming/Python/Python313/Scripts/py-spy.exe" --version
```

### 2. Profile BFS

From the project folder:

```bash
py-spy record -o BFS_profile.svg -- python BFS.py
```

If the command is not recognized, use:

```bash
"/c/Users/<YOUR_USERNAME>/AppData/Roaming/Python/Python313/Scripts/py-spy.exe" record -o BFS_profile.svg -- python BFS.py
```

### 3. Profile DFS

```bash
py-spy record -o DFS_profile.svg -- python DFS.py
```

Or with the full executable path:

```bash
"/c/Users/<YOUR_USERNAME>/AppData/Roaming/Python/Python313/Scripts/py-spy.exe" record -o DFS_profile.svg -- python DFS.py
```

### 4. View the profiling graphs

After a successful run, py-spy creates:

- `BFS_profile.svg`
- `DFS_profile.svg`

Open each SVG file in a web browser to inspect the profiling visualization.

> Note: The SVG profiling files are generated on your computer when you run py-spy. They are not source-code files and should be added to GitHub only if your assignment specifically requires the generated profiles.

## Git Commands

After adding or changing files locally:

```bash
git status
git add .
git commit -m "Add BFS DFS profiling and documentation"
git push origin main
```

## Learning Outcomes

- Understand graph representation using an adjacency list.
- Implement BFS using a queue.
- Implement DFS using recursion.
- Compare BFS and DFS traversal order.
- Understand time and space complexity.
- Use py-spy to profile Python programs.
- Maintain project documentation and a contribution log.
