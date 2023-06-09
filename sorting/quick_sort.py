def partition(A, low_indx, high_indx):
    pivot = A[high_indx]

    i = low_indx - 1

    for j in range(low_indx, high_indx):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[high_indx] = A[high_indx], A[i+1]

    return i+1


def quicksort(A, low_indx, high_indx):
    if low_indx < high_indx:
        pivot_indx = partition(A, low_indx, high_indx)
        quicksort(A, low_indx, pivot_indx-1)
        quicksort(A, pivot_indx+1, high_indx)


def quick_sort(A):
    max_index = len(A)-1
    quicksort(A, 0, max_index)
    return A


A = [64, 34, 25, 12, 22, 11, 90]
print("\nInitial array")
for i in range(len(A)):
    print(A[i], end=" ")

print("\nSorted array")
sorted_A = quick_sort(A)
for i in range(len(sorted_A)):
    print(sorted_A[i], end=" ")
