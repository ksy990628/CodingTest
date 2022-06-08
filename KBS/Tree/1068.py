# 트리
import sys

def dfs(removed_node):
    global arr
    arr[removed_node] = -2
    # 부모 노드가 누구인지가 해당 노드의 값이므로, 부모 노드만 찾아서 없애버리면 됨
    for i in range(len(arr)):
        if arr[i] == removed_node:
            dfs(i)

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
removed_node = int(sys.stdin.readline().strip())
leaf_node_num = 0

dfs(removed_node)

for i in range(len(arr)):
    # 죽은 노드가 아님 and 부모역할을 하는 노드가 아님
    if arr[i] != -2 and i not in arr:
        leaf_node_num += 1
print(leaf_node_num)
