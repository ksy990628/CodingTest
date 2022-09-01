# https://pacific-ocean.tistory.com/332

import sys
input = sys.stdin.readline
n = int(input())
w = [0] + list(map(int, input().split()))

# 정점 연결 표시
s = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    s[a].append(b)
    s[b].append(a)

# 최댓값 표시
dp = [[0,0]for i in range(n + 1)]
# 방문 로그
visit = [False for i in range(n + 1)]
# 방문 정점 로그
num = [[[], []] for i in range(n + 1)]

def dfs(start):
    visit[start] = True
    dp[start][0] = w[start]
    num[start][0].append(start)
    for i in s[start]:
        if not visit[i]:
            dfs(i)

            # 본인 포함
            dp[start][0] += dp[i][1]
            for j in num[i][1]:
                num[start][0].append(j)

            # 본인 미포함    
            if dp[i][1] > dp[i][0]:
                dp[start][1] += dp[i][1]
                for k in num[i][1]:
                    num[start][1].append(k)
            else:
                dp[start][1] += dp[i][0]
                for k in num[i][0]:
                    num[start][1].append(k)

dfs(1)
a = []
if dp[1][0] > dp[1][1]:
    print(dp[1][0])
    a = num[1][0]
else:
    print(dp[1][1])
    a = num[1][1]
a.sort()
print(*a)
