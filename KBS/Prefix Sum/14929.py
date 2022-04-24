import sys
n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().strip().split()))
sum_arr = [0]
result = 0

for i in range(1,n):
    sum_arr.append(sum_arr[i-1]+arr[i])

for i in range(n):
    result += arr[i]*(sum_arr[n-1]-sum_arr[i])



print(result)
