l1 = [1, 43, 3, 2]
l3 = [1, 43, 3, 2]
l2 = [1, 2, 5, 4, 3, 9]

print(l1 > l2)
print(l1 != l2)
print(l1 != l3)


l2 = [1, 2, 5, 4, 3, 9]

print(l2[:])
print(l2[::])
print(l2[0:])
print(l2[0:-1])
print(l2[0:-1:])

l2 = [1, 2, 5, 4, 3, 9]
print(l2[1:10]) # start from index 1 and go till index 9
print(l2[::2]) # Consider entire list and override the increment to 2
print(l2[::1]) # Defining the default behavior differently
print(l2[::-1]) # Consider entire list but decrement by 1 (increment by -1)
print(l2[1:-1:-1]) 