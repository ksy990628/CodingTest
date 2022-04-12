import sys
from collections import deque

n,m,v = map(int,sys.stdin.readline().rstrip().split())
graph = [[] for i in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()


# DFS
discovered = []
stack = deque([v])
while stack:
    cur = stack.popleft()
    if cur not in discovered:
        discovered.append(cur)
        tmp = graph[cur]
        tmp.sort(reverse=True)
        for w in tmp:
            if w not in discovered:
                stack.appendleft(w)

print(*discovered)


for i in range(n+1):
    graph[i].sort()

# BFS
discovered = []
stack = deque([v])
while stack:
    cur = stack.popleft()
    if cur not in discovered:
        discovered.append(cur)
        for w in graph[cur]:
            if w not in discovered:
                stack.append(w)

print(*discovered)
