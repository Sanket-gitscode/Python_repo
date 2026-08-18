# -----------------------------
# 1. Create a TreeNode class
# -----------------------------

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# -----------------------------
# 2. Your isSameTree function
# -----------------------------

def isSameTree(p, q):

    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# -----------------------------
# 3. Create Tree 1
#
#        1
#       / \
#      2   3
# -----------------------------

tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)


# -----------------------------
# 4. Create Tree 2
#
#        1
#       / \
#      2   3
# -----------------------------

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)


# -----------------------------
# 5. Test our function
# -----------------------------

result = isSameTree(tree1, tree2)

print(result)
