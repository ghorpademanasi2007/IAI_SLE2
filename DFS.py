import time

# DFS graph
GRAPH = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G"],
    "E": ["G"],
    "F": ["G"],
    "G": []
}


def dfs_search(graph, node, target, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(node)
    path = path + [node]

    if node == target:
        return path, len(visited)

    for neighbour in graph[node]:
        if neighbour not in visited:
            result = dfs_search(graph, neighbour, target, visited, path)
            if result[0] is not None:
                return result

    return None, len(visited)


def measure_dfs(target, runs=5000):
    dfs_search(GRAPH, "A", target)

    times = []
    path = None
    expanded = 0

    for _ in range(runs):
        start_time = time.perf_counter()
        path, expanded = dfs_search(GRAPH, "A", target)
        end_time = time.perf_counter()
        times.append((end_time - start_time) * 1000)

    return path, expanded, sum(times) / len(times), min(times), max(times)


def print_result(case_name, target):
    path, expanded, average, best, worst = measure_dfs(target)
    path_text = " -> ".join(path) if path else "Not found"

    print(f"{case_name:<10} {target:<8} {average:<15.6f} {best:<15.6f} {worst:<15.6f} {expanded:<8}")
    print(f"Path: {path_text}")
    return average, best, worst, expanded


if __name__ == "__main__":
    print("=" * 82)
    print("                 DFS GRAPH TRAVERSAL AND TIMING")
    print("=" * 82)
    print("Graph: A -> {B,C}, B -> {D,E}, C -> F, D/E/F -> G")
    print("Timing runs per case: 5000")
    print()
    print(f"{'Case':<10} {'Target':<8} {'Average(ms)':<15} {'Best(ms)':<15} {'Worst(ms)':<15} {'Nodes':<8}")
    print("-" * 82)

    best = print_result("Best", "A")
    average = print_result("Average", "E")
    worst = print_result("Worst", "Z")

    print("-" * 82)
    print("Complexity: Best O(1) when the start node is the target; otherwise DFS is O(V+E).")
    print("Worst-case time complexity: O(V+E) and space complexity: O(V).")
    print()
    print("Py-spy command:")
    print("py-spy record --rate 100 -o DFS_profile.svg -- python DFS.py")
