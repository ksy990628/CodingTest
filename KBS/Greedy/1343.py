import sys
board = sys.stdin.readline().strip()

board_list = board.split('.')
ans = ''

for i in board_list:
    countX = i.count('X')
    
    if countX % 2 != 0 :
        print(-1)
        ans = 0
        break
    else:
        ans += ('AAAA'*(countX//4))
        countX -= 4*(countX // 4)
        ans += 'BB'*(countX //2)
            
        ans += '.'


if ans != 0:
    print(ans[:-1])
