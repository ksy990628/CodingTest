import sys
import heapq
V = int(sys.stdin.readline().rstrip())
E = int(sys.stdin.readline().rstrip())
visited = [False]*(V+1)
Elist = [[] for _ in range(V+1)]
heap = [[0, 1]]

for _ in range(E):
    s, e, w = map(int,sys.stdin.readline().split())
    Elist[s].append([w, e])
    Elist[e].append([w, s])
 
answer = 0
cnt = 0
while heap:
    if cnt == V:
        break
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        answer += w
        cnt += 1
        for i in Elist[s]:
            heapq.heappush(heap, i)
 
print(answer)
