import sys
import heapq

v,e = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline().rstrip())
path = [[] for i in range(v+1)]
heap = []
dp = [float('INF') for i in range(v+1)]


def dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap,(0,start))

    while heap:
        # 무게, V
        wei, now = heapq.heappop(heap)

        if dp[now] < wei:
            continue

        for w, next_node in path[now]:
            next_wei = w + wei
            if next_wei < dp[next_node]:
                dp[next_node] = next_wei
                heapq.heappush(heap,(next_wei,next_node))
                   

for _ in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    path[a].append((c,b))

dijkstra(start)
for i in range(1,v+1):
    print("INF" if dp[i] == float('INF') else dp[i])
