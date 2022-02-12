#1	  10872	  팩토리얼
n = int(input())

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(n))

#2	  10870	  피보나치 수 
n = int(input())

def fibo(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibo(n-1)+fibo(n-2)
  
print(fibo(n))

#3	  2447	  별 찍기 - 10


#4	  11729	  하노이 탑 이동 순서		
n = int(input())
count = 0
arr = []

def hanoi(n,a,b,c):
    global count
    count += 1
    if n == 1:
        arr.append([a,c])
    else:
        hanoi(n-1,a,c,b)
        arr.append([a,c])
        hanoi(n-1,b,a,c)
    
    
hanoi(n,1,2,3)
print(count)
for i in range(count):
    print(arr[i][0],arr[i][1])
