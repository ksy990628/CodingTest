import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().strip())
nArr = list(map(int,sys.stdin.readline().split()))
nArr.sort()
m = int(sys.stdin.readline().strip())
mArr = list(map(int,sys.stdin.readline().split()))

res = []

def binary_search(x,start,end):
    i = (start + end) // 2
    if x == nArr[i]:
        res.append(1)
        return
    elif x < nArr[i] and start <= i-1 :
        binary_search(x,start,i-1)
        return 
    elif x > nArr[i] and end >= i+1:
        binary_search(x,i+1,end)
        return
    else:
        res.append(0)
        return


for i in range(m):
    binary_search(mArr[i],0,n-1)

print(*res)
