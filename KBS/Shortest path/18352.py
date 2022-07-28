import sys
from collections import deque
n, m, k,x = map(int,sys.stdin.readline().split())

city = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    city[a].append(b)
distance = [0]*(n+1)
visited = [False]*(n+1)


def bfs(x):
    ans = []
    q = deque([x])
    visited[x] = True
    distance[x] = 0

    while q:
        now = q.popleft()
        for i in city[now]:
            if not visited[i]:
                visited[i] =True
            q.append(i)
            distance[i] = distance[now] + 1
            if distance[i] == k:
                ans.append(i)

    
    if ans:
        ans.sort()
        for i in ans:
            print(i)
    else:
        print(-1)

bfs(x)
