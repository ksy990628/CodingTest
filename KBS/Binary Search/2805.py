import sys
def input():
    return sys.stdin.readline().rstrip()

def binary_search():
    global ans
    start, end = 0, max(arr)
   
   # mid가 아니라 end가 h가 되는 거였음....
    while start <= end:
        mid = (start + end) // 2
        total_length = 0
        for i in arr:
            if i - mid >= 0:
                total_length += i - mid

        # 필요한 나무의 길이보다 자른 나무의 양이 적을 때
        if total_length < M:
            end = mid - 1
        # 필요한 나무의 길이가 충족 및 이상일 때
        else:
            start = mid + 1
    ans = end

N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
binary_search()
print(ans)
