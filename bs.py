from numpy import random
import time
def binarySearch(arr, l, r, x):
    c=0
    while l <= r:
        print("Iterations",c)
       # c+=1
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
            c+=1
        elif arr[mid] < x:
            l = mid + 1
            c+=1
        else:
            r = mid - 1
            c+=1
        #print("Iterations",c)
    #print("Iterations",c)
    return -1

    #print(c)
if __name__ == '__main__':
    arr = random.randint(100,size=(100))
    #print(arr)
    #arr=[1,2,4,6,8,10,12]
    #a=len(arr)
    x = 10
    #print("Iterations",c)
    
    st=time.time()
    result = binarySearch(arr, 0, len(arr)-1, x)
   # print(c)
    et=time.time()
    print("Time Taken: ",et-st,"seconds")
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")