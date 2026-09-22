# BFS and DFS Graph

The same graph is used for both BFS and DFS timing experiments.

```text
                 A
               /   \
              B     C
             / \     \
            D   E     F
             \ /     /
              G-----
```

### Edges

- A -> B
- A -> C
- B -> D
- B -> E
- C -> F
- D -> G
- E -> G
- F -> G

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

### Search cases

- **Best case:** target `A`
- **Average case:** target `E`
- **Worst case:** target `Z` (not present)

The graph is represented in `graph.dot` and is used consistently by `BFS.py`, `DFS.py`, and `BFS_DFS_Comparison.py`.
