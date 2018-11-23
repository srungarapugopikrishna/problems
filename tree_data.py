class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, node):
        if self.root is None:
            self.root = node
        else:
            nodes = [self.root]
            for temp in nodes:
                if temp.left is None:
                    temp.left = node
                    return
                elif temp.right is None:
                    temp.right = node
                    return
                else:
                    nodes.append(temp.left)
                    nodes.append(temp.right)

    def display(self, root):
        if root is not None:
            self.display(root.left)
            print root.data
            self.display(root.right)


tree = Tree()

# arr = [1, 2, 3, 4, 5, 6, 7]
arr = [10, 6, 15, 4, 8, 12, 18, 2, 5, 7, 9, 11, 14, 16, 19, 1, 3]
for val in arr:
    tree.add(Node(val))

root = tree.root
# tree.display(root)
