#Clock rotation
def isSameReflection(word1, word2):
    if word2 in (word1 + word1):
        return 1
    else :
        return -1
original_str = input("Enter the word you want to rotate")
word2 = input("Enter the word you want to check in : ")
result=isSameReflection(original_str, word2)
print(result)
