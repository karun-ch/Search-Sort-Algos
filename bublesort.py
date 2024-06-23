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
 #           print(cnt)
#        print(cnt)
        if s == False : break
    print(cnt)


a = random.randint(1000,size=(100))
st=time.time()
bsort(a)
et=time.time()
#for i in a : print(i , end=" ")
print("Sorted Array:",a)
print(et-st , "seconds")

























# from numpy import random

# def bsort(a):
#     cnt = 0
#     for i in range (len(a)):
#         s = False
#         for j in range (0, len(a)-i-1):
#             t=a[j+1]
#             if a[j]>a[j+1]:
#                 a[j+1] = a[j]
#                 a[j] = t
#                 cnt+=1
#                 s = True
#  #           print(cnt)
# #        print(cnt)
#         if s == False : break
#     print(cnt)


# a = random.randint(1000,size=(50))


# #a = [5,3,4,7,9,6,8,10,13,12,11,15,14,1,2]
# #a = [5,4,3,2,1, 58 ,62 ,0,22 ]
# bsort(a)
# for i in a : print(i , end=" ")



#up main

'''
import numpy as ny

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
                print(cnt)
                s = True
        if s == False : break


a = ny.random.randint(10,size=(5))


#a = [5,3,4,7,9,6,8,10,13,12,11,15,14,1,2]
#a = [5,4,3,2,1, 58 ,62 ,0,22 ]
bsort(a)
for i in a : print(i , end=" ")
'''
'''
from numpy import random

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
                print(cnt)
                s = True
        if s == False : break


a = random.randint(100,size=(5))


#a = [5,3,4,7,9,6,8,10,13,12,11,15,14,1,2]
#a = [5,4,3,2,1, 58 ,62 ,0,22 ]
bsort(a)
for i in a : print(i , end=" ")

'''
