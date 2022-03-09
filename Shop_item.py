'''
Input:
3
3
4
8
10
Output: 
3
'''

# Code ->

import sys
def itemShop(n, A, k):
    a = []
    c = 0
    for i in range(n,0,-1):
        a.append(i)
    for i in range(0,len(A)):
        for j in range(1,a[i]+1):
            if A[i]*j >= k:
                break;
            c += 1
        if A[i]*j == k-1:
            break
    return c

def main():
    n = int(sys.stdin.readline().strip())
    A = []
    for _ in range(n):
        A.append(int(sys.stdin.readline().strip()))
    k = int(sys.stdin.readline().strip())
    result = itemShop(n, A, k)
    print(result)

if __name__ == "__main__":
    main()
               
