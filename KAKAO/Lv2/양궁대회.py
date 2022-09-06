# https://velog.io/@hygge/Python-프로그래머스-양궁대회-BFS
from collections import deque

def bfs(n,info):
    res = []
    q = deque([(0,[0 for i in range(11)])])
    maxGap = 0
    
    while q:
        focus, arrow = q.popleft()
        # 1 종료 조건 : 화살 다 썼을 때
        if sum(arrow) == n:
            ryan, apeach = 0,0
            for i in range(11):
                if info[i] != 0 or arrow[i] != 0:
                    if info[i] >= arrow[i]:
                        apeach += 10-i
                    else:
                        ryan += 10-i
            if ryan > apeach:
                gap = ryan - apeach
                if maxGap > gap:
                    continue
                else: #maxGap < gap
                    maxGap = gap
                    res.clear()
                res.append(arrow)
                
        # 2 종료 조건 : 화살 초과해서 썼을 때 
        elif sum(arrow) > n:
            continue
        # 3 종료 조건 : 한 바퀴 돌았는데 화살 남았을 때
        elif focus == 10:
            tmp = arrow.copy()
            tmp[focus] = n-sum(arrow)
            q.append((-1,tmp))
        # 종료 조건이 아닐 때
        else:
            # 어피치보다 한 발 더 쏘기
            tmp = arrow.copy()
            tmp[focus] = info[focus]+1
            q.append((focus+1,tmp))
            # 0발을 쏴서 화살 아끼기
            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus+1,tmp2))
    return res
    
def solution(n, info):
    answer = bfs(n,info)
    
    if not answer:
        return [-1]
    elif len(answer)==1:
        return answer[0]
    else:
        return answer[-1]
    
