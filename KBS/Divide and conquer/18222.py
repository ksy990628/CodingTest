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

    x = int(log(idx,2))  #float type, idx와 가장 가까운 2의 제곱을 찾음

    val = 0
    while x > 0:
        if idx >= 2 ** x:
            val ^= 1       # 결과 0과 1중 하나를 구분
            idx %= 2 ** x. # idx와 가장 가끼운 2의 제곱 수와의 차이
        x -= 1

    return [val, val ^ 1][idx == 1]. # 배열 [0,1] 또는 [1,0]에서 1번 인덱스 값을 반환


k = int(stdin.readline())
print(thue_morse(k - 1))
