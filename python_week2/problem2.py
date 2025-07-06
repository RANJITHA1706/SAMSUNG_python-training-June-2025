#Cloud computing 
numofReq = int(input("Enter the number of requests :"))
requests = [int(input("Enter the requests  ")) for i in range (0,numofReq)]
sum = 0
for i in range(0,len(requests),2):
    sum += int(requests[i])
print("The memory allocated by server 1 is",sum)