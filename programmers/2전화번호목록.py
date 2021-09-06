def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(0,len(phone_book)):
        current = phone_book[i]
        current_len = len(current)
        for j in range(i+1,len(phone_book)):
            next = phone_book[j]
            if current != next[0:current_len]:
                continue
            else: 
                answer = False
                break
                    
    return answer
