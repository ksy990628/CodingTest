import sys

n = sys.stdin.readline().strip()
m = sys.stdin.readline().strip()

total = 0
for i in range(len(m)):
    total += int(m[i])
print(total)
