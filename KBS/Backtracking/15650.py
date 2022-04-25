import sys
n,m = map(int,sys.stdin.readline().strip().split())
arr = [(i+1) for i in range(n)]


def dfs(cnt,total,i):
    if cnt == m:
        print(*total)
    else:
        cnt += 1
        for i in range(i+1,len(arr)):
            if arr[i] not in total:
                total.append(arr[i])
                dfs(cnt,total,i)
                total.pop()
        

for i in range(n):
    dfs(1,[arr[i]],i)
