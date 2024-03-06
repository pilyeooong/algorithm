class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def get(self, idx):
        find_node = self.head
        if idx == 0:
            return find_node
        else:
            for _ in range(idx):
                find_node = find_node.next 
                if find_node is None:
                    return None
                if find_node.next is None:
                    return find_node
            return find_node

    def insert(self, idx, value):
        new_node = Node(value)
        if idx == 0:
            prev_node = self.get(0)
            self.head = new_node
            new_node.next = prev_node
        else:
            prev_node = self.get(idx - 1)
            original_node = self.get(idx)
            new_node.next = original_node
            prev_node.next = new_node

    def remove_at(self, idx):
        pass

linked_list = LinkedList()
linked_list.append(3) # 0
linked_list.insert(1, 0)

print(linked_list.get(0).value)
print(linked_list.get(1).value)