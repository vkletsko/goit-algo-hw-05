import math


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    counter = 0

    while left <= right:
        mid = left + (right - left) // 2
        counter += 1

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return counter, arr[mid]

    if left < len(arr):
        upper_bound = arr[left]
    else:
        upper_bound = None

    return counter, upper_bound


length = 10
sorted_array = [math.sqrt(i) for i in range(1, length)]
print(f"Відсортований масив: {sorted_array}")

target_value = 1.1

iterations, upper_bound = binary_search(sorted_array, target_value)

print(f"Кількість ітерацій: {iterations}")
print(f"Верхня межа: {upper_bound}")
