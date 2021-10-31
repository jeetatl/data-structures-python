
def level_order(node):
    node_queue = []
    if node is None:
        print('(empty)')
    else:
        print(node.value, end='')

        if node.left is not None:
            node_queue.append(node.left)
        if node.right is not None:
            node_queue.append(node.right)

        while len(node_queue):
            current_node = node_queue.pop(0)
            print('->', node.value, end='')

            if current_node.left is not None:
                node_queue.append(current_node.left)
            if current_node.right is not None:
                node_queue.append(current_node.right)

        print('')
