#1. Find smallest and biggest elements in an list of n numbers.
length = int(input("Enter the length of the list : "))
numbers_list = []
for i in range(length):
    number = int(input("Enter the number you want to add to the list : "))
    numbers_list.append(number)
numbers_list.sort()
print("The smallest number in the list is : ",numbers_list[0])
print("The Biggest number in the list is : ",numbers_list[-1])
