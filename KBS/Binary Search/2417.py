import sys
ipt = int(sys.stdin.readline().strip())

s = 0
e = ipt

while True:
    mid = (s+e)//2
    if mid**2 > ipt:
        e = mid-1
    elif mid**2 < ipt:
        s = mid+1

print(s)
