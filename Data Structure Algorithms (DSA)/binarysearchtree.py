class node:
    def __init__(self, value=None): # Constructor
        self.value = value
        self.left = None #left child
        self.right = None #left child

class binary_search_tree:
    def __init__(self):
        self.root = None

    # Insert

    def insert(self, value):
        if self.root == None:
            self.root = node(value)
        else:
            self.__insert(value, self.root) # Private function
    
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
            self.__show_tree(current_node.left)
            print str(current_node.value)
            self.__show_tree(current_node.right)

    # Search
    def search(self, value):
        if self.root != None:
            return self.__search(value, self.root)
        else:
            return False
    
    def __search(self, value, current_node):
        if value == current_node.value:
            return True
        if value < current_node.value and current_node.left != None:
            return self.__search(value, current_node.left)
        if value > current_node.value and current_node.right != None:
            return self.__search(value, current_node.right)
        
        return False # Value not in tree

    # Find height
    def height(self):
        if self.root != None:
            return self.__height(self.root, 0)
        else:
            return 0
    
    def __height(self, current_node, current_height):
        if current_node == None:
            return current_height
        left_height = self.__height(current_node.left, current_height + 1)
        right_height = self.__height(current_node.right, current_height + 1)
        return max(left_height, right_height)

# Arbitrary data
def add_to_tree(tree, num_elements=10, max_int=50):
    from random import randint
    for _ in xrange(num_elements):
        current_element = randint(0, max_int)
        tree.insert(current_element)
    return tree

tree = binary_search_tree()
# tree = add_to_tree(tree)

tree.insert(0)
tree.insert(10)
tree.insert(13)
tree.insert(7)
tree.insert(99)
tree.insert(77)

tree.show_tree()

print "tree has a height of : {0}".format(tree.height())

print tree.search(7)
print tree.search(1)