T = int(input())
for test_case in range(1, T + 1):
    n,m,l = map(int,input().split())
    arr = list(map(int,input().split()))
    for _ in range(m):
        s = input().split()
        if s[0] == 'I':
            arr.insert(int(s[1]),int(s[2]))
        elif s[0] == 'D':
            del arr[int(s[1])]
        elif s[0] == 'C':
            arr[int(s[1])] = int(s[2])        
        
    ans = -1
    if len(arr)-1 >= l:
        ans = arr[l]
    res = f'#{test_case} {ans}'
    print(res)
