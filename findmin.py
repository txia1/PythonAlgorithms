#complexcitiy n 
import time
from random import randrange
def findmin(alist):

    overallmin = alist[0]
    for i in alist:
        if i < overallmin:
            overallmin = i

    return overallmin

a = [5,4,3,2,1,0]

print(findmin(a))

for listSize in range(1000,10001,1000):
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(findmin(alist))
    end = time.time()
    print(listSize,end-start)