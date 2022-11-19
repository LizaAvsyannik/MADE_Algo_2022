import sys
from sys import setrecursionlimit
import threading

MAX_DISTANCE = 5e18


def main():
    def ford_bellman(distances, n_verticies):
        for _ in range(n_verticies):
            for vertex in range(n_verticies):
                if distances[vertex] < MAX_DISTANCE:
                    for u, weight in adjacency_list[vertex]:
                        if distances[u] > distances[vertex] + weight:
                            distances[u] = max(-MAX_DISTANCE, distances[vertex] + weight)

        return find_cycles(distances, n_verticies)

    def find_cycles(distances, n_verticies):
        no_shortest_path = [0] * n_verticies
        for vertex in range(n_verticies):
            if distances[vertex] < MAX_DISTANCE:
                for u, weight in adjacency_list[vertex]:
                    if distances[u] > distances[vertex] + weight:
                        if not no_shortest_path[vertex]:
                            dfs(u, no_shortest_path)

        return no_shortest_path

    def dfs(vertex, visited):
        visited[vertex] = True
        for u in adjacency_list[vertex]:
            if not visited[u[0]]:
                dfs(u[0], visited)

    inp = sys.stdin.readlines()
    n, m, s = map(int, inp[0].split())
    adjacency_list = [[] for _ in range(n)]
    for edge in inp[1:]:
        edge = list(map(int, edge.split()))
        adjacency_list[edge[0] - 1].append((edge[1] - 1, edge[2]))

    distances = [MAX_DISTANCE] * n
    distances[s - 1] = 0

    no_shortest_path = ford_bellman(distances, n)

    for vertex in range(n):
        if distances[vertex] == MAX_DISTANCE:
            print('*')
        elif no_shortest_path[vertex]:
            print('-')
        else:
            print(distances[vertex])


setrecursionlimit(10 ** 9)
threading.stack_size(2 ** 26)
thread = threading.Thread(target=main)
thread.start()
