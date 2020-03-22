'''
Practice for various sorting algorithms
'''

'''
Quick Sort Avg: O(nlogn) Worst: O(n^2)
- Use when you don't need a stable sort and avg performance matters most
'''
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr,low,high) # parition index
        # sort elems before and after pivot
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
            

def partition(arr, low, high):
    pivot = arr[high] # pick highest elem as pivot
    i = low-1 # index of smaller elem
    
    for j in range(low,high):
        if arr[j] < pivot:
            # if curr elem is smaller than pivot increment index of smaller elem
            i += 1
            
            # swap arr[i] and arr[j]
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    
    # swap arr[i+1] and arr[high]
    temp = arr[i+1]
    arr[i+1] = arr[high]
    arr[high] = temp
    return i+1 # return index of pivot
    


'''
Merge Sort O(nlogn), O(n) space
- Use when you need a stable sort
- has slightly larger constant that quick sort
'''
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2 # index of middle elem
        left = arr[0:mid] # left half
        right = arr[mid:len(arr)] # right half
        
        # call merge sort on left & right halves
        merge_sort(left)
        merge_sort(right)
        
        # sort each half 
        i,j,k = 0,0,0
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                arr[k] = left[i] 
                i+=1
            else: 
                arr[k] = right[j] 
                j+=1
            k+=1
            
        # Checking if any element was left 
        while i < len(left): 
            arr[k] = left[i] 
            i+=1
            k+=1
            
        while j < len(right): 
            arr[k] = right[j] 
            j+=1
            k+=1
'''
Heap Sort O(nlogn), O(1) space 
- Use when you care most about worst case than average case
- useful for sorting a k sorted array and finding k largest/smallest elem
'''
def heap_sort(arr): # O(n)
    for i in range(len(arr), -1, -1):
        heapify(arr, len(arr), i)
    
    for i in range(len(arr)-1, 0, -1): 
        temp = arr[i]
        arr[i] = arr[0]
        arr[0] = temp
        heapify(arr, 0, i) 

# build max heap O(logn)
def heapify(arr, size, root):
    maxNode = root # max node is set to root
    left = 2*root + 1 # left child
    right = 2*root + 2 # right child
    
    # check if left/right children of root exist and are greater
    if left < size and arr[root] < arr[left]:
        maxNode = left
    if right < size and arr[maxNode] < arr[right]:
        maxNode = right
        
    if maxNode != root:
        temp = arr[root]
        arr[root] = arr[maxNode]
        arr[maxNode] = temp
        heapify(arr, size, maxNode)
        
'''
Bubble Sort
- simplest sorting alg, repeatedly swaps adjacent elements if they are in the wrong order
'''
def bubble_sort(arr):
    swapped = False
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True
        if swapped == False:
            break

'''
Insertion Sort O(n^2)
'''
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

'''
Testing
'''

# quicksort
data = [12, 11, 13, 5, 6, 7] 
size = len(data)
quick_sort(data, 0, size - 1)
print('Quick sort:')
print(data)

# merge sort
data = [12, 11, 13, 5, 6, 7] 
merge_sort(data)
print('Merge Sort:')
print(data)

# heapsort
data = [12, 11, 13, 5, 6, 7] 
heap_sort(data)
print('Heap Sort:')
print(data)

# bubble sort
data = [12, 11, 13, 5, 6, 7] 
bubble_sort(data)
print('Bubble Sort:')
print(data)

# insertion sort
data = [12, 11, 13, 5, 6, 7] 
insertion_sort(data)
print('Insertion Sort:')
print(data)