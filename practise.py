l1 = [5,3,10,9]
l2 = [7,9,24,26]
l3 = [6,8,2,1]



class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


    def print(self):
        if self.head is None:
            return
        
        itr = self.head
        lst_elements = []
        while itr:
            lst_elements.append(itr.data)
            itr = itr.next

        print(lst_elements)


    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node


    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)




ll = LinkedList()
ll.insert_at_begining(l1)
ll.insert_at_end(l2)
ll.print()
