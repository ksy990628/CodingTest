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



# 예전에 푼 거
x = int(input())
y = x
cycle = 0

while True:
    cycle = cycle+1

    first = y//10
    second = y%10
    temp = first + second
    if temp>=10:
        temp = temp%10
    y = second*10 + temp
    if y==x:
        break        

print(cycle)
