class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None

class ll:
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
        if not self.head:
            self.head=newNode
            self.tail=newNode
        else:
            if loc==0:
                newNode.next=self.head
                self.head=newNode
            elif loc==-1:
                self.tail.next=newNode
                self.tail=newNode
            else:
                n=self.head
                for i in range(loc):
                    n=n.next
                temp=n.next
                n.next=newNode
                newNode.next=temp
        
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
            elif loc==-1:
                n=self.head
                while n:
                    if n.next==self.tail:
                        break
                    n=n.next
                n.next=None
                tail=n
            else:
                n=self.head
                for i in range(loc):
                    n=n.next
                
                n.val=n.next.val
                n.next=n.next.next
        

    
l1=ll()
l1.insert(-1,1)
l1.insert(-1,2)
l1.insert(-1,3)
l1.insert(-1,4)
l1.insert(2,10)
#l1.delete(-1)
print([i.val for i in l1])


