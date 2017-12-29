# Single Linked List
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
            print(p.info)
            p = p.link
        print(p.info)

    def count_nodes(self):
        if self.start is None:
            print('list is empty')
            return
        else:
            p = self.start
            count = 1
            while p.link is not None:
                count += 1
                p = p.link
            print('count: ' + str(count))

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
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def insert_at_end(self, data):
        temp = Node(data)
        if self.start  is None:
            self.start = temp
            return
        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp

    def create_list(self):
        n = int(input('enter the number of nodes: '))
        if n == 0:
            return
        for i in range(n):
            data = int(input('enter element: '))
            self.insert_at_end(data)

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


linked_list = SingleLinkedList()

linked_list.create_list()

while True:
    print('1. display')
    print('2. count')
    print('3. search for an element')
    print('4. insert in an empty list')
    print('5. insert a node at the end')
    print('6. insert a node before a specified node')
    print('7. insert at a given position')
    print('19. exit')
    option = int(input('Enter your choice: '))

    if option == 1:
        linked_list.display_list()
    elif option == 2:
        linked_list.count_nodes()
    elif option == 3:
        data = int(input('enter the element to be searched: '))
        linked_list.search(data)
    elif option == 4:
        data = int(input('enter the element to be inserted: '))
        linked_list.insert_in_beginning(data)
    elif option == 5:
        data = int(input('enter the element to be inserted: '))
        linked_list.insert_at_end(data)
    elif option == 19:
        break
    else:
        print('wrong option')
    print()
