class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def height(root):
    if root is None:
        return -1  # height in terms of edges
    left_height = height(root.left)
    right_height = height(root.right)
    return 1 + max(left_height, right_height)

# 👇 Reading input and running the solution
if __name__ == "__main__":
    n = int(input())  # Number of nodes
    values = list(map(int, input().split()))  # Insertion order
    root = None
    for val in values:
        root = insert(root, val)
    print(height(root))

