'''
Input -
15
4
hallohallohallo
allo
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15

Output -
21

'''
# Code ->

min = []
def find(arr,C,S,a = 0):
    if len(S) < len(C):
        return min
    b = S.find(C)
    a += b
    min.append(arr[a])
    return find(arr,C,S[b+1:],arr[a])

N = int(input())
M = int(input())
S = input()
C = input()[:M]
arr = []
for i in range(N):
  arr.append(int(input()))
find(arr,C,S)
print(sum(min))
    

