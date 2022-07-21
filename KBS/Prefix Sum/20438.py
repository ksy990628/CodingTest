import sys
input = sys.stdin.readline

n,k,q,m = map(int, input().split())

sleep = [0]*(n+3) # 조는 학생, 졸고 있으면 1
check = [0]*(n+3) # 출석한 학생, 출석 했으면 1

# 조는 학생, 출석한 학생 검토
for i in map(int, input().split()):
    sleep[i] = 1
for i in map(int, input().split()):
    if sleep[i]: 
        continue
    for j in range(i, n+3, i):
        if not sleep[j]:
            check[j] = 1

            
prefix = [check[0]]
# 각 번호 i까지 출석한 얘들 합 구하기
for i in range(1, n+3):
    prefix.append(prefix[-1]+check[i])  #prefix[-1]은 가장 마지막 원소로, 현재 출석한 최대 인원을 나타냄. 즉 현재 출석한 최대 인원 + 다음 출석한 인원

for _ in range(m):
    s, e = map(int, input().split()) # s부터 e까지 결석한 얘들
    print(e-s+1 - (prefix[e]-prefix[s-1])) # 전체 - (s부터 e까지 출석한 얘들)
