def counting_sort(input_arr, exp):
    sorted_arr = [0] * len(input_arr)
    count_arr = [0] * 10 # for 9 digits

    for i in range(len(input_arr)):
        index = (input_arr[i] // exp) % 10
        count_arr[index] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    for i in range(len(input_arr)-1, -1, -1):
        index = (input_arr[i] // exp) % 10
        sorted_arr[count_arr[index] - 1] = input_arr[i]
        count_arr[index] -= 1

    for i in range(len(input_arr)):
        input_arr[i] = sorted_arr[i]


def radix_sort(arr_input):
    max_val = max(arr_input)
    # exp = 10 ^ i where i is current digit number
    exp = 1
    while max_val / exp >= 1:
        counting_sort(arr_input, exp)
        exp *= 10


A = [170, 45, 75, 90, 802, 24, 2, 66]
print("\nInitial array")
for i in range(len(A)):
    print(A[i], end=" ")

radix_sort(A)
print("\nSorted array")
for i in range(len(A)):
    print(A[i], end=" ")

