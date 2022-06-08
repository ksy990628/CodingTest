import sys
k = int(input())
tree = [[]for i in range(k)]


def binaryTree(arr,x):
    mid = len(arr)//2
    tree[x].append(arr[mid])
    if len(arr)>1:
        binaryTree(arr[:mid],x+1)
        binaryTree(arr[mid+1:],x+1)
    else:
        return


arr = list(map(int, sys.stdin.readline().split()))
binaryTree(arr,0)

for i in range(k):
  print(*tree[i])
