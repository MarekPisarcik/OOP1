from node import Node


class LinkedList:
    def __init__(self, head:Node=None):
        self.head = head


    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while not current_node.next_node is None:
            current_node = current_node.next_node

        current_node.next_node = new_node


    def print_list(self):
        print("[", end="")

        if self.head is None:
            print("]")
            return

        current_node: Node = self.head
        while current_node is not None:
            print(current_node.value, end=",")
            current_node = current_node.next_node

        print("]")


    def insert_at_beginning(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    def pop(self):