#implement binary search iteratively
search_array = list(map(int,input("Input the elements in the array : ").split()))
target = int(input("Enter you target element :"))
search_array.sort()
n = len(search_array)
low = 0
high = n-1
while True:
    if low > high:
        break
    mid = (low + high) //2
    if search_array[mid] == target:
        print(mid)
        break 
    elif search_array[mid] < target :
        low = mid +1
    else:
        high = mid - 1