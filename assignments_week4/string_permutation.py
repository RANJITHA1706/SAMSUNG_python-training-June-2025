#Permutations of a String
def permute_string(s):
    def backtrack(path, used):
        if len(path) == len(s):
            result.append("".join(path))
            return
        for i in range(len(s)):
            if used[i]:
                continue
            used[i] = True
            path.append(s[i])
            backtrack(path, used)
            path.pop()
            used[i] = False

    result = []
    backtrack([], [False]*len(s))
    return result


user_input = input("Enter a string to find its permutations: ").strip()


permutations = permute_string(user_input)
print(f"\nTotal permutations: {len(permutations)}")
for i, perm in enumerate(permutations, 1):
    print(f"{i}. {perm}")
