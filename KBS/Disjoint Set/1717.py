import sys
sys.setrecursionlimit(1000000) # 재귀 깊이 제한 늘리기
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)] # 자기 자신을 부모로 갖는 n + 1개 집합

# 찾기 연산(같은 집합에 속하는지 확인하기 위한 함수)
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

# 합집합 연산(두 집합을 합치기 위한 함수)
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b: # 값이 더 작은 쪽을 부모로
        parent[b] = a
    else:
        parent[a] = b
        
for _ in range(m):
    opr, a, b = map(int, input().split())
    if opr == 0:
        union_parent(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
            
            
# 이건 왜 안됐을까?
import sys
n,m = map(int,sys.stdin.readline().strip().split())
res = [[i] for i in range(m)]

for i in range(m):
    q, a, b = map(int,sys.stdin.readline().strip().split())
    if a!=b:
        for i in range(len(res)):
            if a in res[i]:
                x = i
            if b in res[i]:
                y = i
        if x==y:
            result = 1
        else:
            result = 0
    else:
        result = 1

        
    if q == 0 and result == 0:
        res.append(res.pop(max(x,y)) + res.pop(min(x,y)))
    elif q == 1:
        if result == 1:
            print("YES")
        else:
            print("NO")
        
