RED = True
BLACK = False


class Node:
    def __init__(self, value, priority, parent=None, left=None, right=None, color=RED):
        self.value = value
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent 
        self.priority = priority


class RedBlackTree:
    def __init__(self):
        self.root = None

    def left_roatate(self, x):
        y = x.right 
        x.right = y.left 
        y.parent = x.parent 

        if y.left is not None:
            y.left.parent = x

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y 
        else:
            x.parent.right = y

        y.left = x 
        x.parent = y


    def right_rotate(self, x):
        y = x.left 
        x.left = y.right 
        y.parent = x.parent 

        if y.right is not None:
            y.right.parent = x

        if x.parent is None:
            self.root = y 
        elif x == x.parent.left:
            x.parent.left = y 
        else:
            x.parent.right = y

        y.right = x
        x.parent = y 

    def insert(self, value, priority):
        z = Node(value, priority)
        y = None
        x = self.root

        if self.root is None:
            self.root = Node(value, priority, color=BLACK)
            return
        
        while x is not None:
            y = x
            if priority >= x.priority:
                x = x.left 
            else: 
                x = x.right

        z.parent = y 

        if priority >= y.priority:
            y.left = z 
        else: 
            y.right = z 

        self.insert_fix(z)

    def insert_fix(self, z):
        while z.parent and z.parent.color == RED:
            if z.parent.parent.left == z.parent: 
                if z.parent.parent.right and z.parent.parent.right.color == RED:
                    z.parent.color = BLACK
                    z.parent.parent.right.color = BLACK
                    z.parent.parent.color = RED 
                    z = z.parent.parent
                else: 
                    if z == z.parent.right:
                        z = z.parent
                        self.left_roatate(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.right_rotate(z.parent.parent)
            else: 
                if z.parent.parent.left and z.parent.parent.left.color == RED:
                    z.parent.parent.left.color = BLACK
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent 
                else:
                    if z == z.parent.left:
                        z = z.parent 
                        self.right_rotate(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.left_roatate(z.parent.parent)
            if z == self.root:
                break
        self.root.color = BLACK

    def delete(self):
        z = self.search()
        node_to_be_deleted = z
        z_color = z.color

        if z.left is None:
            if z.parent.left == z: 
                z.parent.left = z.right
            else: 
                z.parent.right = z.right
            if z.right is not None:
                z.right.parent = z.parent
            z = z.right
        if z_color == BLACK:
            self.delete_fix(z)
        return node_to_be_deleted.priority

    def delete_fix(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.parent.left: 
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.left_roatate(x.parent)
                    w = x.parent.right
                    if w.left.color == BLACK and w.right.color == BLACK:
                        w.color = RED
                        x = x.parent
                    elif w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self.right_rotate(w)
                        w = x.parent.right
                    else:
                        w.color = x.parent.color 
                        x.parent.parent.color = BLACK
                        w.right = BLACK
                        self.left_roatate(x.parent)
                        self.root = x
            else:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.left_roatate(x.parent)
                    w = x.parent.left
                    if w.right.color == BLACK and w.left.color == BLACK:
                        w.color = RED
                        x = x.parent
                    elif w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.right_rotate(w)
                        w = x.parent.left
                    else:
                        w.color = x.parent.color 
                        x.parent.parent.color = BLACK
                        w.left = BLACK
                        self.left_roatate(x.parent)
                        self.root = x
        x.color = BLACK

    def search(self):
        node = self.root

        while node.left:
            node = node.left

        return node

    def inorder_tree(self, node):
        if node is None:
            return

        self.inorder_tree(node.left)
        print(node.color)
        print(node.priority)
        self.inorder_tree(node.right)
