from numpy import random
import time

def selsort(a):
    c=0
    for i in range (len(a)):
        t = i
        for j in range (i+1,len(a)):
            if a[j]<a[i]:
                t=j
                c+=1
                a[i],a[t] = a[t],a[i]
#             a[j+1]=a[j]
#             j=j-1
#             c+=1
          #  print(c)
           # print(a)
     #   a[j+1] = t
    print("Iterations:",c)

a = random.randint(1000,size=(100))
#print(a)
st = time.time()

selsort(a)
et = time.time()
print("Sorted Array:",a)
#for i in a : print (i, end =" ")
#print()
print("Time Taken:",et-st ,"seconds")