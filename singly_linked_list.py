class Student:
    def __init__(self, id, name, mark):
        self.id = id
        self.name = name
        self.mark = mark

    def create(self):
        self.id = input('ID: ')
        self.name = input('Name: ')
        self.mark = int(input('Mark: '))

    
    def update(self):
        self.id = input('ID: ')
        self.name = input('Name: ')
        self.mark = int(input('Mark: '))

    def show(self):
        print(self.id)
        print(self.name)
        print(self.mark)

class Node:
    def __init__(self,data:Student):
        self.data = data
        # next to Node
        self.next = None

class Singular_linked_list:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_first(self, data:Student): 
        newNode = Node(data)
        if self.checkExist(data.id) == None:
            newNode.next = self.head
            self.head = newNode
            self.size += 1
        else:
            return

    


    def checkExist(self, id):
        temp = self.head
        while temp != None:
            if temp.data.id == id:
                return temp
            temp = temp.next
        return None
            

    # add 1 factor into object having id = id
    def insert_after(self, id, data:Student):

        #Node contain student.id
        newNode = Node(data)
        #check
        if self.size == 0:
            self.head = newNode
            self.size = 1
            return
           
        elif self.checkExist(id) != None and self.checkExist(data.id) == None:
            p = self.head
            while p.data.id != id:
                p = p.next
            newNode.next = p.next
            p.next = newNode
            self.size += 1        

    def insert_last(self, data:Student):  
        newNode = Node(data)
        p = self.head
        if self.checkExist(data.id) == None:
            while p.next != None:
                p = p.next
            p.next = newNode
            self.size += 1
        
    def removeFisrt(self):
        temp = self.head
        if self.size == 0:
            print('Empty')
            return
        self.head = self.head.next
        temp = None
        self.size -= 1
    
    def removeLast(self):
        if self.size == 0:
            print('Empty')
            return
        temp = self.head 
        last = temp.next
        while last.next != None:
            temp = temp.next
            last = last.next 
        temp.next = None
        self.size -= 1

    def remove_id(self, id):
        if self.size == 0:
            print('Empty')
            return
        
        temp = self.head
        id_need = temp.next
        p = self.checkExist(id)
        if p != None:
            while id_need.data.id != p.data.id:
                    temp = temp.next
                    id_need = id_need.next
            temp.next = p.next
            p.next = None
        else:
            return
                
    def display(self):
        if self.size == 0:
            print('Empty')
            return
        else:
            temp = self.head
            while temp != None:
                temp.data.show()
                temp = temp.next

    def update(self, id, data: Student):
        if self.size == 0:
            print('Empty')
            return 
        elif self.checkExist(id) != None and self.checkExist(data.id) == None:
            temp = self.head
            while temp.data.id != id:
                temp = temp.next
            temp.data = data

    def search(self, id):
        if self.size == 0:
            print('Empty')
            return 
        temp = self.checkExist(id)
        if temp == None:
            return None
        print("The student", id,"is")
        temp.data.show()
            
def main():
    def display_menu():
        print("\n\nMenu:")
        print("1. Insert at the beginning")
        print("2. Insert at the end")
        print("3. Insert after a node")
        print("4. Remove the first node")
        print("5. Remove the last node")
        print("6. Remove a node by ID")
        print("7. Display the linked list")
        print("8. Update a node by ID")
        print("9. Search for a node by ID")
        print("0. Exit")

    linked_list = Singular_linked_list()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            userValue = Student('a','b',0)
            userValue.create()
            linked_list.insert_first(userValue)
        elif choice == "2":
            userValue = Student('a','b',0)
            userValue.create()
            linked_list.insert_last(userValue)
        elif choice == "3":
            after_id = input("Insert after student: ")
            userValue = Student('a','b',0)
            userValue.create()
            linked_list.insert_after(after_id, userValue)
        elif choice == "4":
            linked_list.removeFisrt()
        elif choice == "5":
            linked_list.removeLast()
        elif choice == "6":
            id_to_remove = input("Enter the ID to remove: ")
            linked_list.remove_id(id_to_remove)
        elif choice == "7":
            linked_list.display()
        elif choice == "8":
            id_to_update = input("Enter the ID to update: ")
            userValue = Student('a','b',0)
            userValue.update()
            linked_list.update(id_to_update, userValue)
        elif choice == "9":
            id_to_search = input("Enter the ID to search: ")
            linked_list.search(id_to_search)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

    print("Exiting the program.")


main()

