def solution(price, money, count):
    sum = 0
    for i in range(count):
        sum += price*(i+1)
    
    answer = sum - money
    if answer <= 0:
        answer = 0
    
    return answer