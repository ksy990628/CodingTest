# datetime.time 쓰려고 했는데 와 00:00:00 - 00:00:00 케이스에는 24:00:00을 간과함....

import sys
from datetime import time

current_time = sys.stdin.readline().strip().split(":")
throw_time = sys.stdin.readline().strip().split(":")
ttt = []

for i in range(3):
    ttt.append(int(throw_time[i]) - int(current_time[i]))

for i in range(2,-1,-1):
    if i!=0 and ttt[i] < 0:
        ttt[i] += 60
        ttt[i-1] -= 1
    if i == 0 and ttt[i] < 0:
        ttt[i]+=24

if ttt[0] == 0 and ttt[1] == 0 and ttt[2] == 0:
    print("24:00:00")

else:
    print(str(time(ttt[0],ttt[1],ttt[2])))
