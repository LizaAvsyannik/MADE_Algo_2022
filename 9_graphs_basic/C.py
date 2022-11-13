import sys
from sys import setrecursionlimit
import threading


def main():
    def dfs(vertex, colors):
        colors[vertex] = 1

        nonlocal has_cycle
        if not has_cycle:
            for u in adjacency_list[vertex]:
                if not colors[u]:
                    dfs(u, colors)
                elif colors[u] == 1:
                    has_cycle = True

            colors[vertex] = 2
            top_sorted.append(vertex + 1)

    inp = sys.stdin.readlines()
    n, m = map(int, inp[0].split())
    adjacency_list = [[] for _ in range(n)]
    for edge in inp[1:]:
        edge = list(map(int, edge.split()))
        adjacency_list[edge[0] - 1].append(edge[1] - 1)

    colors = [0] * n
    top_sorted = []
    has_cycle = False
    for vertex in range(n):
        if not colors[vertex]:
            dfs(vertex, colors)

    if has_cycle:
        print(-1)
    else:
        top_sorted.reverse()
        print(*top_sorted)


setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)
thread = threading.Thread(target=main)
thread.start()
