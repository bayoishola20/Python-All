class node:
    def __init__(self, value=None):
        self.value = value
        self.left = None #left child
        self.right = None #left child

class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = node(value)
        else:
            self.__insert(value, self.root)
    
    def __insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left == None:
                current_node.left = node(value)
            else:
                self.__insert(value, current_node.left)
        if value > current_node.value:
            if current_node.right == None:
                current_node.right = node(value)
            else:
                self.__insert(value, current_node.right)
        else:
            print "Value is in tree"
    
    def show_tree(self):
        if self.root != None:
            self.__show_tree(self.root)
    
    def __show_tree(self, current_node):
        if current_node != None:
            self.show_tree(current_node.left)
            print str(current_node.value)
            self.show_tree(current_node.right)


def add_to_tree(tree, num_elements=100, max_int=1000):
    from random import randint
    for _ in xrange(num_elements):
        current_element = randint(0, max_int)
        tree.insert(current_element)
    return tree

tree = binary_search_tree()
tree = add_to_tree(tree)

tree.show_tree()