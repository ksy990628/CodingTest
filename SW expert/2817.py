def dfs(idx,sum):
    global cnt
    if idx >= n:
        return
    sum += arr[idx]
    if sum == k:
        cnt += 1
    dfs(idx+1,sum-arr[idx])
    dfs(idx+1,sum)

t = int(input())
for r in range(t):
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    cnt = 0
    dfs(0,0)
    print("#" + str(r + 1) + " " + str(cnt))
