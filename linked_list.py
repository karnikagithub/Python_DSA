
### this class Node represents individual element in the LINKED LIST
class Node:
    def  __init__(self,data=None,next=None):
        self.data = data  ## data can be any TYPE.
        self.next = next  ## is the pointer to the NEXT element.



class LinkedList:
    def __init__(self):
        self.head = None ## HEAD points to the head of LINKED LIST.


    def print(self):
        if self.head is None:
            print('Linked List is Empty')
            return
    
        itr = self.head
        lst_elements = []
        while itr:
            lst_elements.append(str(itr.data))
            itr = itr.next

        print(lst_elements)


    def get_length(self):
        count = 0
        itr = self.head
        
        while itr:
            count +=1
            itr = itr.next

        # print(count)
        return count
    

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node


    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)

    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1
    
    def remove_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
         
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
            count += 1


    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


    def insert_after_value(self,data_after,data_to_insert) :
        if self.head is None:
            return
        
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next)
                break

            itr = itr.next

    
    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


    def reverse(self):
        prev_node = None
        itr = self.head

        while itr:
            next_node = itr.next  # Save the next node
            itr.next = prev_node  # Reverse the pointer
            prev_node = itr
            itr = next_node

        self.head = prev_node  # Set the head to the last node (which was the first in the original list)


    def middleNode(self):

        fast = self.head
        slow = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print(slow.data)
        return slow
    

    def sort(self):
        if self.head is None:
            return

        # Get the length of the linked list
        length = self.get_length()

        # Perform Bubble Sort
        for i in range(length):
            itr = self.head
            while itr.next:
                if itr.data < itr.next.data:
                    # Swap the data of the current node and the next node
                    temp = itr.data
                    itr.data = itr.next.data
                    itr.next.data = temp
                itr = itr.next


        

if __name__ == '__main__':

    ll = LinkedList()

    ll.insert_values([1,2,3,4,5,6,78,82,45,93])
    ll.insert_at_end(984)
    ll.insert_at_begining(2000)
    # ll.remove_at(1)
    # ll.insert_at(0,'srinah')
    # ll.insert_at(2,'srinath')
    ll.print()
    ll.insert_after_value(2,100)
    # ll.insert_after_value(5,100)
    # ll.get_length()
    ll.print()
    # ll.remove_at(2)
    # ll.remove_by_value(2)
    ll.middleNode()
    ll.sort()
    ll.reverse()
    ll.print()
    












        

        