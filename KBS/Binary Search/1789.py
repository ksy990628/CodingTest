# 그냥 막 푼 것
import sys
n = int(sys.stdin.readline().strip())
total = 0
s = 1

while True:
    total += s
    if total > n:
        print(s-1)
        break
    s += 1
    
    
# 정석?
import sys
s = int(sys.stdin.readline().strip())
n = 1
while n * (n + 1) / 2 <= s:
    n += 1
print(n - 1)
