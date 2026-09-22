import time


# ---------------- DFS SEARCH ----------------
def dfs_search(graph, vertex, target, visited=None, path=None, expanded=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    if expanded is None:
        expanded = [0]

    if vertex in visited:
        return None, expanded[0]

    visited.add(vertex)
    expanded[0] += 1
    current_path = path + [vertex]

    if vertex == target:
        return current_path, expanded[0]

    for neighbour in graph[vertex]:
        result, count = dfs_search(
            graph, neighbour, target, visited, current_path, expanded
        )
        if result is not None:
            return result, count

    return None, expanded[0]


# ---------------- GRAPH ----------------
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}


# ---------------- TIMING ----------------
def measure_dfs(target, runs=10000):
    times = []
    path = None
    nodes = 0

    # Warm-up
    dfs_search(graph, 'A', target)

    for _ in range(runs):
        start_time = time.perf_counter()
        path, nodes = dfs_search(graph, 'A', target)
        end_time = time.perf_counter()
        times.append((end_time - start_time) * 1000)

    average = sum(times) / len(times)
    best = min(times)
    worst = max(times)

    return path, nodes, average, best, worst


# ---------------- MAIN ----------------
if __name__ == '__main__':
    cases = [('Best', 'A'), ('Average', 'E'), ('Worst', 'Z')]

    print('\n' + '=' * 88)
    print('                    DFS PERFORMANCE ANALYSIS')
    print('=' * 88)
    print('Graph: A -> B,C | B -> D,E | C -> F | D,E,F -> G')
    print('Runs per case: 10000')

    print('\n' + '-' * 88)
    print(f"{'Case':<12}{'Target':<10}{'Average(ms)':<18}{'Best(ms)':<16}{'Worst(ms)':<16}{'Nodes':<8}")
    print('-' * 88)

    for case, target in cases:
        path, nodes, average, best, worst = measure_dfs(target)
        print(f'{case:<12}{target:<10}{average:<18.6f}{best:<16.6f}{worst:<16.6f}{nodes:<8}')
        print('Path:', ' -> '.join(path) if path else 'Not Found')

    print('-' * 88)
    print('Best search case    : O(1)')
    print('Average search case : O(V + E) upper bound')
    print('Worst search case   : O(V + E)')
    print('Space complexity    : O(V)')
    print('\nPy-spy command:')
    print('py-spy record --rate 100 -o DFS_profile.svg -- python DFS.py')
