def insertion_sort(A):
    for i in range(1, len(A)):
        curr_val = A[i]
        j = i-1
        while j >= 0 and A[j] > curr_val:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = curr_val

    return A


A = [64, 25, 12, 22, 11]
print("\nInitial array")
for i in range(len(A)):
    print(A[i], end=" ")

print("\nSorted array")
sorted_A = insertion_sort(A)
for i in range(len(sorted_A)):
    print(sorted_A[i], end=" ")

