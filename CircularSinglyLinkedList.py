class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
    
class CircularSinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        n=self.head
        while n:
            yield n
            if n.next==self.head:
                break
            n=n.next
    
    def insert(self,loc,value):
        newNode=Node(value)
        if self.head==None and self.tail==None:
            newNode.next=newNode
            self.head=newNode
            self.tail=newNode
        else:
            if loc==0:
                newNode.next=self.head
                self.head=newNode
                self.tail.next=newNode
            elif loc==-1:
                self.tail.next=newNode
                newNode.next=self.head
                self.tail=newNode
            else:
                n=self.head
                for i in range(loc):
                    n=n.next
                temp=n.next
                n.next=newNode
                newNode.next=temp
    
    def traverse(self):
        n=self.head
        while n:
            print(n.val)
            if n.next==self.head:
                break
            n=n.next
    
    def delete(self,loc):
        if not self.head:
            return 'Empty Linked List'
        else:
            if loc==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.tail.next=self.head
            elif loc==-1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    n=self.head
                    while n:
                        if n.next==self.tail:
                            break
                        n=n.next
                    
                    n.next=self.tail.next
                    self.tail=n
                    self.tail.next=self.head
            else:
                n=self.head
                for i in range(loc):
                    n=n.next
                n.val=n.next.val
                n.next=n.next.next
            

l1=CircularSinglyLinkedList()
l1.insert(0,1)
l1.insert(-1,2)
l1.insert(-1,3)
l1.insert(-1,4)
l1.insert(-1,5)
l1.insert(2,7)
print([i.val for i in l1])
l1.delete(4)
print([i.val for i in l1])
l1.traverse()



