# Palindrome Partitioning program
def palindrome_partition(s):
    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, path):
        if start == len(s):
            result.append(list(path))
            return
        for end in range(start + 1, len(s) + 1):
            if is_palindrome(s[start:end]):
                path.append(s[start:end])
                backtrack(end, path)
                path.pop()

    result = []
    backtrack(0, [])
    return result


user_input = input("Enter a string to partition into palindromes: ").strip()


partitions = palindrome_partition(user_input)

print(f"\nFound {len(partitions)} palindrome partitions:")
for idx, part in enumerate(partitions, 1):
    print(f"{idx}. {part}")
