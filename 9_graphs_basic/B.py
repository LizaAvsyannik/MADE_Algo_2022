import sys
from sys import setrecursionlimit
import threading
from collections import defaultdict


def main():
    def dfs(vertex, visited, depth=1):
        visited[vertex] = True

        nonlocal max_depth
        max_depth = max(max_depth, depth)
        depth += 1

        for u in adjacency_list[vertex]:
            if not visited[u]:
                dfs(u, visited, depth)

    inp = sys.stdin.readlines()
    adjacency_list = defaultdict(list)
    polycarp_name = ''
    for edge in inp[1:]:
        edge = edge.strip().split()
        if not polycarp_name:
            polycarp_name = edge[2].lower()
        adjacency_list[edge[2].lower()].append(edge[0].lower())

    visited = defaultdict(lambda: 0)
    max_depth = 0
    dfs(polycarp_name, visited)

    print(max_depth)


setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)
thread = threading.Thread(target=main)
thread.start()
