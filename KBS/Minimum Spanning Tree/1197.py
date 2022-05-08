import sys
import heapq
input = sys.stdin.readline

# 노드, 간선
V, E = map(int, input().split())
# 방문했나?
visited = [False]*(V+1)
# 기록
Elist = [[] for _ in range(V+1)]
# 처음에 1번 노드 방문하기 위한 가중치값 0과 노드 1
heap = [[0, 1]]

for _ in range(E):
    s, e, w = map(int, input().split())
    Elist[s].append([w, e])
    Elist[e].append([w, s])

# 최소 스패닝 트리 최종 가중치값
answer = 0
# 최소 스패닝 트리가 되기 위한 방문하는 노드 수 기록
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
