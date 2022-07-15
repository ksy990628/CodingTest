'''
점화식 방법1
to = 0
t2n = tn
t2n+1 = 1-tn
'''

k = int(input())
def recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n%2:
        return 1-recursive(n//2)
    else:
        return recursive(n//2)
print(recursive(k-1))




# 방법 2
from sys import stdin
from math import log


def thue_morse(idx: int) -> int:
    if idx == 0:
        return 0

    x = int(log(idx,2))  #float type

    val = 0
    while x > 0:
        if idx >= 2 ** x:
            val ^= 1
            idx %= 2 ** x
        x -= 1

    return [val, val ^ 1][idx == 1]


k = int(stdin.readline())
print(thue_morse(k - 1))
