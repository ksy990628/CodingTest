# 정답
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
area = [list(map(int,input().split())) for _ in range(n)]

dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = area[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for _ in range(int(input())):
    x,y,i,j = map(int,input().split())
    print(dp[i][j] - dp[x-1][j] - dp[i][y-1] + dp[x-1][y-1])

# 시간초과난 내 코드...
import sys
n, m = map(int,sys.stdin.readline().strip().split())
target = []

for i in range(n):
    #print(i)
    ipt = list(map(int,sys.stdin.readline().rstrip().split()))
    #print(ipt)
    target.append(ipt)

k = int(sys.stdin.readline().strip())
for _ in range(k):
    result = 0
    ipt = list(map(int,sys.stdin.readline().rstrip().split()))
    for i in range(0,ipt[2],ipt[0]):
        for j in range(0,ipt[3],ipt[1]):
            result += target[i][j]
    print(result)
