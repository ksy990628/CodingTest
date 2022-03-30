import sys
n = int(sys.stdin.readline().strip())

for _ in range(n):
    res = 0
    T = int(sys.stdin.readline().strip())
    coins = list(map(int,sys.stdin.readline().strip().split()))
    target = int(sys.stdin.readline().strip())

    dp = [0 for i in range(target+1)]
    dp[0] = 1

    for i in coins:
        for j in range(1,target+1):
            if j - i >= 0:
                dp[j] += dp[j-i]


    print(dp[target])
