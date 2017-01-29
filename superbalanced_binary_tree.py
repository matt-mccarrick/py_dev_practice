#Given a binary tree, tell whether the tree is "superbalanced"
#"superbalanced" means that there are no leaves with a difference in depth
#greater than 1

#baseclass
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

#something like this. Not super confident, yet
def is_balanced(node):
    #-1 is error value.
    return check_height(node)>0
def check_height(node):
    if not node:
        return -1
    left_height = check_height(node.left)
    right_height = check_height(node.right)

    height_diff = abs(left_height - right_height)
    if height_diff > 1:
        return -1
    else:
        return max(left_height, right_height) + 1
