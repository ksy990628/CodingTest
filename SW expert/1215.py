for r in range(10):
    n = int(input())
    arr = []
    res = 0
    for i in range(8):
        arr_x = list(input())
        arr_x.append('\n')
        arr.append(arr_x)
        for j in range(len(arr_x) - n):
            tmp = arr_x[j:j + n]
            check = True
            for k in range(n // 2):
                if tmp[k] != tmp[n - k - 1]:
                    check = False
            if check == True:
                res += 1

    for i in range(8):
        for j in range(8 - n + 1):
            tmp = []
            for k in range(n):
                tmp.append(arr[j + k][i])
            check = True
            for k in range(n // 2):
                if tmp[k] != tmp[n - k - 1]:
                    check = False
            if check == True:
                res += 1

    print("#" + str(r + 1) + " " + str(res))
