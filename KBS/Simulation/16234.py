import sys
from collections import deque

n,l,r = map(int,sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

# 북 동 남 서
dx = [-1,0,1,0]
dy = [0, 1,0,-1]

def bfs(i,j):
    q = deque()
    tmp = []
    q.append((i,j))
    tmp.append((i,j))

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
                if l<=abs(arr[x][y] - arr[nx][ny])<=r:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    tmp.append((nx,ny))
    return tmp


day = 0
while True:
    visited = [[0]*(n+1) for _ in range(n+1)]
    flag = 0
    for i in range(n):
        for j in range(n):
            # 방문한 적이 없을 때
            if visited[i][j] == 0:
                visited[i][j] = 1
                # 해당 나라를 중심으로 탐색 시작, 연합 상태인 좌표값을 return
                country = bfs(i,j)
                # 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동 시작
                if len(country) > 1:
                    flag = 1
                    number = sum([arr[x][y] for x,y in country]) // len(country)
                    for x,y in country:
                        arr[x][y] = number
    # 변화가 없었으면
    if flag == 0:
        break
    day += 1

print(day)
