#  최장 경로
def dfs(i,count):
    global res
    for j in range(1, n + 1):
        if not visited[j] and arr[i][j]:
            visited[j] = 1
            dfs(j, count + 1)
            visited[j] = 0
    if count > res:
        res = count


if __name__ == '__main__':
    t = int(input())
    for r in range(t):
        res = 0
        n, m = map(int, input().split())
        arr =[[0] * (n + 1) for _ in range(n + 1)]
        visited = [0] * (n + 1)
        for i in range(m):
            x, y = map(int, input().split())
            arr[x][y] = 1
            arr[y][x] = 1

        for i in range(1,n+1):
            visited[i] = 1
            dfs(i, 1)
            visited[i] = 0
        print("#" + str(r + 1) + " " + str(res))
        
