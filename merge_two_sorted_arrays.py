def merge_sort(arr):
    if len(arr) > 1:
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


def merge(arr):
    if len(arr) <= 1:  # Base case: If the length of the array is 0 or 1, it's already sorted
        return arr

    mid = len(arr) // 2

    L = arr[:mid]
    R = arr[mid:]

    merge(L)  # Recursively sort the left sublist
    merge(R)  # Recursively sort the right sublist

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


print(merge_sort([4,6,9,2,1,8,7,5,3,0]))
print(merge([4,6,9,2,1,8,7,5,3,0]))


sublists=[[8,7,5,3,0],[4,6,9,2,1],[10,50,30,20,40]]
sorted_lists = merge(sublists[0] + sublists[1] + sublists[2])
print(sorted_lists)  

sorted_sublists = [merge(sub) for sub in sublists]
# Merge the sorted sublists into a single sorted list
sorted_list = merge(sorted_sublists[0] + sorted_sublists[1])
print(sorted_list)  