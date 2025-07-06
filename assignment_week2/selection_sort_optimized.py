#Implement an optimized selection sort algorithm
def optimized_selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
arr = [64, 25, 12, 22, 11]
sorted_arr = optimized_selection_sort(arr)
print("Optimized Sorted array:", sorted_arr)
