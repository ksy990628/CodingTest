import sys
n,m = map(int,sys.stdin.readline().strip().split())
arr = [(i+1) for i in range(n)]

def dfs(cnt,total,c):
    if cnt == m:
        print(*total)
    else:
        cnt += 1
        for i in range(c,len(arr)):
            total.append(arr[i])
            dfs(cnt,total,i)
            total.pop()
        

for i in arr:
    dfs(1,[i],i-1)
