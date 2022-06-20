import sys
n,k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

st, end = 0,0
dp = [0]*(100001)
res = 1

while end < n:
    if dp[arr[end]] < k:
        dp[arr[end]] += 1
        end += 1
    else:
        dp[arr[st]] -= 1
        st += 1

    res = max(res,end-st)

print(res)
