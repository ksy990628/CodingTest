#1	10818	최소, 최대		
x = int(input())
arr = input().split()
new_arr = []

for i in range(x):
    new_arr.append(int(arr[i]))

print(min(new_arr),max(new_arr))


#2	2562	최댓값
arr = []
for i in range(9):
    x = int(input())
    arr.append(x)

print(max(arr))
print(arr.index(max(arr))+1)


#3	2577	숫자의 개수	
result = 1
numArr = [0 for i in range(10)]

for i in range(3):
    x = int(input())
    result *= x

temp = str(result)

for i in range(len(temp)):
    if temp[i] == "0":
        numArr[0] += 1
    elif temp[i] == "1":
        numArr[1] += 1
    elif temp[i] == "2":
        numArr[2] += 1    
    elif temp[i] == "3":
        numArr[3] += 1
    elif temp[i] == "4":
        numArr[4] += 1
    elif temp[i] == "5":
        numArr[5] += 1
    elif temp[i] == "6":
        numArr[6] += 1
    elif temp[i] == "7":
        numArr[7] += 1
    elif temp[i] == "8":
        numArr[8] += 1
    elif temp[i] == "9":
        numArr[9] += 1

for i in range(len(numArr)):
    print(numArr[i])


#4	3052	나머지	
m_arr = []

for i in range(10):
    x = int(input())
    m = x % 42
    if m not in m_arr:
        m_arr.append(m)

print(len(m_arr))


#5	1546	평균	
x = int(input())
arr = input().split()
new_arr = []

for i in range(x):
    new_arr.append(int(arr[i]))

print((sum(new_arr)/max(new_arr))*100/x)


#6	8958	OX퀴즈
x = int(input())

for i in range(x):
    y = input()
    total = 0
    count = 0
    for j in y:
        if j == 'O': #O인 경우
            count += 1
            total += count
        else:
            count = 0

    print(total)
        

#7	4344	평균은 넘겠지	
x = int(input())

for i in range(x):
    str = input()
    arr = str.split()
    arr = list(map(int, arr))
    avg = (sum(arr)-arr[0])/arr[0]
    n = 0
    for j in range(1,len(arr)):
        if arr[j] > avg:
            n += 1
    print("%.3f%%" %(n/arr[0]*100))
    n = 0
