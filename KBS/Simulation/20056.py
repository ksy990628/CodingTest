import sys
n,m, k = map(int,sys.stdin.readline().split())
fireballs = []
for _ in range(m):
    x,y,m,s,d = list(map(int,sys.stdin.readline().split()))
    fireballs.append([x-1,y-1,m,s,d])
# 방향 : 0 1 2 3 4 5 6 7
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0, 1, 1,1,0,-1,-1,-1]

# 지도에 표시
MAP = [[[] for _ in range(n)] for _ in range(n)]




for _ in range(k):
    while fireballs:
        x,y,m,s,d = fireballs.pop(0)
        nx = (x+dx[d]*s)%n
        ny = (y+dy[d]*s)%n
        MAP[nx][ny].append([m,s,d])

    # 2개 이상 -> 4개의 파이어볼로 쪼개게 됨
    for r in range(n):
        for c in range(n):
            if len(MAP[r][c]) > 1:
                M, S, odd, even, cnt = 0,0,0,0,len(MAP[r][c])
                while MAP[r][c]:
                    m,s,d = MAP[r][c].pop(0)
                    M += m
                    S += s
                    if d % 2 == 0:
                        even += 1
                    else:
                        odd += 1
                        
                if even == cnt or odd == cnt:
                    nd = [0,2,4,6]
                else:
                    nd =[1,3,5,7]
                        
                if M // 5:
                    for dk in nd:
                        fireballs.append([r,c,M//5,S//cnt,dk])
                            
            if len(MAP[r][c]) == 1:
                fireballs.append([r,c]+MAP[r][c].pop())
    
print(sum([f[2] for f in fireballs]))
