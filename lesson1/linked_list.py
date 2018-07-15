from lesson1.node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, node):
        if self.head is None:
            self.head = node
            node.prev = None
            node.next = None
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def print_all_nodes(self):
        _head = self.head
        while _head:
            print(_head.value, end="->")
            _head = _head.next

    def find(self, value):
        _head = self.head
        while _head is not None:
            if _head.value == value:
                return _head
            _head = _head.next
        return None

    def delete_node(self, value):
        prev = None
        _head = self.head
        if _head is not None:
            if _head.value == value:
                self.head = _head.next
                _head = None
                return
        while (_head is not None):
            if _head.value == value:
                break
            prev = _head
            _head = _head.next
        if prev.next is not None:
            prev.next = _head.next
        _head = None

    def delete_nodes(self, value):
        while self.find(value) is not None:
            self.delete_node(value)

    def delete_all_nodes(self):
        _head = self.head
        if _head is not None:
            while _head is not None:
                temp = _head.next
                _head.value = None
                _head = temp

    def find_nodes(self, value):
        new_list = LinkedList()
        _head = self.head
        while _head is not None:
            if _head.value == value:
                new_list.add_in_tail(_head)
            _head = _head.next
        return new_list

    def list_size(self):
        num = 0
        _head = self.head
        while _head is not None:
            num += 1
            _head = _head.next
        return num

    def add_after(self, node1, node2):
        if node1 and node2 is not None:
            node2.next = node1.next
            node1.next = node2

    def merge_lists(self, list1, list2):
        if list1.head and list2.head is not None:
            list = LinkedList()
            if list1.list_size() == list2.list_size():
                while list1.head and list2.head is not None:
                    list.add_in_tail(Node(list1.head.value + list2.head.value))
                    list1.head = list1.head.next
                    list2.head = list2.head.next
                return list
            else:
                raise Exception

    def add_first(self, node):
        if node is not None:
            _head = self.head
            self.head = node
            while _head.next is not None:
                self.head.next = _head
            _head = _head.next

