import sys
input = sys.stdin.readline

class Node(object):
    # trie 자료구조를 위한 node
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        # dictionary 자료구조 사용
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    # 문자열 삽입
    def insert(self, string):
        curr_node = self.head
        
        for char in string:
            # 자식 Node들 중 같은 문자가 없으면 Node 새로 생성
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            # 같은 문자가 있으면 해당 노드로 이동
            curr_node = curr_node.children[char]

        curr_node.data = string

    # 문자열이 존재하는지 search
    def search(self, string):
        curr_node = self.head

        for char in string:
            curr_node = curr_node.children[char]
            
        if curr_node.children:
            return False
        else:
            return True

t = int(input())
for _ in range(t):
    n = int(input())
    trie = Trie()
    nums = []
    for _ in range(n):
        num = input().rstrip()
        nums.append(num)
        trie.insert(num)

    flag = True
    nums.sort()
    for num in nums:
        if not trie.search(num):
            flag = False
            break

    if flag:
        print('YES')
    else:
        print('NO')
