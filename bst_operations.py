from tree_data import bst_root as root
import sys


def in_order_traversal(root, result):
    if root is not None:
        in_order_traversal(root.left, result)
        result.append(root.data)
        in_order_traversal(root.right, result)
    return result


def check_bst_in_order(root):
    result = in_order_traversal(root, [])
    return result == sorted(result)


def check_bst_recursive(node, left, right):
    if node is None:
        return True
    print left, node.data, right
    if left >= node.data or node.data >= right:
        return False
    return check_bst_recursive(node.left, left, node.data) and check_bst_recursive(node.right, node.data, right)


print check_bst_in_order(root)
print check_bst_recursive(root, (-sys.maxsize-1), sys.maxsize)