for k in range(10):
    n = int(input())
    arr = list(map(int,input().split()))
    for _ in range(n):
        a = arr.index(max(arr))
        b = arr.index(min(arr))
        arr[a] -= 1
        arr[b] += 1
        n -= 1
    print("#" + str(k + 1) + " " + str(max(arr) - min(arr)))
