import sys
n,m = map(int,sys.stdin.readline().rstrip().split())

a_list = list(map(int,sys.stdin.readline().rstrip().split()))
b_list = list(map(int,sys.stdin.readline().rstrip().split()))

merge_list = a_list+b_list
merge_list.sort()
print(*merge_list)
