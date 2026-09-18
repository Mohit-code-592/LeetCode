# Remove Duplicates from Sorted Array

def brute_force(arr):
    set_container = sorted(list(set(arr)))
    
    k = len(set_container)
    for i in range(len(set_container)):
        arr[i] = set_container[i]

    return k

    
def two_pointer(arr):
    k = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[k] = arr[i]
            k += 1

    return k

arr = [-1,0,0,0,0,3,3]

