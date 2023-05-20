class Node:
    def __init__(self, data):
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

    def remove_node(self, i):
        if i == 1:
            self.head = self.head.next
            return
        curr_node = self.head
        prev_node = None
        count = 1
        while curr_node and count != i:
            prev_node = curr_node
            curr_node = curr_node.next
            count += 1
        if curr_node is None:
            return
        prev_node.next = curr_node.next

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

linked_list = LinkedList()
linked_list.append("A")
linked_list.append("B")
linked_list.append("C")
linked_list.append("D")
linked_list.remove_node(3)
linked_list.print_list()
