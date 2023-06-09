# FOR POSITIVE INTEGERS
def print_count_arr(count_arr):
    print("\ncount array: ")
    for i in range(len(count_arr)):
        print(count_arr[i], end=" ")


def counting_sort(A):
    max_element = A[0]
    for i in range(len(A)):
        if A[i] > max_element:
            max_element = A[i]
    #print("\nmax_element:", max_element)

    count_arr = [0] * (max_element + 1)
    #print_count_arr(count_arr)

    for i in range(len(A)):
        count_arr[A[i]] += 1
    #print_count_arr(count_arr)

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
    #print_count_arr(count_arr)

    sorted_arr = [0] * len(A)
    for i in range(len(A)):
        sorted_arr[count_arr[A[i]] - 1] = A[i]
        count_arr[A[i]] -= 1

    return sorted_arr


A = [64, 34, 25, 12, 22, 11, 90]
print("\nInitial array")
for i in range(len(A)):
    print(A[i], end=" ")

sorted_A = counting_sort(A)
print("\nSorted array")
for i in range(len(sorted_A)):
    print(sorted_A[i], end=" ")



