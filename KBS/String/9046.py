import sys
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    input = sys.stdin.readline().rstrip().replace(' ','')
    tmp = list(input)
    tmpset = set(tmp)
    res = {}
    for i in tmpset:
        y = tmp.count(i)
        res[i] = y
    re = dict(sorted(res.items(), key=lambda x: x[1],reverse=True))

    ma = -1
    ans = []
    for i in re.keys():
        if re.get(i) >= ma:
            ma = re.get(i)
            ans.append(i)

    if len(ans) == 1:
        print(ans[0])
    else:
        print('?')
            
