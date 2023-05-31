class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class circle_linked_list:
    def ___init__(self) -> None:
        self.last = None
        self.size = 0

    def checkData(data):
        temp = self.last
        while temp.next != self.last:
            temp = temp.next
            if temp.data == data:
                return True
        return False
        
    def insertFirst(self, data):
        newNode = Node(data)
        if self.checkData(data):
        
    def insertAfter(self,after_data,data):
        newNode = Node(data)
            self.size == 0:
            print ('Empty')
            return
        elif self.checkData(after_data):
            temp = self.last
            while temp.data != data:
                temp = temp.next
            newNode.next = temp.next
            temp.next = newNode
        return
