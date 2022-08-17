def inorder(node):
  if node :
    inorder(tree[node][2])    # 왼쪽
    formula.append(tree[node][1])    # 연산자 or 숫자
    inorder(tree[node][3])    # 오른쪽

for tc in range(10) :     # 10개의 테스트 케이스
  n=int(input())        # 총 정점의 수
  tree=[[0 for _ in range(4)] for _ in range(n+1)]    # 열 =  정점 번호, 해당 정점의 알파벳, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점번호
  
  # 정점의 수만큼 입력받음.
  for line in range(n):
    tmp=list(input().split())
    index=int(tmp[0])  		 # 노드 번호
    tree[index][0]=index
    if len(tmp) >= 3 :
      tree[index][2]=int(tmp[2])    # 해당 정점의 왼쪽 자식
    if len(tmp) == 4 :
      tree[index][3]=int(tmp[3])    	# 오른쪽 자식의 정점 번호
    tree[index][1]=tmp[1]     	# 해당 정점의 알파벳

  formula=[]
  inorder(1)
  result=1      # 유효성 검사 통과

  for i in range(len(formula)):
    if not i%2 :    # i%2가 0(짝수)이면 True
      if ord(formula[i]) < 48 or ord(formula[i]) >= 58 :    # '0'이 48, '9'가 57
        result=0      # 유효성 검사 통과 실패
        break
    else:   # 홀수면
      if formula[i] not in ['-', '+', '*', '/']:  # 연산자가 아니면
        result=0
        break

  print(f"#{tc+1} {result}")
