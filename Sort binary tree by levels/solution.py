"""
Solution 
"""

from collections import deque

class TreeNode:
    """ Tree Node
    """

    def __init__(self, val = 0, left = None, right = None):
        self.data = val
        self.left = left
        self.right = right

def tree_by_levels(root: TreeNode) -> list[int]:
    """ Sorts tree by levels.

    Args:
        root (TreeNode): Root of the tree.

    Returns:
        list[int]: Sorted tree by levels.
    """

    if not root:
        return []

    sorted_levels = []

    queue = deque([root])

    while queue:
        curr_node = queue.popleft()

        sorted_levels.append(curr_node.value)

        if curr_node.left:
            queue.append(curr_node.left)

        if curr_node.right:
            queue.append(curr_node.right)

    return sorted_levels
