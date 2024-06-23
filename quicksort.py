from numpy import random
import time

c=0

def part (a,l,h):
    global c
    r=a[h]
    i=l-1
    #print(a)
    for j in range(l,h):
        #global c
        #print(a)
        c+=1
        #print(c)
        if a[j] <=r:
            #global c
            i+=1
            a[i],a[j] = a[j],a[i]
            #c+=1
    a[i+1],a[h] = a[h],a[i+1]
    
    return i+1  
    
def qsort(a,l,h):
    #print(a)
    if l<h:
        #print(a)
        p=part(a,l,h)
        qsort(a,l,p-1)
        qsort(a,p+1,h)
    #print(a)

a = random.randint(1000,size=(100))
#a=[5,58,4,3,0,1]
#print("Taken:",a)
n=len(a)
#c=0
st=time.time()
qsort(a,0,n-1)
et=time.time()
print("Iterations:",c)
print("Sorted array:\n",a)
print("Time taken:",et-st,"seconds")