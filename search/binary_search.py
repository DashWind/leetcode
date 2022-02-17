


def bin_search(arr, target):

    left, right = 0, len(arr) - 1
    while left < right:
        print(arr[left], arr[right])
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


a = [1, 2, 3, 4, 5, 6, 10, 11]
print(bin_search(a, 10))