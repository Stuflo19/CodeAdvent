import Node as n

class Binary_Tree:
    def __init__(self):
        self.root = None

    def create_tree(self, value):
        if type(value) == int:
            return n.Node(None, None, value)
        
        left_node = self.create_tree(value[0])
        right_node = self.create_tree(value[1])

        self.root = n.Node(left_node, right_node, None)
        left_node.parent = self.root
        right_node.parent = self.root

        return self.root

    def add_new_tree(self, old, new):
        new_root = n.Node(old, new, None)

        old.parent = new_root
        new.parent = new_root

        self.root = new_root
