n = int(input())
d = list(map(int,input().split()))
gas = list(map(int,input().split()))
total = d[0]*gas[0]
min_gas = gas[0]

# 가격이 제일 싼 경우
if min(gas) == gas[0]:
    total += gas[0]*(sum(d)-d[0])

else: # min(gas) !=d[0]
    for i in range(1,len(gas)-1):
        if gas[i] < min_gas:
            min_gas = gas[i]
        total += min_gas*d[i]

print(total)
