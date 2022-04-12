# 단방향만 고려했나?아무튼 그래서 아래 코드가 맞음...dfs bfs로 풀어야한다는 건 확실히 알고 있었는디
'''
import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
computers = [[] for i in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    computers[a].append(b)
    computers[b].append(a)

cnt = 0
#print(computers)


def find(num):
    for i in computers[num]:
        if i == 0:
            continue
        elif i == 1:
            computers[num][computers[num].index(i)] = 0
            computers[i][computers[i].index(num)] = 0
        else:
            computers[num][computers[num].index(i)] = 0
            if computers[i][computers[i].index(num)] != 0:
                computers[i][computers[i].index(num)] = 0
                global cnt
                cnt+=1
                #print(computers)
                find(i)
        
find(1)
#print(computers)
print(cnt)
'''


import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
computers = [[] for i in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    computers[a].append(b)
    computers[b].append(a)

discovered = []
stack = [1]

while stack:
    v = stack.pop()
    if v not in discovered:
        discovered.append(v)
        for w in computers[v]:
            stack.append(w)

print(len(discovered)-1)
