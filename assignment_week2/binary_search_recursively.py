#Implement binary search recursively
def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  # Base case: element not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)
arr1 = [1,4,7,9,3,4,5,2]
target1 = 7
low1 = 0
high1 = len(arr1)-1
a = binary_search_recursive(arr1, target1, low1, high1)
print(a)    

