"""
Solution
"""

class TreeNode:
    """ Tree Node
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """ Solution
    """

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """ Deletes a node from the BST.

        Args:
            root (TreeNode): Root of the tree.
            key (int): Node value to be deleted.

        Returns:
            TreeNode: Root of the tree after deletion.
        """

        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None

            if not root.left:
                return root.right

            if not root.right:
                return root.left

            max_left_child = root.left
            while max_left_child.right:
                max_left_child = max_left_child.right

            root.val = max_left_child.val
            root.left = self.deleteNode(root.left, max_left_child.val)

        return root
