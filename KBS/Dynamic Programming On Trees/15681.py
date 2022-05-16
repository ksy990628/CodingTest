import sys
sys.setrecursionlimit(10**9)

def countTree(x):
    count[x]=1
    for i in arr[x]:
        if not count[i]:
            countTree(i)
            count[x]+=count[i]
        



n,r,q = map(int,sys.stdin.readline().rstrip().split())
arr = [[]for _ in range(n+1)]
count = [0]*(n+1)
result = 0

for _ in range(n-1):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)

countTree(r)

for _ in range(q):
    c = int(sys.stdin.readline().rstrip())
    print(count[c])
