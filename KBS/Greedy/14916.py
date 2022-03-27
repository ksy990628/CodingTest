import sys
money = int(sys.stdin.readline().strip())
cnt = 0

if money == 1 or money == 3:
    cnt = -1

else:
    cnt += money // 5
    money = money % 5

    if money % 2 == 0:
        cnt += money // 2
    else:
        cnt -= 1  # -5
        money += 5
        cnt += money // 2

print(cnt)
