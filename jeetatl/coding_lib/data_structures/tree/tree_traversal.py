
def level_order(node, print_prefix=False):
    node_queue = []
    if print_prefix:
        print('Level Order Traversal: ', end='')

    if node is None:
        print('(empty)')
    else:
        print('[Level 0] ', end='')
        print(node.value, end='')
        node_queue.append(1)

        if node.left is not None:
            node_queue.append(node.left)
        if node.right is not None:
            node_queue.append(node.right)

        while len(node_queue):
            current_item = node_queue.pop(0)
            if type(current_item) == int:
                if len(node_queue):
                    print(' -> [Level {0}]'.format(current_item), end='')
                    current_item += 1
                    node_queue.append(current_item)
                    continue
                else:
                    break

            print(' ->', current_item.value, end='')

            if current_item.left is not None:
                node_queue.append(current_item.left)
            if current_item.right is not None:
                node_queue.append(current_item.right)

        print('')


def in_order(node, print_prefix=False):
    if print_prefix:
        print('In Order Traversal: ', end='')

    if node is None:
        print('(empty)')
    else:
        _in_order_helper(node)


def _in_order_helper(node):
    if node.left is not None:
        _in_order_helper(node.left)

    print(node.value, '-> ', end='')

    if node.right is not None:
        _in_order_helper(node.right)
