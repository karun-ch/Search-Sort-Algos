from numpy import random
import time

iterations = 0
def merge(S, temp, From, mid, to):
    global iterations
    a = From
    b = From
    c = mid + 1

    while b <= mid and c <= to:
        iterations += 1
        if S[b] < S[c]:
            temp[a] = S[b]
            b = b + 1
        else:
            temp[a] = S[c]
            c = c + 1
        a = a + 1

# remaining elements
    while b < len(S) and b <= mid:
        iterations += 1
        temp[a] = S[b]
        a = a + 1
        b = b + 1

# copy back
    for b in range(From, to + 1):
        iterations += 1
        S[b] = temp[b]


# Iterative sort
def Merge_Sort(S):
    global iterations
    low = 0
    high = len(S) - 1

# sort list
    temp = S.copy()
    d = 1
    while d <= high - low:

        for b in range(low, high, 2*d):
            iterations +=1
            From = b
            mid = b + d - 1
            to = min(b + 2*d - 1, high)
            merge(S, temp, From, mid, to)
        d = 2*d
    return iterations
# Iterative implementation
if __name__ == '__main__':
#driver code
    S = []
    S = random.randint(1000, size=100)
    #print("The Original array is: ", S)
    start_time = time.time()
    iterations = Merge_Sort(S)
    end_time = time.time()
    print("Sorted array:\n",S)
    print("Iterations:", iterations)
    print("Time taken:", end_time-start_time, "seconds")