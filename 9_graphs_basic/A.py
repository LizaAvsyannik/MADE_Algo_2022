import sys
from sys import setrecursionlimit
import threading


def main():
    def dfs(vertex, colors, current_color):
        colors[vertex] = current_color
        for u in adjacency_list[vertex]:
            if not colors[u]:
                dfs(u, colors, current_color)

    inp = sys.stdin.readlines()
    n, m = map(int, inp[0].split())
    adjacency_list = [[] for _ in range(n)]
    for edge in inp[1:]:
        edge = list(map(int, edge.split()))
        adjacency_list[edge[0] - 1].append(edge[1] - 1)
        adjacency_list[edge[1] - 1].append(edge[0] - 1)

    cnt = 0
    colors = [0] * n
    for vertex in range(n):
        if not colors[vertex]:
            cnt += 1
            dfs(vertex, colors, cnt)

    print(cnt)
    print(*colors)


setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)
thread = threading.Thread(target=main)
thread.start()
