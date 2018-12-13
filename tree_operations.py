from tree_data import Tree, root


def bfs(root):
    node_stack = []
    temp = root
    node_stack.append(temp)
    height = 0
    flag = True
    while flag:
        limit = pow(2, height)
        for i in range(0, limit):
            if node_stack:
                temp = node_stack.pop(0)
                print height, temp.data
                if temp.left is not None:
                    node_stack.append(temp.left)
                if temp.right is not None:
                    node_stack.append(temp.right)
            else:
                flag = False
        height += 1


def connect_nodes_at_same_level(root):
    node_stack = []
    temp = root
    node_stack.append(temp)
    height = 0
    flag = True
    while flag:
        current_nodes = []
        limit = pow(2, height)
        for i in range(0, limit):
            if node_stack:
                temp = node_stack.pop(0)
                current_nodes.append(temp)
                # print height, temp.data
                if temp.left is not None:
                    node_stack.append(temp.left)
                if temp.right is not None:
                    node_stack.append(temp.right)
            else:
                flag = False
        print '->'.join([str(node.data) for node in current_nodes])+'->NULL'
        height += 1


def left_side_view(root):
    node_stack = []
    temp = root
    node_stack.append(temp)
    height = 0
    flag = True
    while flag:
        current_nodes = []
        limit = pow(2, height)
        for i in range(0, limit):
            if node_stack:
                temp = node_stack.pop(0)
                current_nodes.append(temp)
                # print height, temp.data
                if temp.left is not None:
                    node_stack.append(temp.left)
                if temp.right is not None:
                    node_stack.append(temp.right)
            else:
                flag = False
        print [node.data for node in current_nodes][0]
        height += 1


def right_side_view(root):
    node_stack = []
    temp = root
    node_stack.append(temp)
    height = 0
    flag = True
    while flag:
        current_nodes = []
        limit = pow(2, height)
        for i in range(0, limit):
            if node_stack:
                temp = node_stack.pop(0)
                current_nodes.append(temp)
                # print height, temp.data
                if temp.left is not None:
                    node_stack.append(temp.left)
                if temp.right is not None:
                    node_stack.append(temp.right)
            else:
                flag = False
        print [node.data for node in current_nodes][-1]
        height += 1


def find_node(node, val, height):
    if node.data == val:
        return True, height
    if node.left is not None and node.right is not None:
        left = find_node(node.left, val, height+1)
        right = find_node(node.right, val, height+1)
        if left[0]:
            return left
        else:
            return right
    elif node.left is not None:
        return find_node(node.left, val, height+1)
    elif node.right is not None:
        return find_node(node.right, val, height+1)
    return False, height


def find_least_common_ancestor(root, node1, node2, height):
    node_stack = []
    temp = root
    node_stack.append(temp)
    height = 0
    flag = True
    current_nodes = []
    while flag:

        limit = pow(2, height)
        for i in range(0, limit):
            if node_stack:
                temp = node_stack.pop(0)
                current_nodes.append(temp)
                # print height, temp.data
                if temp.left is not None:
                    node_stack.append(temp.left)
                if temp.right is not None:
                    node_stack.append(temp.right)
            else:
                flag = False
    result = None
    min_val = 10000
    for node in current_nodes:
        result1 = find_node(node, node1, height)
        result2 = find_node(node, node2, height)
        if result1[0] and result2[0]:
            if min_val > result1[1]+result2[1]:
                result = node.data
                min_val = result1[1]+result2[1]
    return result

# bfs(root)
# connect_nodes_at_same_level(root)
# left_side_view(root)
# right_side_view(root)
print find_least_common_ancestor(root, 16, 8, 0)
