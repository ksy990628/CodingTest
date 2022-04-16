import sys
n,m = map(int,sys.stdin.readline().strip().split())
cards = list(map(int,sys.stdin.readline().strip().split()))
cards.sort(reverse=True)

# if the card number is bigger than m, delete it
i = 0
while True:
    if cards[i] > m:
        cards.pop(i)
    else:
        break

maxValue = 0

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            total = cards[i]+cards[j]+cards[k]
            if maxValue < total <= m:
                maxValue = total
print(maxValue)

