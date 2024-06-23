import random 

import time 

c=0 

 

a=random.sample(range(0,1000),100) 

 

def heapify(a, N, i): 
    largest = i # Initialize largest as root 

    l = 2 * i + 1 #    # left = 2*i + 1 

    r = 2 * i + 2 #    # right = 2*i + 2 

 

#    # See if left child of root exists and is 

#    # greater than root 

    if l < N and a[largest] < a[l]: 

     largest = l 

 

#    # See if right child of root exists and is 

#    # greater than root 

    if r < N and a[largest] < a[r]: 

     largest = r 

 

#    # Change root, if needed 

    if largest != i: 

     a[i], a[largest] = a[largest], a[i] # swap 

 

#        # Heapify the root. 

     heapify(a, N, largest) 

 

# The main function to sort an array of given size 

 

def heapSort(a): 

 global c 

 N = len(a) 

 # Build a maxheap. 

 for i in range(N//2 - 1, -1, -1): 

    heapify(a, N, i) 

#         

 

#    # One by one extract elements 

 for i in range(N-1, 0, -1): 

     a[i], a[0] = a[0], a[i] # swap 

     heapify(a, i, 0) 

     c+=1 

#         

 

s=time.time() 

 

heapSort(a) 

print("Sorted Array: \n",a) 

 

e=time.time() 

 

print("Time Taken:",e-s,"seconds") 

print("Iterations:",c) 

 