from collections import deque
import time


# ==================== BFS ====================
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


# ==================== DFS ====================
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
            result, nodes = dfs(
                graph, neighbour, target, visited, path
            )
            if result is not None:
                return result, nodes

    return None, len(visited)


# ==================== GRAPH ====================
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}


# ==================== MEASUREMENT ====================
def measure(function, target, runs=10000):
    times = []
    path = None
    nodes = 0

    # Warm-up run.
    function(graph, 'A', target)

    for _ in range(runs):
        start_time = time.perf_counter()
        path, nodes = function(graph, 'A', target)
        end_time = time.perf_counter()
        times.append((end_time - start_time) * 1000)

    average = sum(times) / len(times)
    best = min(times)
    worst = max(times)

    return path, nodes, average, best, worst


# ==================== MAIN ====================
if __name__ == '__main__':
    cases = [
        ('Best', 'A'),
        ('Average', 'E'),
        ('Worst', 'Z')
    ]

    print('\n' + '=' * 100)
    print('                       BFS vs DFS PERFORMANCE ANALYSIS')
    print('=' * 100)
    print('Graph      : A -> B,C | B -> D,E | C -> F | D,E,F -> G')
    print('Start      : A')
    print('Runs/case  : 10000')

    rows = []

    for case_name, target in cases:
        for algorithm, function in [('BFS', bfs), ('DFS', dfs)]:
            path, nodes, average, best, worst = measure(function, target)
            path_text = ' -> '.join(path) if path else 'Not Found'
            rows.append((
                case_name, algorithm, target,
                average, best, worst, nodes, path_text
            ))

    print('\n' + '-' * 100)
    print('                         COMPARISON TABLE')
    print('-' * 100)
    print(
        f"{'Case':<12}{'Algorithm':<12}{'Target':<9}"
        f"{'Average(ms)':<17}{'Best(ms)':<15}"
        f"{'Worst(ms)':<15}{'Nodes':<8}"
    )
    print('-' * 100)

    for row in rows:
        print(
            f'{row[0]:<12}{row[1]:<12}{row[2]:<9}'
            f'{row[3]:<17.6f}{row[4]:<15.6f}'
            f'{row[5]:<15.6f}{row[6]:<8}'
        )

    print('-' * 100)
    print('SEARCH PATHS')
    print('-' * 100)

    for row in rows:
        print(f'{row[0]:<12}{row[1]:<12}{row[7]}')

    print('\n' + '=' * 100)
    print('                         COMPLEXITY ANALYSIS')
    print('=' * 100)
    print('BFS -> Best: O(1), Average: O(V + E), Worst: O(V + E), Space: O(V)')
    print('DFS -> Best: O(1), Average: O(V + E), Worst: O(V + E), Space: O(V)')

    print('\n' + '=' * 100)
    print('                         PY-SPY COMMANDS')
    print('=' * 100)
    print('BFS : py-spy record --rate 100 -o BFS_profile.svg -- python BFS.py')
    print('DFS : py-spy record --rate 100 -o DFS_profile.svg -- python DFS.py')
    print('Both: py-spy record --rate 100 -o BFS_DFS_profile.svg -- python 5.py')
    print('\nNote: timing values are measured on the current computer.')
