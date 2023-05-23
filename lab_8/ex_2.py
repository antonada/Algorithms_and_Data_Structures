class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def delete_node(self, index):
        if index == 1:
            self.head = self.head.next
            return
        current_node = self.head
        previous_node = None
        i = 1
        while current_node and i != index:
            previous_node = current_node
            current_node = current_node.next
            i += 1
        if current_node is None:
            return
        previous_node.next = current_node.next

linked_list = LinkedList()
linked_list.append("A")
linked_list.append("B")
linked_list.append("C")
linked_list.append("D")
linked_list.print_list() 
linked_list.delete_node(2)
linked_list.print_list() 