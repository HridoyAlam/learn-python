from typing import Counter


class Node:
    def __init__(self, data= None, next = None):
        self.data = data
        self.next = next

class Linked_list:

    def __init__(self):
        self.head = None


    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node


    def insert_at_end(self,data):
        if self.head == None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)


    def print_linked_list(self):
        if self.head == None:
            print("Linked list is empty")
            return
        
        itr = self.head
        listr = ''

        while itr:
            listr += str(itr.data) + ' --> '
            itr = itr.next
        print(listr)


    def insert_linked_list(self,data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)


    def get_length(self):

        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count


    def remove_item(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1

    def insert_at_index(self, index, data):
        if index < 0 or index> self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count  = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
                break

            itr = itr.next
            count +=1


if __name__ == '__main__':
    li = Linked_list()
    li.insert_at_begining(82)
    li.insert_at_begining(83)
    li.insert_at_end(10)
    li.insert_linked_list(['bangla', 'english', 'hindi'])
    li.print_linked_list()
    print(li.get_length())