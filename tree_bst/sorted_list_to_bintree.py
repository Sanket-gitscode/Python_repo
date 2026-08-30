class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: list[int]):
    def helper(left, right):
        if left > right:
            return None
        
        # Find the middle element to keep the tree balanced
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        
        # Recursively build left and right subtrees
        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)
        
        return root
        
    return helper(0, len(nums) - 1)


print(sortedArrayToBST([1,2,3,4,5,6,7,8]))


from collections import deque

def print_tree(root):
    if not root:
        print("Empty Tree")
        return
    
    queue = deque([root])
    result = []
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("None")
            
    # Remove trailing None values for a cleaner output
    while result and result[-1] == "None":
        result.pop()
        
    print(result)

# Run it with your function
root = sortedArrayToBST([1, 2, 3, 4, 5, 6, 7, 8])
print_tree(root)