from numpy import random
import time

def insort(a):
    c=0
    for i in range (1,len(a)):
        t = a[i]
        j=i-1
        while j>=0 and a[j] > t :
            a[j+1]=a[j]
            j=j-1
            c+=1
            #print(a)
            #print(c)
        a[j+1] = t
    print("Iterations:",c)

a = random.randint(1000,size=(100))
#print("taken:",a)
st = time.time()

insort(a)
et = time.time()
print("Sorted Array: \n",a)
#for i in a : print (i, end =" ")
#print()
print("Time taken:",et-st ," seconds")