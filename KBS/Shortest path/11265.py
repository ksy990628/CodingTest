# https://velog.io/@hygge/Python-백준-11265-끝나지-않는-파티-Floyd-Warshall
import sys
n,m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k]+graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    if graph[a-1][b-1] <= c :
        print('Enjoy other party')
    else:
        print('Stay here')

