# 참고 블로그
# https://woongsin94.tistory.com/405

import sys
input = sys.stdin.readline
n, m = map(int,input().split())
parent = [i for i in range(0,n+1)]
edges= []
edge_cnt , answer = 0, 0
for _ in range(m):
    src, dst, cost = map(int,input().split())
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
    # 다채우면 종료, 제일 cost가 많이 나가는 간선 하나를 제외
    if edge_cnt + 2 == n:
        break

    # 하나 꺼내기
    nc, ns, nd= edge
    # 사이클 탐지
    if get_parent(parent, ns) == get_parent(parent, nd):
        continue

    # 합치기
    union_parent(parent, get_parent(parent,ns), get_parent(parent, nd))
    answer += nc
    edge_cnt += 1

print(answer)
