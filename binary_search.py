def binary_search(arr,target):

    """ Time Complexity: O(log n) - Binary search repeatedly halves the search space, 
        so the time complexity is logarithmic.
        Space Complexity: O(1) - Binary search uses only a constant amount of extra space for variables."""
    
    start, end = 0, len(arr) - 1
    
    while start <= end:
        mid = (start+end) // 2
        
        if arr[mid] == target:
            return mid
        
        ## search continues to left
        elif arr[mid] < target:
            start = mid + 1
        
        ## search continues to right
        else:
            end = mid - 1
            
    return -1
    

def recursive_binary(arr,low,high,target):

    """ Time Complexity: O(log n) - Same as iterative binary search.
        Space Complexity: O(log n) - Due to the recursive calls, the space complexity is logarithmic,
        as the maximum number of recursive calls on the call stack is logarithmic in the size of the input."""
    
    if low > high:
        return -1
    
    mid = (low+high) // 2

    if arr[mid] == target:
        return mid
        
    elif arr[mid] < target:
        return recursive_binary(arr,mid + 1,high,target)
    else:
        return recursive_binary(arr,low,mid - 1, target)
        


arr = [1,2,3,4,5,6,7,8,9]


print(binary_search(arr,9))

print(recursive_binary(arr,0,len(arr) -1,9))




class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


    def add_child(self,data):
        if self.data == data:
            return
        
        if data < self.data:
            ## meaning we've to add data to the LEFT SUB TREE
            if self.left:
                ## HERE WE'RE CALLING add_child() METHOD RECURSIVELY TO SAVE THE DATA,
                ## BECAUSE SELF.LEFT IS ANOTHER SUBTREE WHICH WILL HAVE add_child() value TAKES DATA
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            ## meaning we've to add data to the RIGHT SUB TREE
            if self.right:
                ## HERE WE'RE CALLING add_child() METHOD RECURSIVELY TO SAVE THE DATA,
                ## BECAUSE SELF.RIGHT IS ANOTHER SUBTREE WHICH WILL WILL HAVE add_child() value TAKES DATA
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def in_order_traversal(self):
        ## this method will return list of elements in your binary tree in a SPECIFIC ORDER
        ## VISIT LEFT TREE => BASE NODE => RIGTH TREE
        elements = []

        ## visits left sub tree
        if self.left:
            elements += self.left.in_order_traversal()

        ## visits base node
        elements.append(self.data)

        ## visits right sub tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements


    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        
        return elements
    

    def search(self,val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    

    def find_min(self):

        if self.left is None:
            # print(self.left,'---------------',self.data)
            return self.data
      
        return self.left.find_min()
    

    def find_max(self):

        if self.right is None:
            # print(self.right,'---------------',self.data)
            return self.data

        return self.right.find_max()


    def calculate_sum(self):

        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        calculated_sum = left_sum + right_sum + self.data
        # print(left_sum,right_sum,'---')
        # print(self.data,'self.dataself.dataself.dataself.data')
        return calculated_sum
    

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            
            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.right.delete(max_val)

        return self

        
# helper function to build binary tree
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


numbers = [4,7,8,2,3,4,6,1,5,9,0,9]

build_numbers = build_tree(numbers)
# print(build_numbers)
print(build_numbers.in_order_traversal(),'  : IN-ORDER TRAVERSAL')
# print(build_numbers.post_order_traversal(),'  : POST-ORDER TRAVERSAL')
# print(build_numbers.pre_order_traversal(),'  : PRE-ORDER TRAVERSAL')
# print(build_numbers.find_min(),'  : FIND_MIN')
# print(build_numbers.find_max(),'  : FIND_MAX')
# print(build_numbers.calculate_sum(),'  : CALCULATED SUM')
# print(build_numbers.search(99))
print(build_numbers.delete(5))
print(build_numbers.in_order_traversal(),'  : IN-ORDER TRAVERSAL AFTER DELETING')


# countries = ['india','usa','uk','afghanistan','bermuda','columbia']

# show_countries = build_tree(countries)
# print(show_countries)
# print(show_countries.in_order_traversal())
# print(show_countries.search('india'))