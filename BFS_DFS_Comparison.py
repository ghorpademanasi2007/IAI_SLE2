import time

from BFS import bfs_search, graph as bfs_graph
from DFS import dfs_search, graph as dfs_graph


CASES = [
    ('Best', 'A'),
    ('Average', 'E'),
    ('Worst', 'Z')
]


def benchmark(search_function, graph, target, runs=1000):
    times = []
    path = None
    nodes = 0

    for _ in range(runs):
        start_time = time.perf_counter()
        path, nodes = search_function(graph, 'A', target)
        end_time = time.perf_counter()
        times.append((end_time - start_time) * 1000)

    return path, nodes, sum(times) / runs, min(times), max(times)


if __name__ == '__main__':
    print('=' * 78)
    print('                 BFS vs DFS PERFORMANCE')
    print('=' * 78)
    print('Graph: A -> {B, C}, B -> {D, E}, C -> F, D/E/F -> G')
    print('1000 timing runs are used for every case.')
    print()

    print(f"{'Case':<10}{'Algorithm':<12}{'Target':<9}{'Average(ms)':<15}{'Best(ms)':<14}{'Worst(ms)':<14}{'Nodes':<8}")
    print('-' * 78)

    for case_name, target in CASES:
        for name, function, graph in [
            ('BFS', bfs_search, bfs_graph),
            ('DFS', dfs_search, dfs_graph)
        ]:
            path, nodes, average, best, worst = benchmark(function, graph, target)
            print(f'{case_name:<10}{name:<12}{target:<9}{average:<15.6f}{best:<14.6f}{worst:<14.6f}{nodes:<8}')

    print('-' * 78)
    print('Search-case complexity: Best = O(1); Average/Worst = O(V + E)')
    print('Note: measured times depend on the computer and system load.')
