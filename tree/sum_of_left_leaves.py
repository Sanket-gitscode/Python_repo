class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_left_leaves(root):

    def helper(node, is_left):

        if node is None:
            return 0

        if node.left is None and node.right is None:
            if is_left:
                return node.val
            return 0

        return helper(node.left, True) + helper(node.right, False)

    return helper(root, False)


# Creating the tree
root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.right = TreeNode(6)


# Get the answer
print(sum_left_leaves(root))


