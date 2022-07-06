# 메모리 초과
'''
import sys
sys.setrecursionlimit(10**6)
n,m = map(int,sys.stdin.readline().split())
arr = [[]for i in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    arr[b].append(a)

res = [ len(arr[i]) for i in range(n+1) ]

def dfs(n):
    if len(arr[n]) == 0:
        return 1
    x = 0
    for i in arr[n]:
        x += dfs(i)
    return x


for i in range(1,n+1):
    for j in arr[i]:
        res[i] += len(arr[j])
        

m = max(res)
for i in range(1,n+1):
    if res[i] == m:
        print(i, end=" ")
'''

# 블로그 답안
import sys
from collections import deque

def bfs(start):
    cnt = 1
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for v in arr[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = 1
                cnt += 1
    return cnt



n,m = map(int,sys.stdin.readline().split())
arr = [[]for i in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    arr[b].append(a)


results = []
max_cnt = 0
for i in range(1,n+1):
    cnt = bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
    results.append([i,cnt])

for i,cnt in results:
    if cnt == max_cnt:
        print(i,end=" ")
