from jeetatl.coding_lib.data_structures.tree.binary_tree_node import BinaryTreeNode
from jeetatl.coding_lib.data_structures.tree.tree_traversal import level_order, in_order


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BinaryTreeNode(value)
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

            # value not found
            if node.left is None:
                return

            # match found
            if value == node.left.value:
                if BinarySearchTree._is_leaf_node(node.left):
                    node.left = None
                elif BinarySearchTree._has_one_child_node(node.left):
                    if node.left.left is not None:
                        node.left = node.left.left
                    else:
                        node.left = node.left.right
                else:
                    node_to_remove = node.left
                    parent_of_current_predecessor = node_to_remove
                    current_predecessor = node.left.right

                    # find predecessor
                    while current_predecessor.right is not None:
                        parent_of_current_predecessor = current_predecessor
                        current_predecessor = parent_of_current_predecessor.right

                    node_to_remove.value = current_predecessor.value

                    if current_predecessor.left is None:
                        parent_of_current_predecessor.right = None
                    else:
                        parent_of_current_predecessor.right = current_predecessor.left
            else:
                BinarySearchTree._remove(node.left, value)
        elif value > node.value:

            # value not found
            if node.right is None:
                return

            # match found
            if value == node.right.value:
                if BinarySearchTree._is_leaf_node(node.right):
                    node.right = None
                elif BinarySearchTree._has_one_child_node(node.right):
                    if node.right.left is not None:
                        node.right = node.right.left
                    else:
                        node.right = node.right.right
                else:
                    node_to_remove = node.right
                    current_predecessor = node.right.left

                    if current_predecessor.right is None:
                        node_to_remove.value = current_predecessor.value
                        node_to_remove.left = current_predecessor.left
                    else:

                        # find predecessor
                        parent_of_current_predecessor = None
                        while current_predecessor.right is not None:
                            parent_of_current_predecessor = current_predecessor
                            current_predecessor = current_predecessor.right

                        node_to_remove.value = current_predecessor.value
                        parent_of_current_predecessor.right = current_predecessor.left
            else:
                BinarySearchTree._remove(node.left, value)
        else:
            if BinarySearchTree._is_leaf_node(node):
                node.left = None
            elif BinarySearchTree._has_one_child_node(node):
                if node.left is not None:
                    node.value = node.left.value
                else:
                    node.left = node.left.right
            else:
                node_to_remove = node
                current_predecessor = node.left

                if current_predecessor.right is None:
                    node_to_remove.value = current_predecessor.value
                    node_to_remove.left = current_predecessor.left
                else:
                    # find predecessor
                    parent_of_current_predecessor = None
                    while current_predecessor.right is not None:
                        parent_of_current_predecessor = current_predecessor
                        current_predecessor = current_predecessor.right

                    node_to_remove.value = current_predecessor.value
                    parent_of_current_predecessor.right = current_predecessor.left

    @staticmethod
    def _is_leaf_node(node):
        return (node.left is None) and (node.right is None)

    @staticmethod
    def _has_one_child_node(node):
        return (node.left is None) ^ (node.right is None)

    def insert_print(self, value):
        level_order(self.root, True)
        print('Inserting %s' % value)
        self.insert(value)
        level_order(self.root, True)
        print('')

    def search_print(self, value):
        level_order(self.root, True)
        print('Searching for %s. Found? ' % value, self.search(value))
        level_order(self.root, True)
        print('')

    def remove_print(self, value):
        level_order(self.root, True)
        print('Removing %s' % value)
        self.remove(value)
        level_order(self.root, True)
        print('')


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.search_print(20)
    bst.insert_print(20)

    print(str(bst.root))

    bst.search_print(20)
    bst.remove_print(20)
    bst.insert_print(20)
    bst.insert_print(10)
    bst.insert_print(5)
    bst.remove_print(5)
    bst.insert_print(5)
    bst.remove_print(10)
    bst.search_print(10)
    bst.search_print(5)

    bst.insert_print(11)
    bst.remove_print(5)

    bst.insert_print(5)
    bst.insert_print(15)

    bst.remove_print(11)

    bst.remove_print(5)

    bst.insert_print(14)
    bst.insert_print(16)
    bst.remove_print(15)

    bst.insert_print(25)
    bst.insert_print(22)
    bst.insert_print(27)

    bst.remove_print(20)