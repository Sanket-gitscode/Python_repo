# Tree:
#
#         1
#        / \
#       2   3
#      /
#     4
#
# Minimum depth = 2
# Shortest path: 1 → 3


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root):
        if root is None:
            return 0

        # No left child → must go right
        if root.left is None:
            return 1 + self.minDepth(root.right)

        # No right child → must go left
        if root.right is None:
            return 1 + self.minDepth(root.left)

        # Both children exist
        return 1 + min(
            self.minDepth(root.left),
            self.minDepth(root.right)
        )


# Create the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)


# Find minimum depth
solution = Solution()
print(solution.minDepth(root))  # Output: 2
