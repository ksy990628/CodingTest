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
