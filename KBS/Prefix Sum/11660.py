# 누적합 , DP
# https://castlerain.tistory.com/100

import sys
n,m = map(int,sys.stdin.readline().split())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
sum_data = [[0]*(n+1) for i in range(n+1)]

# 누적합
for i in range(1,n+1):
    for j in range(1,n+1):
        sum_data[i][j] = sum_data[i][j-1] + sum_data[i-1][j] - sum_data[i-1][j-1]+ data[i-1][j-1]


for _ in range(m):
    x1, y1, x2, y2 = map(int,sys.stdin.readline().split())
    print(sum_data[x2][y2]-sum_data[x1-1][y2]-sum_data[x2][y1-1]+sum_data[x1-1][y1-1])
