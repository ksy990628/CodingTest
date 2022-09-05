import math
from collections import OrderedDict

def dist(x,y):
    hh = int(x[0]) - int(y[0])
    h = int(x[1]) - int(y[1])
    mm = int(x[3]) - int(y[3])
    m = int(x[4]) - int(y[4])
    return (hh*10+h)*60 + mm*10 + m

def solution(fees, records):
    # 기본 시간, 기본 요금, 단위 시간, 단위 요금 // fees[0][1][2][3]
    answer = []
    inCar = {}
    timeCar = {}
    tmpAnswer = {}
    
    for i in records:
        # IN일 경우, 기록
        if i[11:] == 'IN':
            inCar[i[6:10]] = i[0:6]
        # OUT일 경우, 시간 계산
        else:
            x = inCar.pop(i[6:10]) # IN 00:00
            time = dist(i,x)
            if i[6:10] in timeCar:
                time = timeCar[i[6:10]] + time
            timeCar[i[6:10]] = time
    
    # 나머지 출차 처리
    if len(inCar) > 0:
        for i in inCar:
            time = dist('23:59', inCar.get(i))
            if i in timeCar:
                time = timeCar[i] + time
            timeCar[i] = time
    
    # 요금 계산
    for i in timeCar:
        time = timeCar[i]
        val = fees[1]
        time -= fees[0]
        if time > 0:
            val += math.ceil(time/fees[2]) * fees[3] 
        tmpAnswer[i] = int(val)
            

    ans = OrderedDict(sorted(tmpAnswer.items()))
    for i in ans:
        answer.append(ans.get(i))
    return answer
