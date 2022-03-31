import sys
n = int(sys.stdin.readline().strip())

dp = [1]* (n+1)

dp[0] = n

for i in range(1,n+1):
    if dp[i-1] - 3 < 0:
        dp[i] =  dp[i-1] - 1
    else:
        dp[i] = dp[i-1]- 3
        
    if dp[i] == 0:
        if i % 2 == 0:
            print('CY')
        else:
            print('SK')
        break
