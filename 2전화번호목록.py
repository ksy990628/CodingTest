def solution(phone_book):
    answer = True
    min = 0
    for i in range(phone_book):
        for j in range(i+1,len(phone_book)):
            if (i[0] == j):
                answer = False
            
        
    return answer