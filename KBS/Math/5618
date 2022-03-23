def GCD(a,b):
    if a<b:
        tmp = a
        a = b
        b = tmp
    while b!=0:
        tmp = a%b
        a = b
        b = tmp
    return a

import sys
n = int(sys.stdin.readline().rstrip())

arr = list(map(int,sys.stdin.readline().rstrip().split()))
gcd = arr[0]
for i in range(1,n):
    gcd = GCD(gcd,arr[i])




# 왜 x * x를 하는가? gcd 값은 x * x 보다 크면 안됨! 그래서 일부러 x * x를 하는 것!
outputs = list()
x = 1
while x * x <= gcd:
    if gcd % x == 0:
        outputs.append(x)
        if x * x != gcd:
            outputs.append(gcd // x)
    x += 1

outputs.sort()
print(*outputs)
