#2.Find the frequency an element in a list of n elements.

list_size = int(input("Enter the size of the list : "))
element_list = []
for i  in range(list_size):
    element = input("Enter the element you want to enter : ")
    element_list.append(element)
element_find = input("Enter the element you want to find frequency : ")
frequency = element_list.count(element_find)
print(f"The frequency of element {element_find} is {frequency}")




