import heapq
lower = []
higher = []

def putInMaxHeap(val):
    heapq.heappush(lower,-1*val)

def getFromMaxHeap():
    val = heapq.heappop(lower)
    return -1*val

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int,input().split())
    ans = 0
    lower.clear()
    higher.clear()
    for _ in range(n):
        a,b = map(int,input().split())
        if a < m:
            putInMaxHeap(a)
        else:
            heapq.heappush(higher,a)

        if b < m:
            putInMaxHeap(b)
        else:
            heapq.heappush(higher,b)

        if len(lower) != len(higher):
            if len(lower) > len(higher):
                heapq.heappush(higher,m)
                m = getFromMaxHeap()
            elif len(lower) < len(higher):
                putInMaxHeap(m)
                m = heapq.heappop(higher)

        ans = (ans+m)%20171109        
    print("#"+str(test_case)+" "+str(ans))
