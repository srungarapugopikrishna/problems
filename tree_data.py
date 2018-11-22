class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


bst_root = Node(15)
bst_root.left = Node(7)
bst_root.right = Node(35)
bst_root.left.left = Node(4)
bst_root.left.right = Node(9)
bst_root.left.left.left = Node(2)
bst_root.left.left.right = Node(5)
bst_root.left.right.left = Node(8)
bst_root.right.left = Node(22)
bst_root.right.right = Node(96)
bst_root.right.left.right = Node(30)
bst_root.right.right.left = Node(72)
bst_root.right.right.right = Node(103)
