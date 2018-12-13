class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.arbit = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            temp.next = Node(data)
            temp = temp.next
            temp.data = data
            temp.next = None

    def display(self):
        if self.head is not None:
            temp = self.head
            while temp is not None:
                print temp.data
                temp = temp.next
        else:
            print "Q is empty"

    def arbit_updater(self):
        temp = self.head
        temp.arbit = temp.next.next # 1 - 3
        temp = temp.next
        temp.arbit = temp.next.next.next.next # 2 - 6
        temp = temp.next
        temp.arbit = temp.next # 3 -4
        temp = temp.next
        temp.arbit = self.head
        temp = temp.next
        temp.arbit = self.head.next
        t1 = temp.next
        t1.arbit = temp

    def display_arbit(self):
        if self.head is not None:
            temp = self.head
            if self.head is not None:
                temp = self.head
                while temp is not None:
                    print temp.data, '--', temp.arbit.data
                    temp = temp.next
            else:
                print "Q is empty"

    def clone_list(self):
        l2 = LinkedList()
        if self.head is not None:
            temp = self.head
            while temp is not None:
                l2.insert(temp.data)
                temp = temp.next
        else:
            return None
        l2.arbit_updater()
        return l2

l1 = LinkedList()
for i in range(1, 7):
    l1.insert(i)
l1.arbit_updater()

l2 = l1.clone_list()
l2.display_arbit()
