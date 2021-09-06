def solution(scores):
    answer = ''
    size = len(scores)
    new = []
    # 2차원 배열 뒤집기
    for i in range(size):
        ready = []
        for j in range(size):
            ready.append(scores[j][i])
        new.append(ready)
    
    # 점수 계산
    for i in range(size):
        avg = 0
        minimum = min(new[i])
        maximum = max(new[i])
        oneandonly = new[i].count(new[i][i])
        
        if (minimum==new[i][i] or maximum==new[i][i]) and oneandonly == 1:
            avg = (sum(new[i])-new[i][i]) / (size-1)
        else:
            avg = sum(new[i]) / size
        
        if avg >= 90:
            answer += 'A'
        elif avg >= 80:
            answer += 'B'
        elif avg >= 70:
            answer += 'C'
        elif avg >= 50:
            answer += 'D'
        else:
            answer += 'F'
        
    return answer
