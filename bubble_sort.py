def bubble_sort(arr: list, asc: bool) -> list:
    for i in range(1, len(arr)):
        for j in range(len(arr) - 1, i - 1, -1):
            if asc:
                if arr[j - 1] > arr[j]:
                    arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                if arr[j - 1] < arr[j]:
                    arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr


# Testing
print(bubble_sort([1, 2, 3], True))
print(bubble_sort([1, 2, 3], False))
print(bubble_sort([], True))
print(bubble_sort([3, 3, 1, 5, 3, 4], True))
print(bubble_sort([3, 3, 1, 5, 3, 4], False))
print(bubble_sort([-1, 2, 7, -9, 0], True))
print(bubble_sort([-1, 2, 7, -9, 0], False))
