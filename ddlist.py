class Node:
    def _init__(self, data):
        self.data = data # Stores data
        self.next = None # Contains the reference of next node
        self.prev = None # Contains the reference of previous node
class doubly_linked_list:
    def _init__(self):
        self.head = None # Contains the reference of first node of the list
        self.last = None # Contains the reference of the last node of the
    def insertend(self,data):
        newnode=Node(data)
        newnode.prev = self.last
        if self.head == None:
            self.head = newnode
            self.last = newnode
        else:
            self.last.next = newnode
            self.last = newnode
    def deleteend(self):
        if(self.head!=None):
            if(self.head==self.last):
                self.head=None
                self.last=None
            else:
                self.last=self.last.prev
                self.last.next=None


        def traverse(self):
            temp = self.head
            while temp != None:
                if temp.next != None:
                    print(temp.data, end=',')
                else:
                    print(temp.data)
                temp = temp.next
        def traverse_rev(self):
            temp = self.last
            while temp != None:
                if temp.prev != None:
                    print(temp.data, end=',')
                else:
                    print(temp.data)
            temp = temp.prev


ins = eval(input())
delt = int(input())
A = doubly_linked_list()
for i in ins:
    A.insertend(i)
for j in range(delt):
    A.deleteend()
A.traverse()
A.traverse_rev()