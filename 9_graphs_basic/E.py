import sys
from sys import setrecursionlimit
import threading


def main():
    def dfs(vertex, visited, parent=-1, time=1):
        visited[vertex] = True
        tin[vertex] = time
        up[vertex] = time
        time += 1

        num_children = 0
        for u in adjacency_list[vertex]:
            if u != parent:
                if not visited[u]:
                    dfs(u, visited, vertex, time)
                    up[vertex] = min(up[vertex], up[u])
                    num_children += 1
                    if (up[u] >= tin[vertex]) and (parent != -1):
                        articulation_points.add(vertex + 1)
                else:
                    up[vertex] = min(up[vertex], tin[u])
        if (parent == -1) and (num_children > 1):
            articulation_points.add(vertex + 1)

    inp = sys.stdin.readlines()
    n, m = map(int, inp[0].split())
    adjacency_list = [[] for _ in range(n)]
    for edge in inp[1:]:
        edge = list(map(int, edge.split()))
        adjacency_list[edge[0] - 1].append(edge[1] - 1)
        adjacency_list[edge[1] - 1].append(edge[0] - 1)

    visited = [0] * n
    tin = [0] * n
    up = [0] * n
    articulation_points = set()
    for vertex in range(n):
        if not visited[vertex]:
            dfs(vertex, visited)

    print(len(articulation_points))
    print(*sorted(articulation_points))


setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)
thread = threading.Thread(target=main)
thread.start()
