import sys

input = sys.stdin.readline().rstrip()
while input != 'END':
    arr_input = list(input)
    arr_input.reverse()
    for i in arr_input:
        print(i,end="")
    print()
    input = sys.stdin.readline().rstrip()
