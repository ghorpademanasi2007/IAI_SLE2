from collections import deque
import time


GRAPH = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}


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


def measure(function, target, runs=10000):
    function(GRAPH, 'A', target)
    times = []
    path = None
    nodes = 0

    for _ in range(runs):
        start_time = time.perf_counter()
        path, nodes = function(GRAPH, 'A', target)
        end_time = time.perf_counter()
        times.append((end_time - start_time) * 1000)

    return path, nodes, sum(times) / len(times), min(times), max(times)


if __name__ == '__main__':
    cases = [('Best', 'A'), ('Average', 'E'), ('Worst', 'Z')]
    rows = []

    for case, target in cases:
        for algorithm, function in [('BFS', bfs), ('DFS', dfs)]:
            path, nodes, average, best, worst = measure(function, target)
            rows.append((case, algorithm, target, average, best, worst, nodes, path))

    print('\n' + '=' * 100)
    print('                 BFS vs DFS - COMPLETE PERFORMANCE TABLE')
    print('=' * 100)
    print('Runs per case: 10000')
    print('-' * 100)
    print(f"{'Case':<12}{'Algorithm':<12}{'Target':<9}{'Average(ms)':<17}{'Best(ms)':<15}{'Worst(ms)':<15}{'Nodes':<8}")
    print('-' * 100)

    for row in rows:
        print(f'{row[0]:<12}{row[1]:<12}{row[2]:<9}{row[3]:<17.6f}{row[4]:<15.6f}{row[5]:<15.6f}{row[6]:<8}')

    print('-' * 100)
    print('\nPATHS')
    for row in rows:
        print(f'{row[0]:<12}{row[1]:<12}', ' -> '.join(row[7]) if row[7] else 'Not Found')

    print('\nCOMPLEXITY')
    print('BFS: Best O(1), Average O(V + E) upper bound, Worst O(V + E), Space O(V)')
    print('DFS: Best O(1), Average O(V + E) upper bound, Worst O(V + E), Space O(V)')
