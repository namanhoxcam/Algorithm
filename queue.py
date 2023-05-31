class QueueNode:
    def __init__(self, data):
        self.data = data 
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def enqueue(self):
        if self.is_empty == True:
            self.head = QueueNode(data)
        else:
            new_node = QueueNode(data)
            new_node.next = self.head
            self.head = new_node
    
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            p = self.head
            a = p.next
            while a.next != None:
                p = p.next
                a = a.next
            p.next = None
            return a.data
        
    def first(self):
        if self.is_empty():
            return None
        else:
            return self.head.data
    
    def last(self):
        if self.is_empty():
            return None
        else:
            p = self.head
            while p.next != None:
                p = p.next
            return p.data

            
  