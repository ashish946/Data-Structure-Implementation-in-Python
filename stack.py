class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class stack:
    def __init__(self):
        self.head=None
    
    def __iter__(self):
        n=self.head
        while n:
            yield n
            n=n.next
    
    def push(self,value):
        newNode=Node(value)
        if not self.head:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    
    def pop(self):
        if not self.head:
            return 'Stack is empty'
        t=self.head.val
        self.head=self.head.next
        return t

st=stack()
st.push(1)
st.push(2)
st.push(3)


print([i.val for i in st])
print(st.pop())
print([i.val for i in st])

                