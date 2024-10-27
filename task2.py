def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return iterations, arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    return iterations, upper_bound

# Тестування
arr = [1.2, 2.5, 3.8, 4.1, 5.7, 6.2, 7.9, 8.3, 9.1]
target = 6.0
iterations, upper_bound = binary_search(arr, target)
print(f"Кількість ітерацій: {iterations}")
print(f"Верхня межа: {upper_bound}")
