import sys
n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()


ans = []
for x in arr:
    # arr의 값들 중 몇 개의 로프에 따라 들 수 있는 무게 저장
    # arr = 1 8 9 이면, ans 에는 1*3, 8*2, 9*1 이 저장
    ans.append(x*n)
    n -= 1
# 그 중 최고로 많이 들 수 있는 무게 출력    
print(max(ans))
