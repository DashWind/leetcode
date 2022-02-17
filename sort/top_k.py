def heap_adjust(arr, i, length):
    temp = arr[i]
    k = 2 * i + 1
    while k < length:
        if k + 1 < length and arr[k] > arr[k + 1]:
            k = k + 1
        if arr[k] < temp:
            arr[i] = arr[k]
            i = k
        else:
            break
        k = 2 * i + 1
    arr[i] = temp


def top(arr, k):
    for i in range(k // 2 - 1, -1, -1):
        heap_adjust(arr, i, k)

    for j in range(k, len(arr), 1):
        if arr[j] > arr[0]:
            arr[0], arr[j] = arr[j], arr[0]
            heap_adjust(arr, 0, k)


ar = [7,5,2,3,4, 10]
k = 4
top(ar, k)
print(ar[:k])
