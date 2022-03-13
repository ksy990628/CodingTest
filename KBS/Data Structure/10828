import sys
from collections import deque

queue = deque()
n = int(input())


for i in range(n):
    st = sys.stdin.readline().rstrip()
    st = st.split(" ")
    od = st[0]
    
    if od == "push":
        num = st[1]
        queue.append(num)
        
    elif od == "pop":
        if len(queue) > 0:
            print(queue[-1])
            queue.pop()
        else:
            print(-1)
        
    elif od == "top":
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
            
    elif od == "size":
        print(len(queue))
        
    elif od == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

