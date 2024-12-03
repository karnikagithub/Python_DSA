from collections import deque
# stack = deque()


class Stack:
    def __init__(self):
        self.container = deque()
        
    def push(self,value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    

s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

print(s.size())



def reverse_string(strng):

    stck = Stack()

    for char in strng:
        stck.push(char)

    reverse_str = ''
    while stck.size() != 0:
        reverse_str += stck.pop()

    return reverse_str


print(reverse_string('im learning the DSA in Python'))


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x: int):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack:
            top = self.stack.pop()
            if top == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None
    
    def getStck(self):
        return self.stack

# Example usage:
min_stack = MinStack()
min_stack.push(3)
min_stack.push(5)
# print(min_stack.getMin())  # Output: 3
min_stack.push(2)
min_stack.push(1)
# print(min_stack.getMin())  # Output: 1
min_stack.pop()
# print(min_stack.getMin())  # Output: 2
min_stack.pop()
# print(min_stack.top())     # Output: 5
print(min_stack.getMin(),'llllllllll')  # Output: 3
print(min_stack.getStck())




def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(strng):
    stack = Stack()
    for ch in strng:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0

print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("((a+g))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))