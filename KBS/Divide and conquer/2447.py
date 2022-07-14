import sys
n = int(sys.stdin.readline().strip())
map = [[0 for i in range(n)]for i in range(n)]

def star(n):
    global map

    if n == 3:
        map[0][:3] = map[2][:3] = [1]*3  #첫번째랑 세번째행은 *** 를 동일하게 출력
        map[1][:3] = [1,0,1] #두번째 행은 * * 를 출력
        return


    m = n // 3     # 큰 구조는 3등분으로 나눈 것, 1 == 3 , 2
    star(m)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(m):
                map[m*i+k][m*j:m*(j+1)] = map[k][:m]



star(n)
for i in map:
    for j in i:
        if j:
            print("*",end="")
        else:
            print(" ",end="")
    print()
