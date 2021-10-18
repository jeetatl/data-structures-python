from jeetatl.coding_lib.data_structures.tree.binary_tree_node import BinaryTreeNode


class BinarySearchTree:

    def __init__(self):
        self.root = BinaryTreeNode()

    def insert(self, value):
        if self.root.value is None:
            self.root.value = value
        else:
            self._insert_helper(self.root, value)

    def _insert_helper(self, start_node, value):
        if value == start_node.value:
            return
        elif value < start_node.value:
            if start_node.left is None:
                new_node = BinaryTreeNode(value)
                start_node.left = new_node
            else:
                self._insert_helper(start_node.left, value)
        else:
            if start_node.right is None:
                new_node = BinaryTreeNode(value)
                start_node.right = new_node
            else:
                self._insert_helper(start_node.right, value)

    def search(self, value):
        if self.root is None:
            return False
        else:
            return self._search_helper(self.root, value)

    def _search_helper(self, node, value):
        if node.value is None:
            return False
        elif value > node.value:
            if node.right is None:
                return False
            else:
                return self._search_helper(node.right, value)
        elif value < node.value:
            if node.left is None:
                return False
            else:
                return self._search_helper(node.left, value)
        else:
            return True

    def remove(self, value):
        if self.root is not None:
            return self._remove(value)
        return False

    @staticmethod
    def _remove(node, value):
        return

    @staticmethod
    def _is_leaf_node(node):
        return node.left is None and node.right is None



if __name__ == '__main__':
    bst = BinarySearchTree()
    print("Search for 20: %s" % bst.search(20))
    bst.insert(20)
    print("Search for 20: %s" % bst.search(20))
