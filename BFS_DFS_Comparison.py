import time

from BFS import bfs_search, graph as bfs_graph
from DFS import dfs_search, graph as dfs_graph


CASES = [
    ('Best', 'A'),
    ('Average', 'E'),
    ('Worst', 'Z')
]

RUNS = 10000


def benchmark(search_function, graph, target, runs=RUNS):
    """Measure average, best and worst execution time for one search case."""
    times = []
    path = None
    nodes = 0

    # Warm-up call before recording measurements.
    search_function(graph, 'A', target)

    for _ in range(runs):
        start_time = time.perf_counter()
        path, nodes = search_function(graph, 'A', target)
        end_time = time.perf_counter()
        times.append((end_time - start_time) * 1000)

    return (
        path,
        nodes,
        sum(times) / len(times),
        min(times),
        max(times)
    )


if __name__ == '__main__':
    print('=' * 100)
    print('                         BFS vs DFS PERFORMANCE COMPARISON')
    print('=' * 100)
    print('Graph       : A -> B,C | B -> D,E | C -> F | D,E,F -> G')
    print('Start node  : A')
    print(f'Runs/case   : {RUNS}')
    print()

    rows = []

    for case_name, target in CASES:
        for algorithm, function, graph in [
            ('BFS', bfs_search, bfs_graph),
            ('DFS', dfs_search, dfs_graph)
        ]:
            path, nodes, average, best, worst = benchmark(
                function, graph, target
            )
            path_text = ' -> '.join(path) if path else 'Not found'
            rows.append(
                (case_name, algorithm, target, path_text,
                 average, best, worst, nodes)
            )

    print('COMPARISON TABLE')
    print('-' * 100)
    print(
        f"{'Case':<10}{'Algorithm':<12}{'Target':<9}"
        f"{'Average(ms)':<16}{'Best(ms)':<15}{'Worst(ms)':<15}{'Nodes':<8}"
    )
    print('-' * 100)

    for row in rows:
        print(
            f'{row[0]:<10}{row[1]:<12}{row[2]:<9}'
            f'{row[4]:<16.6f}{row[5]:<15.6f}'
            f'{row[6]:<15.6f}{row[7]:<8}'
        )

    print('-' * 100)
    print('PATHS')
    print('-' * 100)
    for row in rows:
        print(f'{row[0]:<10}{row[1]:<12}{row[3]}')

    print('\n' + '=' * 100)
    print('COMPLEXITY')
    print('=' * 100)
    print('BFS : Best O(1), Average/Worst O(V + E) upper bound, Space O(V)')
    print('DFS : Best O(1), Average/Worst O(V + E) upper bound, Space O(V)')
    print()
    print('Note: measured times are machine-dependent. py-spy is used to profile')
    print('the Python execution and generate an SVG flame graph; it does not')
    print('replace the timing measurements or Big-O analysis.')
