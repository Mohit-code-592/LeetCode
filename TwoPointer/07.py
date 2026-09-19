# Merge Sorted Array

def two_pointer(arr1, arr2, m = 3, n = 3):
    index = m + n - 1
    i, j = m - 1, n - 1

    while i >= 0 and j >= 0:
        if arr1[i] >= arr2[j]:
            arr1[index] = arr1[i]
            index -= 1
            i -= 1
        else:
            arr1[index] = arr2[j]
            index -= 1
            j -= 1

    while j >= 0:
        arr1[index] = arr2[j]
        index -= 1
        j -= 1


arr1 = [1,2,3,0,0,0]
arr2 = [2,5,6]

two_pointer(arr1, arr2)
print(arr1)


