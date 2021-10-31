from jeetatl.coding_lib.data_structures.tree.binary_tree_node import BinaryTreeNode
from jeetatl.coding_lib.data_structures.tree.tree_traversal import level_order


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
            return BinarySearchTree._remove(self.root, value)
        return False

    @staticmethod
    def _remove(node, value):
        if value < node.value:
            if node.left is None:
                return
            if value == node.left.value:    # match found
                if BinarySearchTree._is_leaf_node(node.left):
                    node.left = None
                elif BinarySearchTree._has_one_child_node(node.left):
                    if node.left.left is None:
                        node.left = node.left.left
                    else:
                        node.left = node.left.right
                else:
                    parent = node.left
                    current_predecessor = parent.right

                    # find predecessor
                    while current_predecessor.right is not None:
                        parent = current_predecessor.right
                        current_predecessor = parent.right

                    node.value = current_predecessor.value

                    if current_predecessor.left is None:
                        parent.right = None
                    else:
                        parent.right = current_predecessor.left
            else:
                BinarySearchTree._remove(node.left, value)
        elif value > node.value:
            return
            # if node.right is None:
            #     return
            # if value == node.right.value:  # match found
            #     if BinarySearchTree._is_leaf_node(node.right):
            #         node.right = None
            #     elif BinarySearchTree._has_one_child_node(node.right):
            #         if node.right.left is None:
            #             node.right = node.right.left
            #         else:
            #             node.right = node.right.right
            #     else:
            #         parent = node.left
            #         current_predecessor = parent.right
            #
            #         # find predecessor
            #         while current_predecessor.right is not None:
            #             parent = current_predecessor.right
            #             current_predecessor = parent.right
            #
            #         node.value = current_predecessor.value
            #
            #         if current_predecessor.left is None:
            #             parent.right = None
            #         else:
            #             parent.right = current_predecessor.left
            # else:
            #     BinarySearchTree._remove(node.right, value)
        return

    @staticmethod
    def _is_leaf_node(node):
        return (node.left is None) and (node.right is None)

    @staticmethod
    def _has_one_child_node(node):
        return (node.left is None) ^ (node.right is None)


if __name__ == '__main__':
    bst = BinarySearchTree()
    level_order(bst.root)
    print("Search for 20: %s" % bst.search(20))
    bst.insert(20)
    level_order(bst.root)
    print("Search for 20: %s" % bst.search(20))
    bst.remove(20)
    level_order(bst.root)
    print("Search for 20: %s" % bst.search(20))
