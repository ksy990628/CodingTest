# 내가 푼 Prim
import sys
import heapq
input = sys.stdin.readline

n = int(input().strip())
visited = [False for i in range(n+1)]
heap = [[0,1]]
edges= []
cnt, ans = 0,0
for _ in range(n):
    edges.append(list(map(int,input().split())))

while heap:
    if cnt == n:
        break
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        cnt += 1
        ans += w
        for i in range(n):
            if s-1 == i:
                continue
            heapq.heappush(heap, [edges[s-1][i],i+1])

print(ans)


# 영신이 Kruskal 코드
import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b): 
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(sys.stdin.readline().strip().split()) 
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]  
parent = [i for i in range(n)] 
edges = []  

for i in range(1, n):
    for j in range(i):
        edges.append((arr[i][j], i, j))
edges.sort()

answer = 0
for cost, a, b in edges: 
    if find_parent(parent, a) != find_parent(parent, b): 
        union(parent, a, b) 
        answer += cost

print(answer) 
