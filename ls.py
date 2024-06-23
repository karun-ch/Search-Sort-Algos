import time
from numpy import random
#a=[1,2,2,5,6,7,89,93,4,5]
a = random.randint(100,size=(10))
n=len(a)
x=2;c=0
st=time.time()
for i in range (0,n):
    c+=1
    if a[i] ==x:
        print( "Target is at index",i)
        break
if a[i] !=x:
    print("Target is not present in given array.")
et=time.time()
print("Iterations",c)
print("Time Taken: ",et-st)