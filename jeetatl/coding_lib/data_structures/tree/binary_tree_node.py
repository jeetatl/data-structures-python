class BinaryTreeNode:

    def __init__(self, value=None, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        return '{0} <-- [{1}] --> {2}'.format(
            (self.left.value if self.left is not None else None),
            self.value,
            (self.right.value if self.right is not None else None))

