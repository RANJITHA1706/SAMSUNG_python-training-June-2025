#Implement orange problem using quick sort 

def quick_sort(array,low,high):
    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort(array, low, pivot_index-1)
        quick_sort(array,pivot_index+1,high)
def partition(array,low,high):
    pivot = array[high]
    k = low-1
    for i in range(low, high):
        if array[i] < pivot:
            k += 1
            array[i], array[k] = array[k], array[i]
    array[k+1], array[high] = array[high], array[k+1]
    return k+1

array1 = list(map(int,input("Enter the array elements : ").split()))
low1 = 0
high1 = len(array1)-1
quick_sort(array1, low1, high1)
print("The sorted array is : ",array1)


#Learn efficiencies