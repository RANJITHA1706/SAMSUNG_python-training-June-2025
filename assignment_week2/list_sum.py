#3. Find sum of list elements
def list_sum(element_list):
    if len(element_list) == 0:
        return 0
    else:
        return element_list[0] + list_sum(element_list[1:])
new_list = list(map(int,input("Enter the list elements seperated by space :").split()))
print("The sum of list elements is ",list_sum(new_list))

   