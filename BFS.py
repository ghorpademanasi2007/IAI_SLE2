from collections import deque
import time


# ---------------- BFS SEARCH ----------------
def bfs_search(graph, start, target):
    queue = deque([(start, [start])])
    visited = {start}
    nodes_expanded = 0

    while queue:
        vertex, path = queue.popleft()
        nodes_expanded += 1

        if vertex == target:
            return path, nodes_expanded

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, path + [neighbour]))

    return None, nodes_expanded


# ---------------- TIME MEASUREMENT ----------------
def measure_bfs(graph, start, target, runs=10000):
    times = []
    path = None
    nodes = 0

    # Warm-up call before collecting measurements.
    bfs_search(graph, start, target)

    for _ in range(runs):
        begin = time.perf_counter()
        path, nodes = bfs_search(graph, start, target)
        end = time.perf_counter()
        times.append((end - begin) * 1000)

    average_time = sum(times) / len(times)
    best_time = min(times)
    worst_time = max(times)

    return path, nodes, average_time, best_time, worst_time


# ---------------- GRAPH ----------------
# Same graph is used for BFS and DFS comparison.
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}


# ---------------- MAIN ----------------
if __name__ == '__main__':
    start = 'A'
    cases = [
        ('Best', 'A'),       # Starting node is the target.
        ('Average', 'E'),    # Partial graph exploration.
        ('Worst', 'Z')       # Target does not exist.
    ]

    print('\n' + '=' * 82)
    print('                    BFS PERFORMANCE ANALYSIS')
    print('=' * 82)
    print('Graph       : A -> B,C | B -> D,E | C -> F | D,E,F -> G')
    print('Start node  : A')
    print('Runs/case   : 10000')

    results = []

    for case_name, target in cases:
        path, nodes, average, best, worst = measure_bfs(
            graph, start, target
        )

        path_text = ' -> '.join(path) if path else 'Not Found'
        results.append((case_name, target, average, best, worst, nodes))

        print('\n' + case_name.upper() + ' CASE')
        print('Target          :', target)
        print('Path            :', path_text)
        print('Nodes expanded  :', nodes)
        print(f'Average time    : {average:.6f} ms')
        print(f'Best time       : {best:.6f} ms')
        print(f'Worst time      : {worst:.6f} ms')

    print('\n' + '=' * 82)
    print('                         BFS TABLE')
    print('=' * 82)
    print(
        f"{'Case':<12}{'Target':<10}{'Average(ms)':<17}"
        f"{'Best(ms)':<15}{'Worst(ms)':<15}{'Nodes':<8}"
    )
    print('-' * 82)

    for case_name, target, average, best, worst, nodes in results:
        print(
            f'{case_name:<12}{target:<10}{average:<17.6f}'
            f'{best:<15.6f}{worst:<15.6f}{nodes:<8}'
        )

    print('-' * 82)
    print('Best search case    : O(1)')
    print('Average search case : O(V + E) upper bound')
    print('Worst search case   : O(V + E)')
    print('Space complexity    : O(V)')
    print('\nUse py-spy externally to create the profiling SVG:')
    print('py-spy record --rate 100 -o BFS_profile.svg -- python BFS.py')
