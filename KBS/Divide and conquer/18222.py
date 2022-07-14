'''
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
