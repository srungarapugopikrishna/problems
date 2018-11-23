from tree_data import root
from tree_data import Node
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


def display_inorder_recursive(root):
    if root is not None:
        display_inorder_recursive(root.left)
        print root.data
        display_inorder_recursive(root.right)


def display_inorder_iterative(root):
    nodes = [root]
    temp = root
    while nodes:
        if temp.left is not None:
            temp = temp.left
            nodes.append(temp)
            continue
        # while temp.left is not None:
        #     temp = temp.left
        #     nodes.append(temp)
        node = nodes.pop()
        print node.data
        if node.right is not None:
            nodes.append(node.right)
            temp = nodes[-1]

# print check_bst_in_order(root)
# print check_bst_recursive(root, (-sys.maxsize-1), sys.maxsize)
# print search_key(root, 5)
# print insert_key(root, 10)
# display_inorder_recursive(root)
display_inorder_iterative(root)