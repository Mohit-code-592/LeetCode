def roate(arr, k):
    for rounds in range(1, k + 1):
        temp = arr[len(arr) - 1]
        for j in range(len(arr) - 2, -1, -1):
            arr[j + 1] = arr[j]

        arr[0] = temp

arr = [1,2,3,4,5]

def optmized(arr, k):
    n = len(arr) - 1
    k = k % n

    ans = arr[-k:] + arr[:-k]

    print(ans)


# optmized([1,2,3,4,5,6], 3)


def reverse_arr(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
def optimal(arr, k):
    
    k = k % len(arr)
    n = len(arr) - 1
    reverse_arr(arr, 0, n - k)
    reverse_arr(arr, n - k + 1, n)
    reverse_arr(arr, 0, n)
    print(arr)

optimal(arr, 2)
