#1. n에서 k진수로 바꾸기
#2. k진수로 바꾼 배열에서 0이 있으면 넘어가고 0 사이의 값만 소수 판별하기
#3. 소수 판별하기
#4. answer +1하기

import math

def chage_num(n, k): #k진수로 바꾸기
    num=[]
              
    while n>=k:
        num.append(n%k)
        n=n//k
    
    num.append(n)
    
    num = num[::-1]
    
    return num


def decimal(n): #소수 판별하기
    if n>2:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
    
    elif n==2:
        return True
    else:
        return False
        
    
    

def solution(n, k):
    num = chage_num(n, k)
    buffer=[]
    answer = 0
    
    num.append(0) #숫자 마지막에 소수가 있는 경우에 검사하기 위해서
    
    for i in num:
        if i !=0:
            buffer.append(i)
        else:
            if buffer:
                if (decimal(int(''.join(map(str, buffer))))):
                    answer +=1
                buffer.clear()
    
    return answer  


