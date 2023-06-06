def bubble_sort(A):
    for i in range(len(A)):
        swapped = False
        for j in range(len(A)-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swapped = True
        if not swapped:
            break
    return A


A = [64, 34, 25, 12, 22, 11, 90]
print("\nInitial array")
for i in range(len(A)):
    print(A[i], end=" ")

print("\nSorted array")
sorted_A = bubble_sort(A)
for i in range(len(sorted_A)):
    print(sorted_A[i], end=" ")