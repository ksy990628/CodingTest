import sys
n,m = map(int,sys.stdin.readline().strip().split())
arr = [(i+1) for i in range(n)]

def dfs(cnt,total):
    if cnt == m:
        print(*total)
    else:
        cnt += 1
        for i in arr:
            if i not in total:
                total.append(i)
                dfs(cnt,total)
                total.pop()
        

for i in arr:
    dfs(1,[i])
