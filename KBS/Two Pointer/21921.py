import sys
n,x = map(int,sys.stdin.readline().rstrip().split())
visitor = list(map(int,sys.stdin.readline().rstrip().split()))

if sum(visitor) == 0:
    print("SAD")

else:
    tmp = sum(visitor[:x])
    count_max = 1
    max_X = tmp
    
    for i in range(x,n):
        tmp += visitor[i]
        tmp -= visitor[i-x]
        if tmp > max_X:
            max_X = tmp
            count_max = 1
        elif tmp == max_X:
            count_max += 1
                
    print(max_X)
    print(count_max)

    
    # 그리구 시간초과난 코드..
    '''
    import sys
n,x = map(int,sys.stdin.readline().rstrip().split())
visitor = list(map(int,sys.stdin.readline().rstrip().split()))

max_X = 0
count_max = 0

if sum(visitor) == 0:
    print("SAD")

else:
    for i in range(0,n-x+1):
        tmp = sum(visitor[i:i+x])
        
        if tmp > max_X:
            max_X = tmp
            count_max = 1
        elif max_X == tmp:
            count_max += 1

    
    print(max_X)
    print(count_max)
    '''
