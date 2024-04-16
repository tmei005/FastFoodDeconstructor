import string
import Node
class HashMap:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, menu_item):
        ascii_sum = 0
        for c in menu_item.restaurant:
            ascii_sum += ord(c)
        for c in menu_item.category:
            ascii_sum += ord(c)
        return ascii_sum % self.capacity

    def insert(self, menu_item):
        index = hash(menu_item)
        if self.table[index] is None:
            self.table[index] = menu_item
            self.size += 1
        else:
            new_node = menu_item
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1