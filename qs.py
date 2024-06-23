import random
import time


def msort(a):
    if n>1:
        mid = n//2
        L = a[:mid]
        R = a[mid:]
        msort(L)
        msort(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i] <= R[j]:
                a[k] = L[i]
                i+=1
            else:
                a[k] = R[j]
                j+=1


            k+=1
        while i<len(L):
            a[k] = L[i]
            i+=1
            k+=1
        while j<len(R):
            a[k] = R[i]
            j+=1
            k+=1   
        
a = random.sample(range(0,100),10)
print(a)
n=len(a)
#c=0
st=time.time()
msort(a)
et=time.time()
#print(c)
print(a)
print(et-st , end =" ")
print("seconds")
