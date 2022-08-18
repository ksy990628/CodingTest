import sys
input = sys.stdin.readline
n, m = map(int,input().split())
parent = [i for i in range(0,n+1)]
edges= []
edge_cnt , answer = 0, 0
for _ in range(m):
    src, dst, cost = map(int,input().split())
    answer += cost
    edges.append((cost, src, dst))

edges.sort()

# 부모 찾기
def get_parent(parent, a):
    if parent[a] != a:
        parent[a] = get_parent(parent, parent[a])
    return parent[a]

# 합치기
def union_parent(parent, a_p, b_p):
    # index 작은 순
    if a_p < b_p:
        parent[b_p] = a_p
    else:
        parent[a_p] = b_p

# MST 생성
for edge in edges:
    # 하나 꺼내기
    nc, ns, nd= edge
    # 사이클 탐지
    if get_parent(parent, ns) == get_parent(parent, nd):
        continue

    # 합치기
    union_parent(parent, get_parent(parent,ns), get_parent(parent, nd))
    answer -= nc
    edge_cnt += 1


flag = 1
tmp = set()
for i in range(1,n+1):
    tmp.add(parent[i])

for i in tmp:
    if get_parent(parent,i) != 1:
        flag = 0
        
    
if flag == 0:
    print(-1)
else:
    print(answer)

# 이건 시간초과난 코드
'''
import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
visited = [False]*(V+1)
Elist = [[] for _ in range(V+1)]
answer = 0
# 처음에 1번 노드 방문하기 위한 가중치값 0과 노드 1
heap = [[0, 1]]

for _ in range(E):
    s, e, w = map(int, input().split())
    Elist[s].append([w, e])
    Elist[e].append([w, s])
    answer += w


# 최소 스패닝 트리가 되기 위한 방문하는 노드 수 기록
cnt = 0
while heap:
    if cnt == V:
        break
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        answer -= w
        cnt += 1
        for i in Elist[s]:
            heapq.heappush(heap, i)

if cnt == V:
    print(answer)
else:
    print(-1)
'''
