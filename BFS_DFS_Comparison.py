import time
from collections import deque


# ---------------- COMMON GRAPH ----------------
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}


# ---------------- BFS ----------------
def bfs(graph, start, target):
    queue = deque([(start, [start])])
    visited = {start}
    nodes = 0

    while queue:
        vertex, path = queue.popleft()
        nodes += 1

        if vertex == target:
            return path, nodes

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, path + [neighbour]))

    return None, nodes


# ---------------- DFS ----------------
def dfs(graph, vertex, target, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(vertex)
    path = path + [vertex]

    if vertex == target:
        return path, len(visited)

    for neighbour in graph[vertex]:
        if neighbour not in visited:
            result, nodes = dfs(graph, neighbour, target, visited, path)
            if result is not None:
                return result, nodes

    return None, len(visited)


# ---------------- BENCHMARK ----------------
def benchmark(function, target, runs=10000):
    function(graph, 'A', target)  # warm-up
    times = []
    path = None
    nodes = 0

    for _ in range(runs):
        start = time.perf_counter()
        path, nodes = function(graph, 'A', target)
        end = time.perf_counter()
        times.append((end - start) * 1000)

    return (
        path,
        nodes,
        sum(times) / len(times),
        min(times),
        max(times)
    )


# ---------------- MAIN ----------------
if __name__ == '__main__':
    cases = [('Best', 'A'), ('Average', 'E'), ('Worst', 'Z')]
    rows = []

    for case, target in cases:
        for name, function in [('BFS', bfs), ('DFS', dfs)]:
            path, nodes, average, best, worst = benchmark(function, target)
            rows.append((case, name, target, average, best, worst, nodes, path))

    print('\n' + '=' * 100)
    print('                    BFS vs DFS PERFORMANCE COMPARISON')
    print('=' * 100)
    print('Graph: A -> B,C | B -> D,E | C -> F | D,E,F -> G')
    print('Runs per case: 10000')

    print('\n' + '-' * 100)
    print(f"{'Case':<12}{'Algorithm':<12}{'Target':<9}{'Average(ms)':<17}{'Best(ms)':<15}{'Worst(ms)':<15}{'Nodes':<8}")
    print('-' * 100)

    for row in rows:
        print(f'{row[0]:<12}{row[1]:<12}{row[2]:<9}{row[3]:<17.6f}{row[4]:<15.6f}{row[5]:<15.6f}{row[6]:<8}')

    print('-' * 100)
    print('\nSEARCH PATHS')
    print('-' * 100)
    for row in rows:
        print(f'{row[0]:<12}{row[1]:<12}', ' -> '.join(row[7]) if row[7] else 'Not Found')

    print('\n' + '=' * 100)
    print('COMPLEXITY')
    print('=' * 100)
    print('BFS: Best O(1), Average O(V + E) upper bound, Worst O(V + E), Space O(V)')
    print('DFS: Best O(1), Average O(V + E) upper bound, Worst O(V + E), Space O(V)')
    print('\nPy-spy:')
    print('py-spy record --rate 100 -o BFS_DFS_profile.svg -- python BFS_DFS_Comparison.py')
