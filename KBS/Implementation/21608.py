import sys

input = sys.stdin.readline
n = int(input())
p = n * n

# 교실 반 배정
classroom = [[0] * n for _ in range(n)]

# 선호 학생 배열
like_room = [[] for _ in range(p+1)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(p):
    array = list(map(int, input().split()))
    like = array[1:]
    like_room[array[0]] = like
    
    # 제일 첫번째 학생의 경우, 무조건 [1][1] 좌석으로 배정
    if p == 0:
        classroom[1][1] = array[0]
        continue
        
        
    temp = []
    for i in range(n):
        for j in range(n):
            sum_like, sum_empty = 0, 0
            if classroom[i][j] != 0:
                continue
            # 상하좌우
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                    continue
                if classroom[nx][ny] in like:
                    sum_like += 1
                if classroom[nx][ny] == 0:
                    sum_empty += 1
            temp.append((sum_like, sum_empty, (i, j)))
    temp.sort(key=lambda x:(-x[0], -x[1], x[2]))

    classroom[temp[0][2][0]][temp[0][2][1]] = array[0]

sum_answer = 0


for i in range(n):
    for j in range(n):
        answer = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
                continue
            if classroom[nx][ny] in like_room[classroom[i][j]]:
                answer += 1
                continue
        if answer != 0:
            sum_answer += (10 ** (answer - 1))


print(sum_answer)
