#! /usr/bin/python
import math
#look for the factor of 2 and 5
 def look2and5 (L):
    m = 0
    n = 0
    for i in L:
        t= i
        while t%2==0:
            t/=2
            m+=1
        while t%5==0:
            t/=5
            n+=1
    if m>n:
        print(n)
    else:
        print(m)
  
# prime number
def prime_number():
    L=[]
    for i in range(2,100):
        flag = 1
        for m in range(2,int(math.sqrt(i))+1):
            if i%m == 0:
                flag = 0
        if flag == 1:
            L.append(i)
    print(' '.join(str(i) for i in L))
  
# median number
def median_number(L):
    L.sort()
    length = len(L)
    if length%2==0:
        print((L[length/2]+L[length/2-1])/2.0)
    else:
        print(L[int(length/2)])
    print(L)
