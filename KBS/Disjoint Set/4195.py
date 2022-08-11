import sys

def find(x):
    if parent[x] != x:
        y = find(parent[x])
        parent[x] = y
        x = y
    return x

def union(x,y):
    x = find(x)
    y = find(y)
    if x!=y:
        parent[y] = x
        number[x] += number[y]
    print(number[x])
        
test_case = int(sys.stdin.readline().rstrip())
for _ in range(test_case):
    n = int(sys.stdin.readline().rstrip())
    parent, number = {}, {}
    for _ in range(n):
        a,b = sys.stdin.readline().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1
        union(a,b)
