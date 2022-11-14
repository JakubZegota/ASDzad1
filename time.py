import time
import random
import sys

def maxHeapify(A, heapsize, i):
    largest = i
    l = 2*i+1
    r = 2*i+2
    if (l<heapsize and A[l]>A[largest]):
        largest = l
    else:
        largest = i
    
    if (r<heapsize and A[r]>A[largest]):
        largest = r        

    if (largest!=i):
        A[i],A[largest]=A[largest],A[i]
        maxHeapify(A, heapsize, largest) 
        
def buildMaxHeap(A, heapsize):
    n = int((heapsize//2)-1)
    for k in range(n, -1, -1):
        maxHeapify(A,heapsize,k) 

def heapSort(A):
    startTime = time.time()
    heapsize = len(A)
    buildMaxHeap(A, heapsize)
    for i in range (heapsize-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        maxHeapify(A, i, 0)

    endTime = time.time()  
    print (round(endTime-startTime, 3),"s")
    return A    

def partition(A, p, r):
    pivot = A[r]
    smaller = p
    for i in range(p, r):
        if (A[i]<=pivot):
            A[i], A[smaller] = A[smaller], A[i]
            smaller = smaller+1
    
    A[r], A[smaller] = A[smaller], A[r]     
    return smaller

def quickSort(A, p, r):
    startTime = time.time()
    def sort(A, p,r): 
        if (p<r): 
            q = partition(A, p, r)
            sort(A, p, q-1) 
            sort(A, q+1, r)
    sort(A, p, r)
    endTime = time.time()  
    print (round(endTime-startTime,3),"s")

   

def mergeSort(A):
    startTime = time.time()
    def sort(A):
        if len(A) > 1:
            half = len(A)//2
            L = A[:half]
            M = A[half:]
            sort(L)
            sort(M)

            i = j = k = 0

            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    A[k] = L[i]
                    i += 1
                else:
                    A[k] = M[j]
                    j += 1
                k += 1

            while i < len(L):
                A[k] = L[i]
                i += 1
                k += 1

            while j < len(M):
                A[k] = M[j]
                j += 1
                k += 1  

    sort(A)
    endTime = time.time()
    print (round(endTime-startTime,3),"s")

def tabWithZeros(n): 
    tabWithZeros = []
    for i in range(0, n):
        tabWithZeros.append(0)
    return tabWithZeros

def tabRandom(n, max):
    tabRandom = tabWithZeros(n)
    for i in range (0,n):
        tabRandom[i] = random.randint(1,max)
    return tabRandom

def tabSorted(n, min):
    tabSorted = tabWithZeros(n)   
    tabSorted[0] = min 
    for i in range (1,n):
        tabSorted[i] = tabSorted[i-1]+random.randint(1,5)
    return tabSorted

def tabReverselySorted(n, max):
    tabReverselySorted = tabWithZeros(n)
    tabReverselySorted[0] = max
    for i in range (1,n):
        tabReverselySorted[i] = tabReverselySorted[i-1]-random.randint(1,5)
    return tabReverselySorted

sys.setrecursionlimit(200000)
tabSize=100000
tabMax=1000000

print("Mergesort, losowa tablica: ",end="")
mergeSort(tabRandom(tabSize,tabMax))

print("Heapsort, losowa tablica: ", end="")
heapSort(tabRandom(tabSize,tabMax))

print("Quicksort, tablica losowa: ",end="")
quickSort(tabRandom(tabSize,tabMax), 0, tabSize-1)

print("------------------------------------------")

print("Mergesort, tablica posortowana: ",end="")
mergeSort(tabSorted(tabSize,0))

print("Heapsort, tablica posortowana: ", end="")
heapSort(tabSorted(tabSize,0))

# Problematyczny kod, odkomentować tylko dla tabSize=10000

# print("Quicksort, tablica posortowana: ",end="")
# quickSort(tabSorted(tabSize,1), 0, tabSize-1)

print("------------------------------------------")

print("Mergesort, tablica odwrotnie posortowana: ",end="")
mergeSort(tabReverselySorted(tabSize,tabMax))
    
print("Heapsort, tablica odwrotnie posortowana: ",end="")
heapSort(tabReverselySorted(tabSize,tabMax))

# Problematyczny kod, odkomentować tylko dla tabSize=10000

# print("Quicksort, tablica odwrotnie posortowana: ",end="")
# quickSort(tabReverselySorted(tabSize,tabMax),0,tabSize-1)

