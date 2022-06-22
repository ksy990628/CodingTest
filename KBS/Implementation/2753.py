def year(n):
    if n%4 == 0 and (n%100 != 0 or n%400 == 0):
        return 1
    return 0
    

import sys
n = int(sys.stdin.readline().rstrip())

print(year(n))
