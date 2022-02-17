def adjust_heap(arr, i, length):
    temp = arr[i]
    k = 2 * i + 1
    while k < length:
        if k + 1 < length and arr[k] < arr[k + 1]:
            k = k + 1
        if arr[k] > temp:
            arr[i] = arr[k]
            i = k
        else:
            break
        k = 2 * i + 1
    arr[i] = temp


def sort(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        adjust_heap(arr, i, len(arr))
    for j in range(len(arr) - 1, -1, -1):
        arr[0], arr[j] = arr[j], arr[i]
        adjust_heap(arr, 0, j)



arr = [9,8,7,6,5,4,3,2,1]
sort(arr)
print(arr)



