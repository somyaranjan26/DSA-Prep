def target_sum(arr, target, l, r):
    while l <= r:
        if arr[l] + arr[r] == target:
            return l, r
        elif arr[l] + arr[r] > target:
            r = r - 1
        else:
            l = l + 1

arr = [1, 2, 3, 4, 5, 6, 7, 7, 10, 11]
target = 10

print(target_sum(arr, target, 0, len(arr)-1))

#   Time Complexity: O(n)

