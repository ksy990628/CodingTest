import sys
n = sys.stdin.readline().rstrip()
start = n
ans = 0
if int(n)< 10:
    tmp = n
    n = '0'+n
    start = n

while True:
    res = int(n[0]) + int(n[1])
    n = n[1] + str(res%10)
    ans += 1
    if n == start:
        break
    
print(ans)
