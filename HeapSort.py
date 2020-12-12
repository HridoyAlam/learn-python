def MaxHeapify(a, n, i):
    l = 2*i +1
    r = 2*i +2
    largest = i

    if(l<n and a[l]>a[largest]):
        largest = l
    if(r< n and a[r]> a[largest]):
        largest =r
    
    if(largest != i):
        temp = a[largest]
        a[largest]= a[i]
        a[i] = temp
        MaxHeapify(a,n,largest)
def BuildMaxHeap(a,n):
    startInd = (n//2)-1

    for i in range(startInd, -1,-1):
        MaxHeapify(a,n,i)
def Heap_Sort(a,n):
    BuildMaxHeap(a,n)

    for i in range(n-1, 0, -1):
        arr[i],arr[0] = arr[0],arr[i]
        MaxHeapify(a,i,0)

def printHeap(a, n):
    for i in range(n):
        print(a[i],end=" ")

if __name__ == "__main__":
    arr = [2,4,6,8,7,5,10,15]
    n = len(arr)
   # BuildMaxHeap(arr,n)
    #printHeap(arr, n)
    Heap_Sort(arr,n)
    print(arr,n)
