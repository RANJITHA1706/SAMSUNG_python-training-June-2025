#Implement Selection Sort
arr = list(map(int,input("Enter the elements of the array : ").split()))
n = len(arr)
for i in range(1,n):
    element = arr[i-1]
    position = i-1
    for j in range(i-1,n):
        if arr[j] <element :
            element = arr[j]
            position = j 
    arr[position], arr[i-1] = arr[i-1], arr[position]
print("The sorted array is ",arr)