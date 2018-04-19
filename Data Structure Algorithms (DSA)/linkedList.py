class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
    
    def length(self):
        current_node = self.head
        sum = 0
        while current_node.next != None:
            sum += 1
            current_node = current_node.next
        return sum
    
    def display(self):
        elems = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elems.append(current_node.data)
        print elems

    def get(self, index):
        if index >= self.length():
            print "Get Index is Out of range"
            return None
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index:  return current_node.data
            current_index += 1
    
    def erase(self, index):
        if index >= self.length():
            print "Erase Index is Out of range"
            return
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1
                

sample_list = linked_list()

sample_list.append(1)
sample_list.append(5)
sample_list.append(7)
sample_list.append(1)
sample_list.append(9)


sample_list.erase(1)

sample_list.display()