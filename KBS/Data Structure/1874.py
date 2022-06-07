# 수열은 1 ~ n 로 이루어져있음.
n = int(input())

s = []
op = []

count = 1

temp = True

for i in range(n):
    num = int(input())
    
    
    while count <= num:
        # 수열에 오름차순으로 아직 추가되지 않은 값 추가 
        s.append(count)
        op.append('+')
        count += 1
        
    # 값이 같은 경우에는 pop
    if s[-1] == num:
        s.pop()
        op.append('-')
        
    # 값이 다른 경우에는 불가능한 케이스
    else:
        temp = False
        
        
        
if temp == False:
    print('NO')
else:
    for i in op:
        print(i)
        
