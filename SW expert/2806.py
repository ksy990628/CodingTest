def dfs(queen, n, row):
    count = 0

    # 마지막 행인지 확인
    if n == row:
        return 1

    # 가로 자리 선정
    for col in range(n):
        queen[row] = col

        for x in range(row):
            # 세로로 겹치면 안됨
            if queen[x] == queen[row]:
                break

            # 대각선으로 겹치면 안됨, 1의 차이가 나면 대각선인 관계인 것임
            if abs(queen[x] - queen[row]) == (row - x):
                break
        else:
            count += dfs(queen, n, row + 1)

    return count

if __name__ == '__main__':
    t = int(input())
    for r in range(1, t+1):
        n = int(input())
        nQueen = [0 for i in range(n)]
        res = dfs(nQueen,n,0)
        print("#"+str(r)+" "+str(res))
