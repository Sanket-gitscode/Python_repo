from collections import deque

# ==========================================
# 1. BASIC BINARY TREE NODE
# ==========================================
class TreeNode:
    """Standard node structure for a binary tree."""
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


# ==========================================
# 2. TREE TRAVERSALS (DFS & BFS)
# ==========================================
# Let's assume 'root' is the starting node of a tree.

def pre_order_traversal(root):
    """Root -> Left -> Right"""
    res = []
    def dfs(node):
        if not node:
            return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return res

def in_order_traversal(root):
    """Left -> Root -> Right (For BST, this yields sorted order)"""
    res = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)
    dfs(root)
    return res

def post_order_traversal(root):
    """Left -> Right -> Root"""
    res = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        res.append(node.val)
    dfs(root)
    return res

def level_order_traversal(root):
    """Breadth-First Search (BFS) level by level from top to bottom."""
    if not root:
        return []
    
    res = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(current_level)
    return res


# ==========================================
# 3. BINARY SEARCH TREE (BST) IMPLEMENTATION
# ==========================================
class BinarySearchTree:
    """
    BST Property: For any node, all values in the left subtree 
    are less than the node's value, and all values in the right 
    subtree are greater.
    """
    def __init__(self):
        self.root = None

    def insert(self, val):
        """Public method to insert a value."""
        self.root = self._insert_recursive(self.root, val)

    def _insert_recursive(self, node, val):
        if not node:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert_recursive(node.left, val)
        elif val > node.val:
            node.right = self._insert_recursive(node.right, val)
        return node  # Duplicate values are ignored in this implementation

    def search(self, val):
        """Public method to search for a value. Returns True/False."""
        return self._search_recursive(self.root, val)

    def _search_recursive(self, node, val):
        if not node or node.val == val:
            return node is not None
        if val < node.val:
            return self._search_recursive(node.left, val)
        return self._search_recursive(node.right, val)

    def delete(self, val):
        """Public method to delete a value from the BST."""
        self.root = self._delete_recursive(self.root, val)

    def _delete_recursive(self, node, val):
        if not node:
            return None
        
        if val < node.val:
            node.left = self._delete_recursive(node.left, val)
        elif val > node.val:
            node.right = self._delete_recursive(node.right, val)
        else:
            # Case 1: No child or only one child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            # Case 2: Two children -> Get the inorder successor (smallest in the right subtree)
            temp = self._find_min(node.right)
            node.val = temp.val
            node.right = self._delete_recursive(node.right, temp.val)
            
        return node

    def _find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current


# ==========================================
# 4. COMMON UTILITY & TREE PROPERTIES
# ==========================================

def get_height(root):
    """Returns the maximum depth (height) of a tree."""
    if not root:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))

def lowest_common_ancestor_bst(root, p, q):
    """Finds LCA of two values (p and q) in a BST."""
    current = root
    while current:
        if p < current.val and q < current.val:
            current = current.left
        elif p > current.val and q > current.val:
            current = current.right
        else:
            return current.val
    return None


# ==========================================
# 5. EXECUTION & TESTING EXAMPLE
# ==========================================
if __name__ == "__main__":
    print("--- BUILDING BST ---")
    bst = BinarySearchTree()
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]
    for v in values_to_insert:
        bst.insert(v)
    print(f"Inserted values: {values_to_insert}")

    print("\n--- TRAVERSALS ---")
    print("In-Order (Sorted for BST):", in_order_traversal(bst.root))
    print("Pre-Order:", pre_order_traversal(bst.root))
    print("Post-Order:", post_order_traversal(bst.root))
    print("Level-Order (BFS):", level_order_traversal(bst.root))

    print("\n--- UTILITIES ---")
    print("Height of tree:", get_height(bst.root))
    print("Search for 40:", bst.search(40))
    print("Search for 99:", bst.search(99))
    print("LCA of 20 and 40:", lowest_common_ancestor_bst(bst.root, 20, 40))

    print("\n--- DELETION ---")
    print("Deleating node 30 (has two children)...")
    bst.delete(30)
    print("In-Order after deletion:", in_order_traversal(bst.root))
    print("Level-Order after deletion:", level_order_traversal(bst.root))