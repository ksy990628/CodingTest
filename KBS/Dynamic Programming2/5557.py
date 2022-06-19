import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().rstrip().split()))

# 0부터 20까지의 수만 가능
dp = [[0]*21 for i in range(n)]
# 첫번째 수에 대해 1로 초기화
dp[0][arr[0]] = 1

for i in range(1,n-1):
    for j in range(21):
        # 만약 전에 값이 있던 경우
        if dp[i-1][j] != 0:
            pre = j
            nxt = arr[i]
            # 조건에 부합하는 지 확인
            if 0 <= pre + nxt <= 20:
                dp[i][pre+nxt] += dp[i-1][pre]
            if 0 <= pre - nxt <= 20:
                dp[i][pre-nxt] += dp[i-1][pre]

print(dp[n-2][arr[n-1]])
