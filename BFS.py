from collections import deque
import time


# BFS search: stops when the target vertex is found.
def bfs_search(graph, start, target):
    visited = {start}
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        if vertex == target:
            return True

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False


def benchmark_case(graph, start, target, repetitions=10000):
    start_time = time.perf_counter()

    for _ in range(repetitions):
        bfs_search(graph, start, target)

    end_time = time.perf_counter()
    return end_time - start_time


# Same graph used for the traversal and profiling experiment.
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


if __name__ == '__main__':
    start = 'A'

    # Best case: target is the starting vertex.
    best_target = 'A'

    # Average case: target is a middle/deeper vertex.
    average_target = 'E'

    # Worst case: target is not present, so all reachable vertices are searched.
    worst_target = 'Z'

    print('BFS Search Analysis')
    print('Graph: A-B-C-D-E-F')
    print()

    print('Best case target   :', best_target)
    print('Found              :', bfs_search(graph, start, best_target))
    print('Time complexity    : O(1)')
    print()

    print('Average case target:', average_target)
    print('Found              :', bfs_search(graph, start, average_target))
    print('Time complexity    : O(V + E)')
    print()

    print('Worst case target  :', worst_target)
    print('Found              :', bfs_search(graph, start, worst_target))
    print('Time complexity    : O(V + E)')
    print()

    # Repeated runs make the program long enough for py-spy to sample.
    print('Measured execution time over 10,000 repetitions:')
    best_time = benchmark_case(graph, start, best_target)
    average_time = benchmark_case(graph, start, average_target)
    worst_time = benchmark_case(graph, start, worst_target)

    print(f'Best case   : {best_time:.6f} seconds')
    print(f'Average case: {average_time:.6f} seconds')
    print(f'Worst case  : {worst_time:.6f} seconds')
