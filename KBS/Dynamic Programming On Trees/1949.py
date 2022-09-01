import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input().rstrip())
people = [0] + list(map(int,input().split()))
s = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
#dp[i][0]은 정점 포함했을 때 최댓값, dp[i][1]은 미포함 최댓값
dp = [[0,0] for i in range(n+1)]

for _ in range(n-1):
    a, b = map(int,input().split())
    s[a].append(b)
    s[b].append(a)

def dfs(start):
    visited[start] = 1
    dp[start][0] = people[start]
    
    for i in s[start]:
        if visited[i] == 0:
            dfs(i)
            dp[start][0] += dp[i][1]
            dp[start][1] += max(dp[i][0],dp[i][1])


dfs(1)
print(max(dp[1][0],dp[1][1]))
