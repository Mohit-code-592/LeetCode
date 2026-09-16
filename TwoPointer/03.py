def three_sum(arr):
    arr.sort()
    res = []
    n = len(arr)

    for i in range(n - 2):
        if i > 0 and arr[i] == arr[i + 1]:
            continue
        
        start = i + 1
        end = n - 1
        
        while start < end:
            s = arr[i] + arr[start] + arr[end]

            if s == 0:
                res.append([arr[i], arr[start], arr[end]])
                while start < end and arr[start] == arr[start + 1]:
                    start += 1
                while start < end and arr[end] == arr[end - 1]:
                    end -= 1

                start += 1
                end -= 1

            elif s < 0:
                start += 1
            else:
                end -= 1

        return res

arr = [-1, 0, 1, 2, -4]

