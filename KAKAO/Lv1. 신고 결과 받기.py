def solution(id_list, report, k):
    answer = [set() for _ in range(len(id_list))]
    for i in report:
        tmp = i.split()
        # 고발당한 자의 값에 고발한 자의 이름 표기
        answer[id_list.index(tmp[1])].add(tmp[0])
    
    q = []
    for i in range(len(id_list)):
        # 정지된 아이디
        if len(answer[i]) >= k:
            q.append(i)
    
    ans = [0 for _ in range(len(id_list))]
    for i in q:
        for j in answer[i]:
            ans[id_list.index(j)] += 1

    return ans
