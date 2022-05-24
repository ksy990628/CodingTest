if __name__ == '__main__':
    t = int(input())
    for r in range(t):
        n = int(input())
        res = 0
        for i in range(n//2+1):
            arr = list(map(str, input()))
            tmp = arr[n//2-i:n//2+i+1]
            for k in tmp:
                res += int(k)
        for i in range(n-(n//2+1)):
            arr = list(map(str, input()))
            tmp = arr[i+1:n-i-1]
            for k in tmp:
                res += int(k)

        print("#"+str(r+1)+" "+str(res))
