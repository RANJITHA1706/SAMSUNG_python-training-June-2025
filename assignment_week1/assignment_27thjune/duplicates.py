#3.3. Remove the duplicates in a list of size n
length = int(input("Enter the length of the list : "))
element_list = []
for i in range(length):
    element = input("Enter the element you want to enter : ")
    element_list.append(element)
print("The list before removing duplicates : ",element_list)
unique_list = []
for element in element_list:
    if element not in unique_list:
        unique_list.append(element)
print("The element after removig duplicates : ",unique_list)