import sys
sugar = int(sys.stdin.readline().strip())
cnt = 0

if sugar == 4 or sugar == 7:
    cnt = -1


else:
    cnt += sugar // 5
    sugar = sugar % 5

    while sugar > 0:
        if sugar % 3 == 0:
            cnt += sugar // 3
            sugar = 0
        else:
            cnt -= 1
            sugar += 5
    
print(cnt)
