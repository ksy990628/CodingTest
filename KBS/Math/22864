import sys
a,b,c,d = map(int,sys.stdin.readline().rstrip().split())
#print(a,b,c,d)

exp = 0
work = 0
for i in range(24):
    if exp + a <= d:
        work += b
        exp += a
    else:
        exp -= c
        if exp < 0:
            exp = 0
    #print(exp)

print(work)
