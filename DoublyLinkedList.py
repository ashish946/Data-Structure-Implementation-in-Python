class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    

    def __iter__(self):
        n=self.head
        while n:
            yield n
            n=n.next

    def insert(self,loc,value):
        newNode=Node(value)
        if loc==0:
            if self.head==None:
                self.head=newNode
                self.tail=newNode
            else:
                newNode.next=self.head
                self.head.prev=newNode
                self.head=newNode
        elif loc==-1:
            if self.tail==None:
                self.head=newNode
                self.tail=newNode
            else:
                self.tail.next=newNode
                newNode.prev=self.tail
                self.tail=newNode
        else:
            n=self.head
            for i in range(loc):
                n=n.next
            temp=n.next
            n.next=newNode
            newNode.prev=n
            newNode.next=temp
            temp.prev=newNode
    
    def traverse(self):
        if not self.head:
            print('Linked list is empty')
        t=self.head
        while t:
            print(t.val)
            t=t.next
    
    def reversetraverse(self):
        if not self.tail:
            print('Linked list is empty')
        t=self.tail
        while t:
            print(t.val)
            t=t.prev
        
    def delete(self,loc):

        if self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            if loc==0:
                t=self.head
                self.head=self.head.next
                self.head.prev=None
                t.next=None
            elif loc==-1:
                t=self.tail
                self.tail=self.tail.prev
                self.tail.next=None
                t.prev=None
            else:
                n=self.head
                for i in range(loc-1):
                    n=n.next
                t=n.next
                n.next=t.next
                t=t.next
                t.prev=t.prev.prev




d1=DoublyLinkedList()
d1.insert(-1,1)
d1.insert(-1,2)
d1.insert(-1,3)
d1.insert(-1,4)
d1.insert(-1,5)
d1.insert(-1,6)
d1.insert(3,10)
print([i.val for i in d1])
d1.delete(4)
print([i.val for i in d1])
#d1.reversetraverse()
            
                
                
        