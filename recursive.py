def binary_seacrh_helper(arr, target, low, high):

    if low > high:
        return "Not in array"

    mid = low + ((high - low) // 2)

    if arr[mid] == target:
        return mid
    
    elif arr[mid] > target:
        binary_seacrh_helper(arr, target, low, mid-1)
    
    else:
        binary_seacrh_helper(arr, target, mid+1, high)

def binary_seacrh(arr, target):
    return binary_seacrh_helper(arr, target, 0, (len(arr)-1))

arr = [1, 2, 3, 5, 6, 7, 7, 10, 11]
target = 4

binary_seacrh(arr, target)
