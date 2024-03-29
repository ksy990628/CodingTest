import sys


class Trie:
    def __init__(self):
        self.root = {}

    def add(self, foods):
        cur = self.root

        for food in foods:
            if food not in cur:
                cur[food] = {}  # 자식 노드
            cur = cur[food]
        cur[0] = True  # 리프 노드 표시
        # print(self.root)
	
    # DFS
    def travel(self, level, cur):
        if 0 in cur:
            return
        cur_child = sorted(cur)

        for ch in cur_child:
            print("--" * level + ch)
            self.travel(level + 1, cur[ch])


input = sys.stdin.readline
N = int(input())
trie = Trie()
for i in range(N):
    data = list(input().split())
    trie.add(data[1:])

trie.travel(0, trie.root)
profile


# Trie 이외의 완전탐색
'''
import sys

input = sys.stdin.readline
N = int(input())
food_info = []
for i in range(N):
    data = list(input().split())
    food_info.append(data[1:])

food_info.sort()

dash = '--'
answer = []
for i in range(N):
    # 첫 번째는 부모, 자식 노드의 중복이 없으므로 그대로 출력.
    if i == 0:
        for j in range(len(food_info[i])):
            answer.append(dash * j + food_info[i][j])
    else:
        idx = 0   # 이전의 리스트와 현재 리스트에서 맨 왼쪽부터 겹치는 원소의 개수를 저장.
        for j in range(len(food_info[i])):
            # 이전의 리스트의 원소가 없거나, 이전의 리스트와 현재 리스트가 겹치지 않을 때
            if food_info[i - 1][j] != food_info[i][j] or len(food_info[i - 1]) <= j:
                break
            # 겹치는 원소가 존재한다면 해당 원소를 출력할 필요가 없으므로 idx를 조정.
            else:
                idx = j + 1
        for j in range(idx, len(food_info[i])):
            answer.append(dash * j + food_info[i][j])

for ans in answer:
    print(ans)
'''
