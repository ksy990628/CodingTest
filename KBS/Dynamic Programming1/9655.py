n = int(input())
if n % 2 == 0:
    print("CY")
else:
    print("SK")

'''
# 이것두 맞음 굳이 dp 쓴건디..
import sys
n = int(sys.stdin.readline().strip())

dp = [1]* (n+1)

dp[0] = n

for i in range(1,n+1):
    if dp[i-1] - 3 < 0:
        dp[i] =  dp[i-1] - 1
    else:
        dp[i] = dp[i-1]- 3
        
    if dp[i] == 0:
        if i % 2 == 0:
            print('CY')
        else:
            print('SK')
        break
'''
        
'''        
# 이것두 맞음
import sys
n = int(sys.stdin.readline().strip())

dp = [1]* (n+1)
dp[0] = n

for i in range(1,n+1):
    dp[i] =  dp[i-1] - 1
    if dp[i] == 0:
        if i % 2 == 0:
            print('CY')
        else:
            print('SK')
        break
'''
