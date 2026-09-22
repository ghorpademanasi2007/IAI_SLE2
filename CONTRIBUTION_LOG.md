# Contribution Log

## IAI_SLE2 – BFS and DFS Graph Traversal

| Date | Contribution | File(s) |
|---|---|---|
| 22-Sep-2026 | Created BFS graph-search implementation | `BFS.py` |
| 22-Sep-2026 | Created DFS graph-search implementation | `DFS.py` |
| 22-Sep-2026 | Added best, average and worst execution-time measurement using `time.perf_counter()` | `BFS.py`, `DFS.py` |
| 22-Sep-2026 | Added 5000-run timing procedure for more stable measurements | `BFS.py`, `DFS.py` |
| 22-Sep-2026 | Added py-spy profiling commands and documentation | `README.md` |
| 22-Sep-2026 | Added common graph representation for BFS and DFS | `graph.dot` |
| 22-Sep-2026 | Cleaned repository to keep only required SLE-2 files | Repository |

## Tools Used

- Python 3
- `time.perf_counter()` for execution-time measurement
- `py-spy` for sampling/profiling and SVG flame graphs
- GitHub for version control and project documentation

## Notes

The measured millisecond values are generated on the student's computer when the programs are executed. They are not hard-coded because execution time varies with hardware, Python version and system load.
