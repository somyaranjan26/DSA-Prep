def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    if target not in arr:
        return "Not in array"

    while low <= high:
        mid = low + ((high - low) // 2)

        if arr[mid] == target:
            return mid

        if target < arr[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return "Not Found"

arr = [1, 2, 3, 5, 6, 7, 7, 10, 11]
target = 3

print(binary_search(arr, target))


