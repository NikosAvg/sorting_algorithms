def selection_sort(arr: list, asc: bool) -> list:
    """
    Sorts a list of comparable elements in either ascending or descending order.

    Parameters:
        - arr (list): The input list containing elements to be sorted.
        - asc (bool): A boolean flag indicating the sorting order.
                      If True, the list will be sorted in ascending order.
                      If False, the list will be sorted in descending order.

    Returns:
        list: The sorted list.

    Description:
        The function implements the selection sort algorithm, which iterates
        through the input list and selects the minimum (or maximum) element in
        the unsorted portion, swapping it with the first element of the unsorted
        portion. This process is repeated until the entire list is sorted.

        The sorting order is determined by the 'asc' parameter. If 'asc' is True,
        the list is sorted in ascending order; otherwise, it is sorted in
        descending order.
    """
    for i in range(len(arr)):
        comparable = arr[i]
        pos = i
        for j in range(i, len(arr)):
            if asc:
                if comparable > arr[j]:
                    pos = j
                    comparable = arr[j]
            else:
                if comparable < arr[j]:
                    pos = j
                    comparable = arr[j]
        arr[i], arr[pos] = arr[pos], arr[i]
    return arr


# Testing
print(selection_sort([1, 2, 3], True))
print(selection_sort([1, 2, 3], False))
print(selection_sort([], True))
print(selection_sort([3, 3, 1, 5, 3, 4], True))
print(selection_sort([3, 3, 1, 5, 3, 4], False))
print(selection_sort([-1, 2, 7, -9, 0], True))
print(selection_sort([-1, 2, 7, -9, 0], False))
