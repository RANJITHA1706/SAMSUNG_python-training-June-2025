# Subset Sum Problem 
def subset_sum(nums, target):
    def backtrack(i, total):
        if total == target:
            return True
        if i >= len(nums) or total > target:
            return False
        return backtrack(i + 1, total + nums[i]) or backtrack(i + 1, total)

    return backtrack(0, 0)


try:
    nums = list(map(int, input("Enter a list of integers (space-separated): ").split()))
    target = int(input("Enter the target sum: "))

    if subset_sum(nums, target):
        print(" A subset exists that sums to the target.")
    else:
        print(" No subset found that sums to the target.")
except ValueError:
    print("Invalid input. Please enter integers only.")
