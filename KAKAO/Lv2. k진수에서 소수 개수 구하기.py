import math

def prime(x):
    if x == 1:
        return 0
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return 0
    return 1
        

def solution(n, k):
    answer = 0
    # 진수 변환
    trans_k = []
    while n > k:
        trans_k.append(n%k)
        n = n // k
    trans_k.append(n)
    trans_k.reverse()
    print(trans_k)
    
    # 소수 세기
    tmp = ''
    for i in range(len(trans_k)):
        if trans_k[i] != 0:
            tmp += str(trans_k[i])
            
        else: # 0을 만났을 때
            if len(tmp) == 0:
                continue
            x = int(tmp)
            answer += prime(x)
            tmp = ''
            
    if len(tmp) > 0:
        x = int(tmp)
        answer += prime(x)
        
    return answer
