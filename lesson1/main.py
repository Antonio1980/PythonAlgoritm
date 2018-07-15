from lesson1.linked_list import LinkedList
from lesson1.node import Node
import unittest

class Tester(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.n1 = Node(12)
        cls.n2 = Node(55)
        cls.n3 = Node(50)
        cls.s_list = LinkedList()

    @classmethod
    def test_delete_node(cls):
        cls.n1.next = cls.n2
        cls.s_list.add_in_tail(cls.n1)
        cls.s_list.add_in_tail(cls.n2)
        cls.s_list.add_in_tail(Node(128))
        cls.s_list.delete_node(128)
        if cls.s_list.find(128) is None:
            print("test_delete_node - PASSED")

    @classmethod
    def test_delete_nodes(cls):
        cls.n1.next = cls.n2
        cls.s_list.add_in_tail(cls.n1)
        cls.s_list.add_in_tail(cls.n2)
        cls.s_list.add_in_tail(Node(12))
        cls.s_list.add_in_tail(Node(128))
        cls.s_list.delete_nodes(12)
        if cls.s_list.find(12) is None:
            print("test_delete_nodes - PASSED")

    @classmethod
    def test_delete_all_nodes(cls):
        cls.n1.next = cls.n2
        cls.s_list.add_in_tail(cls.n1)
        cls.s_list.add_in_tail(cls.n2)
        cls.s_list.add_in_tail(Node(128))
        cls.s_list.delete_all_nodes()
        print("test_delete_all_nodes:")
        cls.s_list.print_all_nodes()

    @classmethod
    def test_list_size(cls):
        cls.n1.next = cls.n2
        cls.s_list.add_in_tail(cls.n1)
        cls.s_list.add_in_tail(cls.n2)
        cls.s_list.add_in_tail(Node(128))
        if cls.s_list.list_size() == 2:
            print("test_list_size - PASSED")

    @classmethod
    def test_add_node(cls):
        cls.n1.next = cls.n2
        cls.s_list.add_in_tail(cls.n1)
        cls.s_list.add_in_tail(cls.n2)
        cls.s_list.add_in_tail(Node(128))
        cls.s_list.add_after(cls.n2, cls.n3)
        if cls.s_list.list_size() == 4:
            print("test_add_node - PASSED")

    @classmethod
    def test_merge_lists(cls):
        list, list1, list2 = LinkedList(), LinkedList(), LinkedList()
        node1, node2, node3 = Node(50), Node(100), Node(200)
        node1_1, node2_2, node3_3 = Node(500), Node(1500), Node(2008)
        node1.next, node2.next = node2, node3
        node1_1.next, node2_2.next = node2_2, node3_3
        list1.add_in_tail(node1)
        list2.add_in_tail(node1_1)
        print("test_merge_lists:")
        list1.print_all_nodes()
        list2.print_all_nodes()
        list = list.merge_lists(list1, list2)
        list.print_all_nodes()
        assert list.list_size() == 3
        assert list.head.value == 550
        assert list.head.next.value == 1600
        next = list.head.next
        assert next.next.value == 2208

    @classmethod
    def test_add_first(cls):
        cls.n1.next = cls.n2
        cls.n2.next = cls.n3
        n4 = Node(20)
        cls.s_list.add_in_tail(cls.n1)
        cls.s_list.add_in_tail(cls.n2)
        cls.s_list.add_in_tail(cls.n3)
        cls.s_list.add_first(n4)
        assert cls.s_list.list_size() == 4
        cls.s_list.print_all_nodes()


if __name__ == '__main__':
    Tester.setUpClass()
    Tester.test_add_first()
