# Valid Triangle Number

def bruteforce(arr):
    arr.sort()
    n = len(arr)
    count_triplates = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            sum_of_two = arr[i] + arr[j]
            for k in range(j + 1, n):
                if sum_of_two > arr[k]:
                    count_triplates += 1

    return count_triplates


def two_pointer(arr):
    n = len(arr)
    arr.sort()
    count = 0

    for k in range(n - 1, 1, -1):
        left, right = 0, k - 1
        while left < right:
            if arr[left] + arr[right] > arr[k]:
                count += right - left
                right -= 1
            else:
                left += 1

    return count

arr = [2,3,4,4,5]
print(two_pointer(arr))

