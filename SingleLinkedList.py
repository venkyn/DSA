class Node:
    def __init__(self, value):
        self.info = value
        self.link = None


class SingleLinkedList():

    def __init__(self):
        self.start = None

    def display_list(self):
        p = self.start
        while p.link is not None:
            print(p.info, ' ', " ")
            p = p.link

    def count_nodes(self):
        if self.start is None:
            print('list is empty')
            return
        else:
            p = self.start
            count = 0
            while p.link is not None:
                count += 1
                p = p.link
            print('count: ' + count)

    def search(self, x):
        position = 1
        p = self.start
        while p.link is not None:
            if p.info == x:
                print('p is at position: ' + position)
                return
            else:
                p = p.link
                position += 1
        print(' ' + x + ' not found in list')

    def insert_in_beginning(self, data):
        pass

    def insert_at_end(self, data):
        pass

    def create_list(self):
        pass

    def insert_after(self, data, x):
        pass

    def insert_before(self, data, x):
        pass

    def insert_at_position(self, data, x):
        pass

    def delete_node(self, x):
        pass

    def delete_first_node(self):
        pass

    def delete_last_node(self):
        pass

    def reverse_list(self):
        pass

    def bubble_sort_exdata(self):
        pass

    def bubble_sort_exlinks(self):
        pass

    def has_cycle(self):
        pass

    def find_cycle(self):
        pass

    def remove_cycle(self):
        pass

    def insert_cycle(self, x):
        pass

    def merge2(self, list2):
        pass

    def _merge2(self, p1, p2):
        pass

    def merge_sort(self):
        pass

    def _merge_sort_rec(self, list_start):
        pass

    def _divide_list(self, p):
        pass


list = SingleLinkedList()

list.create_list()

while True:
    print('1. display')
    option = int(input('Enter your choice: '))

    if option == 1:
        list.display_list()
    elif option == 19:
        break
    else:
        print('wrong option')
    print()
