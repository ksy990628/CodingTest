import sys
sys.setrecursionlimit(1000000)

n = int(sys.stdin.readline().rstrip())
arr = [i for i in range(10**6+1)]
set_size = [1 for x in range(10**6 + 1)]

def find(x):
    if arr[x] != x:
        arr[x] = find(arr[x])
    return arr[x]
    
def union(x,y):
    a = find(x)
    b = find(y)
    if a < b:
        arr[b] = a
        set_size[a] += set_size[b]
        set_size[b] = 0
    elif a > b:
        arr[a] = b
        set_size[b] += set_size[a]
        set_size[a] = 0   
    else:
        return    
    
for _ in range(n):
    a = list(sys.stdin.readline().split())
    
    if a[0] == "I":
        x = int(a[1])
        y = int(a[2])
        union(x,y)
        
    elif a[0] == "Q":
        x = int(a[1])
        y = find(x)
        print(set_size[y])
