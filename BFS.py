from collections import deque
import time


# Breadth First Search: returns path, expanded-node count and found status.
def bfs_search(graph, start, target):
    queue = deque([(start, [start])])
    visited = {start}
    expanded = 0

    while queue:
        vertex, path = queue.popleft()
        expanded += 1

        if vertex == target:
            return path, expanded

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None, expanded


def benchmark_case(graph, start, target, runs=10000):
    times = []
    path = None
    nodes = 0

    # Warm-up run avoids using the first call as the only measurement.
    bfs_search(graph, start, target)

    for _ in range(runs):
        begin = time.perf_counter()
        path, nodes = bfs_search(graph, start, target)
        end = time.perf_counter()
        times.append((end - begin) * 1000)

    average = sum(times) / len(times)
    return path, nodes, average, min(times), max(times)


# Seven-node directed graph used for the experiment.
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}


if __name__ == '__main__':
    start = 'A'
    cases = [
        ('Best', 'A'),
        ('Average', 'E'),
        ('Worst', 'Z')
    ]

    print('=' * 70)
    print('                 BFS PERFORMANCE ANALYSIS')
    print('=' * 70)
    print('Graph       : A, B, C, D, E, F, G')
    print('Start node  : A')
    print('Runs/case   : 10000')
    print()

    results = []

    for case_name, target in cases:
        path, nodes, average, best, worst = benchmark_case(
            graph, start, target
        )
        path_text = ' -> '.join(path) if path else 'Not found'
        results.append((case_name, target, average, best, worst, nodes))

        print(f'{case_name.upper()} CASE')
        print(f'Target         : {target}')
        print(f'Path           : {path_text}')
        print(f'Nodes expanded : {nodes}')
        print(f'Average time   : {average:.6f} ms')
        print(f'Best time      : {best:.6f} ms')
        print(f'Worst time     : {worst:.6f} ms')
        print('-' * 70)

    print('\n' + '=' * 70)
    print('                     BFS SUMMARY TABLE')
    print('=' * 70)
    print(f"{'Case':<12}{'Target':<10}{'Average(ms)':<17}{'Best(ms)':<15}{'Worst(ms)':<15}{'Nodes':<8}")
    print('-' * 77)

    for row in results:
        print(
            f'{row[0]:<12}{row[1]:<10}{row[2]:<17.6f}'
            f'{row[3]:<15.6f}{row[4]:<15.6f}{row[5]:<8}'
        )

    print('-' * 77)
    print('Search complexity: Best O(1), Average/Worst O(V + E) upper bound')
    print('Space complexity : O(V)')
