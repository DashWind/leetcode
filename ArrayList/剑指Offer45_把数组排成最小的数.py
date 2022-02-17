def min_num(arr):
    def quick_sort(arr, l, r):
        if l >= r: return
        i, j = l, r
        while i < j:
            while i < j and arr[j] + arr[l] >= arr[l] + arr[j]: j -= 1
            while i < j and arr[i] + arr[l] <= arr[l] + arr[i]: i += 1
            arr[i], arr[j] = arr[j], arr[i]
        arr[i], arr[l] = arr[l], arr[i]
        quick_sort(arr, l, i - 1)
        quick_sort(arr, i + 1, r)

    strs = [str(num) for num in arr]
    quick_sort(strs, 0, len(strs) - 1)
    return ''.join(strs)


a = [3, 34, 5, 30, 9]
# print(min_num(a))
