import sys
n = int(sys.stdin.readline().rstrip())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

# 0 ~ i까지 오름차순으로 부분 수열의 원소 갯수
# [3,7,5,2,6,1,4] => dp = [1,2,2,1,3,1,2]
dp = [0 for i in range(n)]
dp[0]=1

for i in range(1,n):
    a = []
    # 0 ~ i 까지 돌면서 만약 오름차순 수열인 부분이 있을 경우, a에 그 부분 배열 저장
    for j in range(i):
        if arr[i] > arr[j]:
            a.append(dp[j])

            
    # 0 ~ i 중에 오름차순인 배열이 하나도 없을 때
    if not a:
        dp[i] = 1
    # 0 ~ i까지 오름차순인 배열이 하나라도 있을 때
    else:
        dp[i] = max(a) + 1

print(n-max(dp))
