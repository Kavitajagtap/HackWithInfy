'''
input:  20  

output:  4, 6, 9, 10, 14, 15   

explanation :
  2 * 2 = 4         3 * 3 = 9
  2 * 3 = 6         3 * 5 = 15
  2 * 5 = 10
  2 * 7 = 17
  
'''
             



# Code - >
import math
def isprime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True

    for i in range(2, int((num**0.5) + 1)):
        if num % i == 0:
            return False
    return True

n= int(input())

for i in range(n):
    num = int(input())
    primes = []
    for p in range(2,num//2+1):
        if isprime(p):
          primes.append(p)

    semiprime = []

    for i in range(0,len(primes)):
       for j in range(i,len(primes)):
        curr_num = primes[i]*primes[j]
        if curr_num <= num:
            semiprime.append(curr_num)
        else:
            break
    semiprime.sort()
    for i in semiprime:
        print(i,end = " ")


