"""
Solution
"""

class TreeNode:
    """ Tree Node
    """

    def __init__(self, val = 0, left = None, right = None):
        self.data = val
        self.left = left
        self.right = right

def pre_order(root: TreeNode) -> list[int]:
    """ Pre-order traversal of a binary tree.

    Args:
        root (TreeNode): Root of the binary tree.

    Returns:
        list[int]: List of node values in pre-order traversal.
    """

    if not root:
        return []

    pre_order_traverse = []

    def traverse(node: TreeNode):
        if not node:
            return

        pre_order_traverse.append(node.data)

        if node.left:
            traverse(node.left)

        if node.right:
            traverse(node.right)

    traverse(root)

    return pre_order_traverse

# In-order traversal
def in_order(root: TreeNode) -> list[int]:
    """ In-order traversal of a binary tree.

    Args:
        root (TreeNode): Root of the binary tree.

    Returns:
        list[int]: List of node values in in-order traversal.
    """

    if not root:
        return []

    pre_order_traverse = []

    def traverse(node):
        if not node:
            return

        if node.left:
            traverse(node.left)

        pre_order_traverse.append(node.data)

        if node.right:
            traverse(node.right)

    traverse(root)

    return pre_order_traverse

# Post-order traversal
def post_order(root: TreeNode) -> list[int]:
    """ Post-order traversal of a binary tree.

    Args:
        root (TreeNode): Root of the binary tree.

    Returns:
        list[int]: List of node values in Post-order traversal.
    """

    if not root:
        return []

    pre_order_traverse = []

    def traverse(node):
        if not node:
            return

        if node.left:
            traverse(node.left)

        if node.right:
            traverse(node.right)

        pre_order_traverse.append(node.data)

    traverse(root)

    return pre_order_traverse
