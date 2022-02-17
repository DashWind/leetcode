def get_index(arr, left, right):
    temp = arr[left]

    while left < right:
        while left < right and arr[right] >= temp:
            right -= 1

        arr[left] = arr[right]

        while left < right and arr[left] <= temp:
            left += 1

        arr[right] = arr[left]

    arr[left] = temp
    return left


def quick_sort_recur(arr, left, right):
    """
    递归快排
    :param arr:
    :param left:
    :param right:
    :return:
    """
    if left < right:
        mid = get_index(arr, left, right)
        quick_sort_recur(arr, left, mid - 1)
        quick_sort_recur(arr, mid + 1, right)


def quick_sort_unrecur(arr, left, right):
    """
    非递归快排
    :param arr:
    :param left:
    :param right:
    :return:
    """
    stack = [left, right]
    while stack:
        r, l = stack.pop(), stack.pop()
        mid = get_index(arr, l, r)
        if r > mid + 1:
            stack.append(mid + 1)
            stack.append(r)
        if l < mid - 1:
            stack.append(l)
            stack.append(mid - 1)


a = [2, 1, 4, 5, 10, 12, 1, 1]
quick_sort_unrecur(a, 0, len(a) - 1)
print(a)
