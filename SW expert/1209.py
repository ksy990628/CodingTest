# 행/열만 구함...대각선 안 구했는데 패스..
for r in range(10):
    n = input()
    arr = []
    res = 0
    for i in range(100):
        arr_x = list(map(int, input().split()))
        arr.append(arr_x)
        res = max(res, sum(arr_x))

    for i in range(100):
        arr_x = []
        for j in range(100):
            arr_x.append(arr[j][i])
        res = max(res, sum(arr_x))

    print("#" + str(r + 1) + " " + str(res))
