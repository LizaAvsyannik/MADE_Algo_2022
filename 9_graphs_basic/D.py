import sys
from sys import setrecursionlimit
import threading


def main():
    def dfs(vertex, colors):
        visited[vertex] = True

        for u in adjacency_list[vertex]:
            if not colors[u]:
                dfs(u, visited)

        top_sorted.append(vertex)

    def dfs_coloring(vertex, colors, current_color):
        colors[vertex] = current_color
        for u in inverse_adjacency_list[vertex]:
            if not colors[u]:
                dfs_coloring(u, colors, current_color)

    inp = sys.stdin.readlines()
    n, m = map(int, inp[0].split())
    adjacency_list = [[] for _ in range(n)]
    inverse_adjacency_list = [[] for _ in range(n)]
    for edge in inp[1:]:
        edge = list(map(int, edge.split()))
        adjacency_list[edge[0] - 1].append(edge[1] - 1)
        inverse_adjacency_list[edge[1] - 1].append(edge[0] - 1)

    visited = [0] * n
    top_sorted = []
    for vertex in range(n):
        if not visited[vertex]:
            dfs(vertex, visited)

    cnt = 0
    colors = [0] * n
    top_sorted.reverse()
    for vertex in top_sorted:
        if not colors[vertex]:
            cnt += 1
            dfs_coloring(vertex, colors, cnt)

    edges = set()
    for vertex in range(n):
        for u in adjacency_list[vertex]:
            if colors[vertex] != colors[u]:
                edges.add((colors[vertex], colors[u]))

    print(len(edges))


setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)
thread = threading.Thread(target=main)
thread.start()
