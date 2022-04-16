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
