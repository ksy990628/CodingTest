# 민정이가 준 코드....아직도 문제도 이해 못하고, 

import sys
input = sys.stdin.readline

def dfs(x):
    visited[x] = 1
    dp[x][1] = x
    for y in b:
        for nxt in (x - y, x + y):
            if nxt in visited and visited[nxt] == 0:
                dfs(nxt)
                dp[x][0] += max(dp[nxt][0], dp[nxt][1])
                dp[x][1] += dp[nxt][0]


n, m = map(int, input().split())
a = [int(input()) for i in range(n)]
a.sort()
visited = {x: 0 for x in a}
dp = {x: [0, 0] for x in a}
b = [int(input()) for i in range(m)]

start = a[0]
dfs(start)
print(max(dp[start][0], dp[start][1]))
