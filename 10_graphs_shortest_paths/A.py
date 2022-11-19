import sys

DELTAS = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]


def bfs(start):
    visited[start[0] * n + start[1]] = True
    queue.append(start)
    global reached_goal
    while not reached_goal:
        vertex = queue.pop(0)
        for dx, dy in DELTAS:
            nx = vertex[0] + dx
            ny = vertex[1] + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx * n + ny]:
                    visited[nx * n + ny] = True
                    queue.append((nx, ny))
                    distances[nx * n + ny] = distances[vertex[0] * n + vertex[1]] + 1
                    prev[nx * n + ny] = (vertex[0], vertex[1])
                    if nx == end[0] and ny == end[1]:
                        reached_goal = True
                        break


inp = sys.stdin.readlines()
n = int(inp[0])
start = tuple(map(lambda x: int(x) - 1, inp[1].split()))
end = tuple(map(lambda x: int(x) - 1, inp[2].split()))

visited = [0] * n ** 2
distances = [0] * n ** 2
prev = [-1] * n ** 2
queue = []
reached_goal = False

bfs(start)

print(distances[end[0] * n + end[1]] + 1)

answer = [end]
next_cell = end
for _ in range(distances[end[0] * n + end[1]]):
    next_cell = prev[next_cell[0] * n + next_cell[1]]
    answer.append(next_cell)

for edge in answer[::-1]:
    print(edge[0] + 1, edge[1] + 1)
