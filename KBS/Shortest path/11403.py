import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
graph = []

for i in range(n):
    arr = list(map(int,sys.stdin.readline().split()))
    graph.append(arr)


def dfs(i):
    visited = [0 for i in range(n)]
    q = deque([i])


    while q:
        x = q.popleft()
        for i in range(n):
            if graph[x][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = 1

    return visited


for i in range(n):
    print(*dfs(i))
