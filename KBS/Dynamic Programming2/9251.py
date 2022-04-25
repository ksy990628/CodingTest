# https://myjamong.tistory.com/317
import sys
s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

l1 = len(s1)
l2 = len(s2)

cache = [0]*l2

for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < cache[j]:
            cnt = cache[j]
        elif s1[i] == s2[j]:
            cache[j] = cnt+1

print(max(cache))
