import sys
from copy import deepcopy

r,c,t = map(int,sys.stdin.readline().split())
arr = []
for _ in range(r):
    arr.append(list(map(int,sys.stdin.readline().split())))
# 북 동 남 서
dx = [0,1,0,-1]
dy = [-1,0,1,0]

airc = []

def diffuse():
    newarr = deepcopy(arr)
    for i in range(r):
        for j in range(c):
            if arr[i][j] == -1:
                airc.append([i,j])
            if arr[i][j] > 4:
                cnt = 0
                amt = arr[i][j] // 5
                for k in range(4):
                    y = j + dx[k]
                    x = i + dy[k]
                    if 0<=x<r and 0<=y<c and newarr[x][y] != -1:
                        newarr[x][y] += amt
                        cnt += 1
                newarr[i][j] -= amt*cnt
    return newarr


def cleanup(arr):
    newarr = deepcopy(arr)

    nxy2 = newarr[0][c-1]
    nxy3 = newarr[0][0]
    nxy4 = newarr[r-1][c-1]#4
    nxy5 = newarr[r-1][0] #0

    x,y = airc[0]

    nxy1 = newarr[x][c-1]
    cur = newarr[x][y+1]
    for i in range(y+1,c-1):
        nxt = newarr[x][i+1]
        if i == y+1:
            newarr[x][i] = 0
        newarr[x][i+1] = cur
        cur = nxt


    cur = newarr[x-1][c-1]  #6
    newarr[x-1][c-1] = nxy1 #5
    for i in range(x-1,-1,-1):
        nxt = newarr[i-1][c-1]
        newarr[i-1][c-1] = cur
        cur = nxt

    cur = newarr[0][c-2] #1
    newarr[0][c-2] = nxy2 #8
    for i in range(c-2,0,-1):
        nxt = newarr[0][i-1]
        newarr[0][i-1] = cur
        cur = nxt

    cur = newarr[1][0] #0
    newarr[1][0] = nxy3
    for i in range(1,x-1):
        nxt = newarr[i+1][0]
        newarr[i+1][0] = cur
        cur = nxt
#########
    x,y = airc[1]
    nxy1 = newarr[x][c-1]
 
    cur = newarr[x][y+1]
    for i in range(y+1,c-1):
        nxt = newarr[x][i+1]
        if i == y+1:
            newarr[x][i] = 0
        newarr[x][i+1] = cur
        cur = nxt

    
    cur = newarr[x+1][c-1] #8
    newarr[x+1][c-1] = nxy1 #0
    for i in range(x+1,r-1):
        nxt = newarr[i+1][c-1]
        newarr[i+1][c-1] = cur
        cur = nxt

 

    cur = newarr[r-1][c-2] 
    newarr[r-1][c-2] = nxy4 #4
    for i in range(c-2,0,-1):
        nxt = newarr[r-1][i-1]
        newarr[r-1][i-1] = cur
        cur = nxt

    cur = newarr[r-2][0] 
    newarr[r-2][0] = nxy5
    for i in range(r-2,x+1,-1):
        nxt = newarr[i-1][0]
        newarr[i-1][0] = cur
        cur = nxt

    return newarr
            
            
for _ in range(t):
    arr = diffuse()
    #print("start",arr)
    arr = cleanup(arr)
    #print("end",arr)



res = 0
for i in range(r):
    res += sum(arr[i])
print(res+2)
