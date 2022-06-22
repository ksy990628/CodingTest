import sys
input = sys.stdin.readline
n, k = map(int, input().split())
lst = list(map(int, input().split()))
    
cnt = 0                 # 현재 부분 수열 중 홀수의 갯수
start, end = 0, 0
size, size_max = 0, 0   # 현재 부분수열의 길이, 가장 긴 짝수 부분수열의 길이
flag = 1                # end가 n-1이 되면 더이상 end += 1 작업을 할 수 없도록 막기 위한 플래

for start in range(n):
    while cnt <= k and flag:
        if lst[end] % 2:
            if cnt == k:
                break
            cnt += 1
        size += 1
        if end == n - 1:
            flag = 0
            break
        end += 1
        
    if size_max < size - cnt:
        size_max = size - cnt
        
    if lst[start] % 2:
        cnt -= 1
        
    size -= 1

print(size_max)
