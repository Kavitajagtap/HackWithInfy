'''
input:
6
aabbca
Output:
2

'''
# Code ->

N = int(input())
s = input()[:N]
s_left = s[:len(s)//2]
s_right = s[len(s)//2:]
count = 0
for i in set(s_left):
    if i in s_right:
        count += 1
print(count)
