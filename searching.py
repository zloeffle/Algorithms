'''
Binary Search O(logn)
- searches a sorted array by repeatedly dividing the search interval in half
'''
def binary_search(arr, low, high, key):
    
    if high >= low:
        mid = low + (high-low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search(arr, low, mid-1, key)
        else:
            return binary_search(arr, mid+1, high, key)
    else:
        return -1 # key not found

'''
TESTING
'''
# binary search
arr = [ 2, 3, 4, 10, 40 ]
res = binary_search(arr, 0, len(arr)-1, 10)
print('Binary Search')
print(res)