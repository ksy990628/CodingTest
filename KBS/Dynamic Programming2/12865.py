import sys
n, k = map(int,sys.stdin.readline().rstrip().split())

stuff = [[0,0]]
bag = [[0]*(k+1) for i in range(n+1)]

for _ in range(n):
    stuff.append(list(map(int,sys.stdin.readline().rstrip().split())))


for i in range(1,n+1):
    for j in range(1,k+1):
        w = stuff[i][0]
        v = stuff[i][1]

        if j < w:
            bag[i][j] = bag[i-1][j]
        else:
            bag[i][j] = max(v + bag[i-1][j-w],bag[i-1][j])

print(bag[n][k])
