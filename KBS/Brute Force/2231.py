import sys
n = int(sys.stdin.readline())
res = 0

def sp(n):
    if n > 100000:
        return n//100000 + n%100000//10000 + n%10000//1000 + n%1000//100 + n%100//10 + n%10

    elif n > 10000:
        return n//10000 + n%10000//1000 + n%1000//100 + n%100//10 + n%10

    elif n > 1000:
        return n//1000 + n%1000//100 + n%100//10 + n%10

    elif n > 100:
        return n//100 + n%100//10 + n%10

    elif n > 10:
        return n//10 + n%10

    else:
        return n

for i in range(n):
    if i + sp(i) == n:
        res = i
        break

print(res)
