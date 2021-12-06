class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def __iter__(self):
        n=self.head
        while n:
            yield n
            n=n.next

    def Enqueue(self,val):
        newNode=Node(val)
        if not self.head:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
    
    def Dequeue(self):
        if not self.head:
            return 'Queue is empty'
        t=self.head.val
        if self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next

        return t


q1=Queue()
q1.Enqueue(1)
q1.Enqueue(2)
q1.Enqueue(3)
print([i.val for i in q1])
print(q1.Dequeue())
print(q1.Dequeue())
print(q1.Dequeue())


print([i.val for i in q1])

            