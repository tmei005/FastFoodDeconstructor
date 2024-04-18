import string
import Node
class HashMap:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.load_factor = .75
        self.map = [None] * capacity
        print(self.capacity)

    def _hash(self, menu_item):
        ascii_sum = sum(ord(c) for c in menu_item.category) + sum(ord(c) for c in menu_item.restaurant)
        return ascii_sum % self.capacity

    def _rehash(self):
        # Double the capacity
        new_capacity = self.capacity * 2
        new_map = [None] * new_capacity

        # Re-insert existing items into the new map
        for item in self.map:
            current = item
            while current is not None:
                new_index = self._hash(current.menu_item)
                if new_map[new_index] is None:
                    new_map[new_index] = Node(current.menu_item)
                else:
                    temp = new_map[new_index]
                    while temp.next is not None:
                        temp = temp.next
                    temp.next = Node(current.menu_item)
                current = current.next

        # Update hashmap properties
        self.map = new_map
        self.capacity = new_capacity

    def insert(self, menu_item):
        # check load factor
        if self.size / self.capacity >= self.load_factor:
            self._rehash()

        index = hash(menu_item) % self.capacity
        print (index)
        if self.map[index] is None:
            self.map[index] = menu_item
            self.size += 1
        else:
            current = self.map[index]
            while current.next is not None:
                current = current.next
            current.next = menu_item
            self.size += 1

    #write a search/retreival function