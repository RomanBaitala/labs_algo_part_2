class BinaryTree: 
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def max_tree_depth(tree):
    if not tree:
        return 0
    return 1 + max(max_tree_depth(tree.left), max_tree_depth(tree.right))


def tree_diameter(tree, diameter):
    if not tree: 
        return None
    cur_diameter = 0 
    if tree.left and tree.right:
        left = max_tree_depth(tree.left)
        right = max_tree_depth(tree.right)
        cur_diameter = left + right
        if diameter[0] < cur_diameter:
            diameter[0] = cur_diameter
    tree_diameter(tree.left, diameter)
    tree_diameter(tree.right, diameter)


def max_tree_diameter(tree):
    diameter = [0]
    tree_diameter(tree, diameter)
    return diameter[0]
