from collections import deque
import time


# Breadth First Search: returns the path to target and number of expanded nodes.
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


def measure_case(graph, start, target, repetitions=1000):
    times = []
    path = None
    nodes = 0

    for _ in range(repetitions):
        begin = time.perf_counter()
        path, nodes = bfs_search(graph, start, target)
        end = time.perf_counter()
        times.append((end - begin) * 1000)

    return path, nodes, times


# Seven-node graph used for the experiment.
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

    print('=' * 58)
    print('             BFS PERFORMANCE ANALYSIS')
    print('=' * 58)
    print('Graph nodes : A, B, C, D, E, F, G')
    print('Start node  : A')
    print('Runs/case   : 1000')
    print()

    results = []

    for case_name, target in cases:
        path, nodes, times = measure_case(graph, start, target)
        average = sum(times) / len(times)
        best = min(times)
        worst = max(times)
        path_text = ' -> '.join(path) if path else 'Not found'

        results.append((case_name, target, average, best, worst, nodes))

        print(f'{case_name.upper()} CASE')
        print(f'Target          : {target}')
        print(f'Path            : {path_text}')
        print(f'Nodes expanded  : {nodes}')
        print(f'Average time    : {average:.6f} ms')
        print(f'Best time       : {best:.6f} ms')
        print(f'Worst time      : {worst:.6f} ms')
        print('-' * 58)

    print('\n' + '=' * 58)
    print('                 SUMMARY TABLE')
    print('=' * 58)
    print(f"{'Case':<12}{'Target':<10}{'Average(ms)':<16}{'Best(ms)':<14}{'Worst(ms)':<14}{'Nodes':<8}")
    print('-' * 74)

    for row in results:
        print(f'{row[0]:<12}{row[1]:<10}{row[2]:<16.6f}{row[3]:<14.6f}{row[4]:<14.6f}{row[5]:<8}')

    print('-' * 74)
    print('Complexity: Best = O(1), Average/Worst = O(V + E)')
    print('Memory: O(V) for the queue and visited set')
