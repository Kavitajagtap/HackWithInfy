'''
Problem Statement: Let’s define a Beautiful Function F(x) in such a way: Add 1 to the value of x, if the result of addition contains any trailing zeros then remove them all.

Example:
F(11) = 12
F(19) = 2 (20 –> 2)
F(99) = 1(100 –> 10 –> 1)

Let’s define a number to be reachable from x , if we can apply Beautiful Function some number of times (possibly zero) to x and get that number as result
Ex. 102 can be reachable from 1099 as F(F(1099)) = F(101) = 102
You are given a number N . Calculate how many numbers are reachable from N.

input         output                       explanation

1             	9	                  1,2,3,4,5,6,7,8,9 are reachable from 1.

'''

# Code ->

num = input()
total = 0

i = len(num)-1
carry = 0
while(i > 0):
    curr_dist = 10 - (int(num[i]) + carry)
    total = total + curr_dist
    carry = 1
    i -= 1
total = total + 9
print(total)






