class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    # Constructor to initialize the root of linked list
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def push(self, data):
        if self.is_empty == True:
            self.head = StackNode(data)
        else:
            new_node = StackNode(data)
            new_node.next = self.head
            self.head = new_node
    
    def pop(self):
        if self.is_empty():
            return None
        else:
            p = self.head
            self.head = self.head.next
            p.next = None
            return p.data
    
    def top(self):
        if self.is_empty():
            return None
        else:
            return self.head.data
        
    def dislay(self):
        if self.is_empty():
            print('Empty Stack')
        else:
            p = self.head
            while p != None:
                print(p.data, '-->', end = ' ')
                p = p.next

st = Stack()
print(st.pop())
st.push(1)
st.push(4)
st.push(1)
st.dislay()
