import sys
n = int(sys.stdin.readline().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().strip().split())))

def pulling(arr,n):
    if n == 1:
        return arr[0][0]
    
    new_arr = [[]for _ in range(n//2)]
    
    for i in range(0,n,2):
        for j in range(0,n,2):
            li = [arr[i][j],arr[i][j+1],arr[i+1][j],arr[i+1][j+1]]
            li.sort()
            # new_arr[i//2] 에 저장해줘야한다는 부분을 생각 못함
            new_arr[i//2].append(li[2])
    # 재귀형식으로 다시 
    return pulling(new_arr,n//2)

print(pulling(arr,n))
        
