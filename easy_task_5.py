from math import *
t = int(input())
for i in range(t):
    N = int(input())
    list = [int(x) for x in input().split()]
    evennum = 0
    for i in list:
        if i % 2 == 0:
            evennum += 1
    oddnum = N-evennum
    print(min(evennum,floor((N+1)/2)) + min(oddnum,ceil((N-1)/2)))
