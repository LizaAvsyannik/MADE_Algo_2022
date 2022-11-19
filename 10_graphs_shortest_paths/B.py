import sys
import heapq

MAX_DISTANCE = 4e9


def dijkstra(start):
    distances[start] = 0
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)

    while priority_queue:
        vertex = heapq.heappop(priority_queue)[1]
        visited[vertex] = True
        for u, weight in adjacency_list[vertex]:
            if visited[u]:
                continue
            if distances[u] > distances[vertex] + weight:
                distances[u] = distances[vertex] + weight
                heapq.heappush(priority_queue, (distances[u], u))


inp = sys.stdin.readlines()
n, m = map(int, inp[0].split())
adjacency_list = [[] for _ in range(n)]
for edge in inp[1:]:
    edge = list(map(int, edge.split()))
    adjacency_list[edge[0] - 1].append((edge[1] - 1, edge[2]))
    adjacency_list[edge[1] - 1].append((edge[0] - 1, edge[2]))


distances = [MAX_DISTANCE] * n
visited = [0] * n
dijkstra(0)
print(*distances)
