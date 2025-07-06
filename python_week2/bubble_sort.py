#Implement bubble sort
def bubble_sort(arr,n):
    for i in range(n):
        for j in range(n-1-i):
            if arr[j] >arr[j+1]:
                arr[j], arr[j+1] = arr[j+1] ,arr[j]
    return arr
arr1 = list(map(int,input("Enter the elements of the array : ").split()))
m = len(arr1)
result = bubble_sort(arr1, m)
print("The sorted Array is : ",result)
