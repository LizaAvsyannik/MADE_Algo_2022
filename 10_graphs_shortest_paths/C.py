import sys
from copy import deepcopy

MAX_DISTANCE = 1e6
NO_EDGE = 1e5


def floyd(distances, n_verticies):
    next = [list(range(n_verticies)) for _ in range(n_verticies)]
    for k in range(n_verticies):
        for u in range(n_verticies):
            for v in range(n_verticies):
                if distances[u][v] > distances[u][k] + distances[k][v]:
                    distances[u][v] = max(-MAX_DISTANCE, distances[u][k] + distances[k][v])
                    next[u][v] = next[u][k]
                if u == v and distances[u][v] < 0:
                    return find_cycle(u, next)


def find_cycle(cycle_start, next):
    negative_cycle = [cycle_start]
    next_vertex = next[cycle_start][cycle_start]
    while next_vertex != cycle_start:
        negative_cycle.append(next_vertex)
        next_vertex = next[next_vertex][cycle_start]
    return negative_cycle


inp = sys.stdin.readlines()
n = int(inp[0])
weights = [list(map(lambda x: int(x) if int(x) < NO_EDGE else MAX_DISTANCE, i.split())) for i in inp[1:]]

distances = deepcopy(weights)

result = floyd(distances, n)

if not result:
    print('NO')
else:
    print('YES')
    print(len(result))
    print(*[v + 1 for v in result])
