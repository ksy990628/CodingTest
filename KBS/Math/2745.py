import sys
import string
a,b = map(str,sys.stdin.readline().split())
c = list(a)
d = int(b)

unit = 0
ans = 0

alphabet = string.ascii_uppercase

for i in range(len(c)-1,-1,-1):
    if c[i] in alphabet:
        x = alphabet.index(c[i]) + 10
    else:
        x = int(c[i])
    ans += (d**unit*x)
    unit += 1

print(ans)
