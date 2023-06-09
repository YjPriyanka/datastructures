def merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2
        left_list = A[:mid]
        right_list = A[mid:]

        merge_sort(left_list)
        merge_sort(right_list)

        i = j = k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] <= right_list[j]:
                A[k] = left_list[i]
                i += 1
            else:
                A[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            A[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            A[k] = right_list[j]
            j += 1
            k += 1

    return A


A = [64, 34, 25, 12, 22, 11, 90]
print("\nInitial array")
for i in range(len(A)):
    print(A[i], end=" ")

print("\nSorted array")
sorted_A = merge_sort(A)
for i in range(len(sorted_A)):
    print(sorted_A[i], end=" ")
