def solution(new_id):
    # 길이 3~15자, 알파벳소문자, 숫자, -, _, . 
    # .은 중간에만 사용 가능 및 연속 불가
    answer = ''
    # 1단계
    id2 = new_id.lower()
    # 2단계
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    example = ['0','1','2','3','4','5','6','7','8','9','.','-','_']
    for i in id2:
        if i in example or i in alpha:
            answer += i
    # 3단계
    id3 = answer
    answer = ''
    cnt = 0
    for i in range(len(id3)-1):
        if id3[i]=='.':
            if id3[i+1] =='.':
                continue
        answer += id3[i]
    answer += id3[-1]
    # 4단계
    id4 = answer
    answer =''
    for i in range(len(id4)):
        if i == 0 and id4[i] =='.':
            continue
        if i == len(id4)-1 and id4[i]=='.':
            continue
        answer += id4[i]
    # 5단계
    if answer=='':
        answer +='a'
    # 6단계
    id6 = list(answer[:15])
    answer =''
    if id6[-1] == '.':
        id6.pop()
    for i in id6:
        answer += i
    # 7단계
    if len(answer) <= 2:
        t = answer[-1]
    while len(answer) <3:
        answer+=t
    return answer
