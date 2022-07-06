# 예제 다 맞으나, 시간 초과
'''
n = int(sys.stdin.readline().rstrip())
arr = [[]for i in range(n+1)]
for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)
    
res = [0 for i in range(n+1)]
visited = []

def dfs(arr,i):
    stack = arr[i]
    while stack:
        if i not in visited:
            visited.append(i)
        x = stack.pop()
        if x in visited:
            continue
        res[x] = i
        dfs(arr,x)


dfs(arr,1)
for i in range(2,n+1):
    print(res[i])
'''

# 내가 푼 답안
import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline().rstrip())
arr = [[]for i in range(n+1)]
for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)
    
visited = [0 for i in range(n+1)]

def dfs(arr,i):
    stack = arr[i]
    while stack:
        if visited[i] == 0:
            visited[i] = i
        x = stack.pop()
        if visited[x] != 0:
            continue
        visited[x] = i
        dfs(arr,x)


dfs(arr,1)
for i in range(2,n+1):
    print(visited[i])


    
# 블로그 참고 답안
'''
import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline().rstrip())
arr = [[]for i in range(n+1)]
for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

res = [ 0 for i in range(n+1) ]

def dfs(n):
    for i in arr[n]:
        if res[i] == 0:
            res[i] = n
            dfs(i)


dfs(1)
for i in range(2,n+1):
    print(res[i])
'''

