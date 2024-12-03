def bubble_sort(arr):

    """ Time Complexity: O(n'2)
    Space Complexity: O(1)."""


    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so no need to check them
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array using bubble sort:", arr)


def merge_sort(arr):

    """ Time Complexity: O(n log n)
        Space Complexity: O(n)."""

    if len(arr) <= 1:
        return arr
    
    ## gives the half value
    mid = len(arr) // 2

    L = arr[:mid]
    R = arr[mid:]

    merge_sort(L)
    merge_sort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    return arr


print("Sorted array using Merge sort:",merge_sort([8,5,2,1,4,7,9,6,3]))



def quick_sort(arr):

    """ Time Complexity: In each recursion level, the array is divided into two partitions, which takes O(n) time,
        and there are O(log n) levels of recursion in the best and average cases.
        Therefore, the overall time complexity is O(n log n).

        Space Complexity: The space complexity mainly comes from the call stack during the recursive calls.
        In the best and average cases, the recursion depth is O(log n) because the array is partitioned roughly in half at each step.
        However, in the worst case, where the partitioning is highly unbalanced,
        the recursion depth can be as large as 'n', resulting in a space complexity of O(n)."""


    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print(sorted_arr)


















