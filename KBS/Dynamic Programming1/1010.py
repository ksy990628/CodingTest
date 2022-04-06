def factorial(n):
    num = 1
    for i in range(1,n+1):
        num *= i
    return num

import sys
t = int(sys.stdin.readline().strip())

for _ in range(t):
    n, m = map(int,sys.stdin.readline().rstrip().split())
    bridge = factorial(m) // (factorial(n)*factorial(m-n))
    print(bridge)
   
