from numpy import random
import time

def bsort(a):
    cnt = 0
    for i in range (len(a)):
        s = False
        for j in range (0, len(a)-i-1):
            t=a[j+1]
            if a[j]>a[j+1]:
                a[j+1] = a[j]
                a[j] = t
                cnt+=1
                s = True
                #print("Array:",a)
                #print(cnt)
 #           print(cnt)
#        print(cnt)
        if s == False : break
    print("Itterations:",cnt)


a = random.randint(10000,size=(100))
#print("UnsArray:",a)
st=time.time()
bsort(a)
et=time.time()
#for i in a : print(i , end=" ")
print("Sorted Array:","\n",a)
print("Time taken:",et-st , end =" ")
print("seconds")