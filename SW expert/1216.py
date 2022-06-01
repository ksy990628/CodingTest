def check(lst):
    for i in range(len(lst)//2):
        if lst[i] != lst[-i-1]:
            return False
    return True

if __name__ == '__main__':
    for _ in range(10):
        t = int(input())
        arr = [list(input()) for _ in range(100)]
        # arr2는 전치 행렬(행과 열을 바꾼 행렬)
        arr2 = list(zip(*arr))
        # 길이가 1이어도 회문, 따라서 최소 결과값은 1
        res = 1

        for i in range(100,1,-1):
            if res >= i:
                break
            for idx in range(100-i+1):
                if res == i:
                    break
                for lst, lst2 in zip(arr,arr2):
                    if check(lst[idx:idx+i]) or check(lst2[idx:idx+i]):
                        res = i
                        break
        print("#" + str(t) + " " + str(res))
        
