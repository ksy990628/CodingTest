if __name__ == "__main__":

    N = int(input())  # 숫자의 개수
    num_list = list(map(int, input().split()))  # 숫자 리스트

    # 2차원 dp 초기화
    dp = []
    for i in range(N - 1):
        dp.append([0 for _ in range(21)])

    dp[0][num_list[0]] = 1
    for i in range(1, N - 1):
        for j in range(21):
            if dp[i - 1][j] != 0:
                pre_value = j
                next_value = num_list[i]
                if 0 <= pre_value + next_value <= 20:
                    dp[i][pre_value + next_value] += dp[i - 1][pre_value]
                if 0 <= pre_value - next_value <= 20:
                    dp[i][pre_value - next_value] += dp[i - 1][pre_value]

    print(dp[N - 2][num_list[N - 1]])
    
